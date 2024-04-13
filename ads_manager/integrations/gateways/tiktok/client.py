import datetime
import json
import typing

import requests

from ads_manager import enums, utils
from ads_manager.integrations.gateways.tiktok import exceptions as tiktok_api_exceptions


class TikTokApiClient(object):
    BASE_URL_PROD = "https://business-api.tiktok.com/open_api/v1.3"
    BASE_URL_SANDBOX = "https://sandbox-ads.tiktok.com/open_api/v1.3"
    VALID_STATUS_CODES = [200]
    VALID_PAYLOAD_STATUS_CODES = [0, 20001]
    LIMIT = 1000

    def __init__(self, user_access_token: str, params: typing.Dict = None) -> None:
        self._user_access_token = user_access_token
        self._params = params  # {"sandbox: True"}

    @property
    def base_url(self):
        if self._params and self._params.get("sandbox"):
            return self.BASE_URL_SANDBOX
        return self.BASE_URL_PROD

    def get_ad_accounts(self, params) -> typing.List[typing.Dict]:
        return self._get_content(
            response=self._request(endpoint="oauth2/advertiser/get/", method=enums.HttpMethod.GET, params=params),
        )["data"]["list"]

    def get_advertiser_campaigns(self, advertiser_id: str, fields: typing.List[str]) -> typing.List[typing.Dict]:
        return self._get_paginated_content(
            endpoint="campaign/get/",
            params={
                "advertiser_id": advertiser_id,
                "fields": json.dumps(fields),
            },
        )

    def get_advertiser_adgroups(self, advertiser_id: str, fields: typing.List[str]) -> typing.List[typing.Dict]:
        return self._get_paginated_content(
            endpoint="adgroup/get/",
            params={
                "advertiser_id": advertiser_id,
                "fields": json.dumps(fields),
            },
        )

    def get_advertiser_ads(self, advertiser_id: str, fields: typing.List[str]) -> typing.List[typing.Dict]:
        return self._get_paginated_content(
            endpoint="ad/get/",
            params={
                "advertiser_id": advertiser_id,
                "fields": json.dumps(fields),
            },
        )

    def create_ads(self, ad_params: typing.Dict) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint="ad/create",
                method=enums.HttpMethod.POST,
                params=ad_params,
            )
        )["data"]

    def update_ads(self, ad_params: typing.Dict) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint="ad/update",
                method=enums.HttpMethod.POST,
                params=ad_params,
            )
        )["data"]

    def update_ads_status(self, ads_status_params: typing.Dict) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint="ad/status/update",
                method=enums.HttpMethod.POST,
                params=ads_status_params,
            )
        )["data"]

    def create_campaign(self, campaign_params: typing.Dict) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint="campaign/create",
                method=enums.HttpMethod.POST,
                params=campaign_params,
            )
        )["data"]

    def update_campaign(self, campaign_params: typing.Dict) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint="campaign/update",
                method=enums.HttpMethod.POST,
                params=campaign_params,
            )
        )["data"]

    def create_adgroup(self, adgroup_params: typing.Dict) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint="adgroup/create",
                method=enums.HttpMethod.POST,
                params=adgroup_params,
            )
        )["data"]

    def update_adgroup(self, adgroup_params: typing.Dict) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint="adgroup/update",
                method=enums.HttpMethod.POST,
                params=adgroup_params,
            )
        )["data"]

    def upload_image(self, image_params: typing.Dict) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint="file/image/ad/upload",
                method=enums.HttpMethod.POST,
                params=image_params,
            )
        )["data"]

    def update_image_name(self, image_params: typing.Dict) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint="file/image/ad/update",
                method=enums.HttpMethod.POST,
                params=image_params,
            )
        )["data"]

    def get_images_info(self, image_params: typing.Dict) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint="file/image/ad/info",
                method=enums.HttpMethod.GET,
                params=image_params,
            )
        )["data"]["list"]

    def upload_video(self, video_params: typing.Dict) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint="file/video/ad/upload",
                method=enums.HttpMethod.POST,
                params=video_params,
            )
        )["data"]

    def update_video_name(self, video_params: typing.Dict) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint="file/video/ad/update",
                method=enums.HttpMethod.POST,
                params=video_params,
            )
        )["data"]

    def get_videos_info(self, video_params: typing.Dict) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint="file/video/ad/info",
                method=enums.HttpMethod.GET,
                params=video_params,
            )
        )["data"]["list"]

    def get_insights_report(
        self,
        advertiser_id: str,
        service_type: str,
        report_type: str,
        data_level: str,
        dimensions: typing.List[str],
        metrics: typing.List[str],
        from_datetime: datetime.datetime,
        to_datetime: datetime.datetime,
    ) -> typing.List[typing.Dict]:
        return self._get_paginated_content(
            endpoint="report/integrated/get",
            params={
                "advertiser_id": advertiser_id,
                "service_type": service_type,
                "report_type": report_type,
                "data_level": data_level,
                "dimensions": json.dumps(dimensions),
                "metrics": json.dumps(metrics),
                "start_date": utils.format_tiktok_date(from_datetime),
                "end_date": utils.format_tiktok_date(to_datetime),
            },
        )

    def _get_paginated_content(
        self,
        endpoint: str,
        params: typing.Optional[typing.Dict] = None,
        page_size: typing.Optional[int] = None,
    ) -> typing.List[typing.Dict]:
        params = params if params else {}
        params["page_size"] = self.LIMIT if not page_size else page_size
        all_data = []

        while True:
            data = self._get_content(
                response=self._request(
                    endpoint=endpoint,
                    method=enums.HttpMethod.GET,
                    params=params,
                )
            )["data"]
            all_data.extend(data.get("list", []))

            page_number = data["page_info"]["page"]
            if page_number >= data["page_info"]["total_page"]:
                break

            page_number += 1
            params["page"] = page_number

        return all_data

    def _request(
        self,
        endpoint: str,
        method: enums.HttpMethod,
        params: typing.Optional[typing.Dict] = None,
        payload: typing.Optional[typing.Dict] = None,
    ) -> requests.Response:
        full_endpoint = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(
                url=full_endpoint,
                method=method.value,
                params=params,
                headers={
                    "Access-Token": self._user_access_token,
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                },
                data=payload,
            )
            if response.status_code not in self.VALID_STATUS_CODES:
                raise tiktok_api_exceptions.BadResponseCodeError(
                    message="Invalid API client response (status_code={}, data={})".format(
                        response.status_code,
                        response.content.decode(encoding="utf-8"),
                    ),
                    code=response.status_code,
                )
        except requests.exceptions.ConnectTimeout as e:
            raise tiktok_api_exceptions.TikTokAPIClientError(
                "Connection timeout. Error: {}".format(utils.get_exception_message(exception=e))
            )
        except requests.RequestException as e:
            raise tiktok_api_exceptions.TikTokAPIClientError(
                "Request exception. Error: {}".format(utils.get_exception_message(exception=e))
            )

        return self._validate_response(response=response)

    @staticmethod
    def _validate_response(response: requests.Response) -> requests.Response:
        """
        As per this reference page: https://ads.tiktok.com/marketing_api/docs?id=1737172488964097
        The payload can contain their own status
        """
        payload_status_code = TikTokApiClient._get_content(response=response)["code"]
        if payload_status_code not in TikTokApiClient.VALID_PAYLOAD_STATUS_CODES:
            raise tiktok_api_exceptions.BadPayloadCodeError(
                message="Invalid API client response (status_code={}, payload_status_code={}, data={})".format(
                    response.status_code,
                    payload_status_code,
                    response.content.decode(encoding="utf-8"),
                ),
                code=response.status_code,
                payload_code=payload_status_code,
            )

        return response

    @staticmethod
    def _get_content(response: requests.Response) -> typing.Dict:
        return json.loads(response.content)
