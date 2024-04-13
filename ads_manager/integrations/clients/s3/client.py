import datetime
import json
import logging
import typing

import boto3
import requests

from ads_manager import enums, utils
from ads_manager.integrations.clients.s3 import constants as s3_client_constants
from ads_manager.integrations.clients.s3 import exceptions as s3_client_exceptions

logger = logging.getLogger(__name__)


class S3Uploader(object):
    def __init__(self, s3_path: str) -> None:
        self._bucket_name = None
        self._prefix = None
        self._setup_bucket_name_and_prefix(s3_path=s3_path)

        self._bucket = boto3.Session().resource(service_name="s3").Bucket(self._bucket_name)

    def _setup_bucket_name_and_prefix(self, s3_path: str) -> None:
        if not s3_path.startswith("s3://"):
            raise s3_client_exceptions.S3PathIsNotValidError("S3 path (path_name={}) is not valid".format(s3_path))

        s3_path_parts = s3_path.replace("s3://", "").split("/")
        self._bucket_name = s3_path_parts[0]
        self._prefix = "/".join(s3_path_parts[1:]).rstrip("/")

    def upload_resource_details(
        self,
        resource_details: typing.List[typing.Dict],
        resource_type: typing.Union[enums.ResourceType, enums.TiktokResourceType, enums.FacebookResourceType],
        date_created: datetime.datetime,
    ) -> str:
        return self._upload_data(
            data=resource_details,
            file_path="{}/date_created={}/details.json".format(
                resource_type.value,
                self._get_formatted_date_created(date_created=date_created),
            ),
        )

    def upload_resource_performance(
        self,
        resource_performance: typing.List[typing.Dict],
        resource_type: typing.Union[enums.ResourceType, enums.TiktokResourceType, enums.FacebookResourceType],
        date_created: datetime.datetime,
    ) -> typing.List[str]:
        uploaded_paths = []
        date_created_formatted = self._get_formatted_date_created(date_created=date_created)
        for performance_data in resource_performance:
            uploaded_path = self._upload_data(
                data=performance_data,
                file_path="{}/{}={}/date_created={}/performance_{}.json".format(
                    resource_type.value,
                    resource_type.value,
                    performance_data["{}_id".format(resource_type.value)],
                    date_created_formatted,
                    performance_data["date_start"],
                ),
            )
            uploaded_paths.append(uploaded_path)

        return uploaded_paths

    def upload_resource_assets(
        self,
        asset_list: typing.List[typing.Dict],
        resource_type: enums.ResourceType,
        date_created: datetime.datetime,
    ) -> typing.List[str]:
        s3_paths = []
        date_created_formatted = self._get_formatted_date_created(date_created=date_created)
        for asset in asset_list:
            if not asset.get("image_url"):
                continue

            upload_path = self._upload_image_from_url(
                file_path="{}/{}={}/date_created={}/asset.png".format(
                    resource_type.value,
                    resource_type.value,
                    asset["id"],
                    date_created_formatted,
                ),
                image_url=asset["image_url"],
            )
            s3_paths.append(upload_path)

        return s3_paths

    def _upload_data(
        self,
        data: typing.Union[typing.List[typing.Dict], typing.Dict],
        file_path: str,
    ) -> str:
        file_path_with_prefix = f"{self._prefix}/{file_path}"
        try:
            self._bucket.put_object(
                Key=file_path_with_prefix,
                Body=json.dumps(data, indent=4),
            )
        except Exception as e:
            raise s3_client_exceptions.S3ClientError(
                "Unable to upload data to S3 path (path_name={}). Error: {}".format(
                    file_path_with_prefix, utils.get_exception_message(exception=e)
                )
            )

        return self._get_full_s3_path(file_path=file_path_with_prefix)

    def _upload_image_from_url(
        self,
        file_path: str,
        image_url: str,
    ) -> str:
        file_path_with_prefix = f"{self._prefix}/{file_path}"
        try:
            self._bucket.upload_fileobj(requests.get(image_url, stream=True).raw, file_path_with_prefix)
        except Exception as e:
            raise s3_client_exceptions.S3ClientError(
                "Unable to upload image data to S3 path (path_name={}, image_url={}). Error: {}".format(
                    file_path_with_prefix,
                    image_url,
                    utils.get_exception_message(exception=e),
                )
            )

        return file_path_with_prefix

    @staticmethod
    def _get_formatted_date_created(date_created: datetime) -> str:
        return date_created.strftime(s3_client_constants.DATE_CREATED_FORMAT)

    def _get_full_s3_path(self, file_path: str) -> str:
        return "s3://{}/{}".format(self._bucket_name, file_path)
