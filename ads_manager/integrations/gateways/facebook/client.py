import datetime
import json
import typing

import requests

from ads_manager import enums, utils
from ads_manager.integrations.gateways.facebook import (
    constants as facebook_api_constants,
)
from ads_manager.integrations.gateways.facebook import (
    exceptions as facebook_api_exceptions,
)


class FacebookApiClient:
    BASE_URL = "https://graph.facebook.com/v18.0"
    VALID_STATUS_CODES = [200]
    LIMIT = 100

    def __init__(self, user_access_token: str) -> None:
        self._user_access_token = user_access_token

    def get_accounts(self) -> typing.List[typing.Dict]:
        return self._get_paginated_content(endpoint="me/adaccounts")

    def get_resource_details(
        self,
        resource_id: str,
        fields: str,
    ) -> typing.Dict:
        return self._get_content(
            response=self._request(
                method=enums.HttpMethod.GET,
                endpoint=resource_id,
                params={
                    "fields": fields,
                },
            )
        )

    def create_insights_report(
        self,
        ad_account: str,
        level: str,
        fields: str,
        time_increment: int,
        from_datetime: datetime.datetime,
        to_datetime: datetime.datetime,
    ) -> typing.Dict:
        params = {
            "level": level,
            "fields": fields,
            "time_increment": time_increment,
            "time_range": self._get_time_range(
                from_datetime=from_datetime,
                to_datetime=to_datetime,
            ),
        }

        return self._get_content(
            response=self._request(
                endpoint=f"{ad_account}/insights",
                method=enums.HttpMethod.POST,
                params=params,
            )
        )

    def get_insights_report_status(self, report_id: str) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint=report_id,
                method=enums.HttpMethod.GET,
            )
        )

    def get_insights_report_results(self, report_id: str) -> typing.List[typing.Dict]:
        return self._get_paginated_content(endpoint=f"{report_id}/insights")

    def get_account_campaigns(
        self,
        ad_account: str,
        fields: str,
    ) -> typing.List[typing.Dict]:
        return self._get_paginated_content(endpoint=f"{ad_account}/campaigns", params={"fields": fields})

    def get_account_adsets(
        self,
        ad_account: str,
        fields: str,
    ) -> typing.List[typing.Dict]:
        return self._get_paginated_content(endpoint=f"{ad_account}/adsets", params={"fields": fields})

    def get_account_ads(
        self,
        ad_account: str,
        fields: str,
    ) -> typing.List[typing.Dict]:
        return self._get_paginated_content(endpoint=f"{ad_account}/ads", params={"fields": fields})

    def get_account_adcreatives(
        self,
        ad_account: str,
        fields: str,
    ) -> typing.List[typing.Dict]:
        return self._get_paginated_content(endpoint=f"{ad_account}/adcreatives", params={"fields": fields})

    def create_campaign(
        self,
        ad_account: str,
        params: typing.Dict,
    ) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint=f"{ad_account}/campaigns",
                method=enums.HttpMethod.POST,
                params=params,
            )
        )

    def update_campaign(
        self,
        campaign_id: str,
        params: typing.Dict,
    ) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint=campaign_id,
                method=enums.HttpMethod.POST,
                params=params,
            )
        )

    def create_adset(
        self,
        ad_account_id: str,
        params: typing.Dict,
    ) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint=f"{ad_account_id}/adsets",
                method=enums.HttpMethod.POST,
                params=params,
            )
        )

    def update_adset(
        self,
        adset_id: str,
        params: typing.Dict,
    ) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint=adset_id,
                method=enums.HttpMethod.POST,
                params=params,
            )
        )

    def create_adcreative(
        self,
        ad_account_id: str,
        params: typing.Dict,
    ) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint=f"{ad_account_id}/adcreatives",
                method=enums.HttpMethod.POST,
                params=params,
            )
        )

    def update_adcreative(
        self,
        adcreative_id: str,
        params: typing.Dict,
    ) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint=adcreative_id,
                method=enums.HttpMethod.POST,
                params=params,
            )
        )

    def create_ad(
        self,
        ad_account_id: str,
        params: typing.Dict,
    ) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint=f"{ad_account_id}/ads",
                method=enums.HttpMethod.POST,
                params=params,
            )
        )

    def update_ad(
        self,
        ad_id: str,
        params: typing.Dict,
    ) -> typing.Dict:
        return self._get_content(
            response=self._request(
                endpoint=ad_id,
                method=enums.HttpMethod.POST,
                params=params,
            )
        )

    def _get_paginated_content(
        self,
        endpoint: str,
        params: typing.Optional[typing.Dict] = None,
    ) -> typing.List[typing.Dict]:
        params = params if params else {}
        all_data = []

        while True:
            data = self._get_content(
                response=self._request(method=enums.HttpMethod.GET, endpoint=endpoint, params=params)
            )
            all_data.extend(data.get("data", []))
            after = data.get("paging", {}).get("cursors", {}).get("after")
            if not after or not data.get("data"):
                break

            params["after"] = after

        return all_data

    def _request(
        self,
        endpoint: str,
        method: enums.HttpMethod,
        params: typing.Optional[typing.Dict] = None,
        payload: typing.Optional[typing.Dict] = None,
    ) -> requests.Response:
        full_endpoint = f"{self.BASE_URL}/{endpoint}"
        try:
            response = requests.request(
                url=full_endpoint,
                method=method.value,
                params=self._construct_request_params(params=params),
                data=payload,
            )
            if response.status_code not in self.VALID_STATUS_CODES:
                raise facebook_api_exceptions.BadResponseCodeError(
                    message="Invalid API client response (status_code={}, data={})".format(
                        response.status_code,
                        response.content.decode(encoding="utf-8"),
                    ),
                    code=response.status_code,
                )
        except requests.exceptions.ConnectTimeout as e:
            raise facebook_api_exceptions.FacebookAPIClientError(
                "Connection timeout. Error: {}".format(utils.get_exception_message(exception=e))
            )
        except requests.RequestException as e:
            raise facebook_api_exceptions.FacebookAPIClientError(
                "Request exception. Error: {}".format(utils.get_exception_message(exception=e))
            )

        return response

    def _construct_request_params(self, params: typing.Optional[typing.Dict]) -> typing.Dict:
        mandatory_params = {
            "access_token": self._user_access_token,
            "limit": self.LIMIT,
        }

        if params:
            mandatory_params.update(params)

        return mandatory_params

    @staticmethod
    def _get_content(response: requests.Response) -> typing.Dict:
        return json.loads(response.content)

    @staticmethod
    def _get_time_range(from_datetime: datetime.datetime, to_datetime: datetime.datetime) -> str:
        return json.dumps(
            {
                "since": datetime.datetime.strftime(from_datetime, facebook_api_constants.FACEBOOK_DATE_FORMAT),
                "until": datetime.datetime.strftime(to_datetime, facebook_api_constants.FACEBOOK_DATE_FORMAT),
            }
        )
