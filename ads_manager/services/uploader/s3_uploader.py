import datetime
import typing

from ads_manager import enums, exceptions, utils
from ads_manager.integrations.clients.s3 import client as s3_client
from ads_manager.integrations.clients.s3 import exceptions as s3_client_exceptions


def upload_resource_details(
    s3_path: str, resource_details: typing.List[typing.Dict], resource_type: enums.ResourceType
) -> str:
    try:
        uploaded_path = s3_client.S3Uploader(s3_path=s3_path).upload_resource_details(
            resource_details=resource_details,
            resource_type=resource_type,
            date_created=datetime.datetime.utcnow(),
        )
    except s3_client_exceptions.S3UploaderError as e:
        raise exceptions.ImporterException(utils.get_exception_message(exception=e))

    return uploaded_path


def upload_resource_insights(
    s3_path: str, resources_insights: typing.List[typing.Dict], resource_type: enums.ResourceType
) -> typing.List[str]:
    try:
        uploaded_path = s3_client.S3Uploader(s3_path=s3_path).upload_resource_performance(
            resource_performance=resources_insights,
            resource_type=resource_type,
            date_created=datetime.datetime.utcnow(),
        )
    except s3_client_exceptions.S3UploaderError as e:
        raise exceptions.ImporterException(utils.get_exception_message(exception=e))

    return uploaded_path


def upload_facebook_ad_creatives(s3_path: str, ad_creatives: typing.List[typing.Dict]) -> typing.List[str]:
    try:
        uploaded_paths = s3_client.S3Uploader(s3_path=s3_path).upload_resource_assets(
            asset_list=ad_creatives,
            resource_type=enums.ResourceType.AD_CREATIVE,
            date_created=datetime.datetime.utcnow(),
        )
    except s3_client_exceptions.S3UploaderError as e:
        raise exceptions.ImporterException(utils.get_exception_message(exception=e))

    return uploaded_paths
