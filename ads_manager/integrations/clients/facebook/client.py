import datetime
import json
import logging
import time
import typing

from ads_manager import enums, utils
from ads_manager.integrations.clients import base_client
from ads_manager.integrations.clients import exceptions as client_exceptions
from ads_manager.integrations.clients import messages
from ads_manager.integrations.clients.facebook import (
    constants as facebook_client_constants,
)
from ads_manager.integrations.clients.facebook import schemas as facebook_client_schemas
from ads_manager.integrations.gateways.facebook import client as facebook_api_client
from ads_manager.integrations.gateways.facebook import (
    exceptions as facebook_api_client_exceptions,
)

# TODO: Remove this. Used only for testing/debugging

logger = logging.getLogger(__name__)


class FacebookClient(base_client.BaseClient):
    def __init__(self, user_access_token: str, params: typing.Optional[typing.Dict] = None) -> None:
        super().__init__(user_access_token=user_access_token, params=params)

    def get_rest_api_client(self) -> facebook_api_client.FacebookApiClient:
        if not self._rest_api_client:
            self._rest_api_client = facebook_api_client.FacebookApiClient(user_access_token=self._user_access_token)

        return self._rest_api_client

    def get_account_ids(
        self,
    ) -> typing.List[messages.AdAccount]:
        try:
            response = self.get_rest_api_client().get_accounts()
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to fetch account ids (platform={}). Error: {}".format(
                    enums.Platform.FACEBOOK.name, utils.get_exception_message(exception=e)
                )
            )

        validated_data = utils.validate_marshmallow_schema(data=response, schema=facebook_client_schemas.AdAccounts())
        if not validated_data:
            raise client_exceptions.ResponseDataNotValidError(
                "Account data fetched (platform={}, response_data={}) is not valid".format(
                    enums.Platform.FACEBOOK.name, response
                )
            )

        message_to_return = [
            messages.AdAccount(id_token=data["account_id"], account_id=data["id"], account_name=None)
            for data in validated_data["ad_accounts"]
        ]

        # return [data["id"] for data in validated_data["ad_accounts"]]
        return message_to_return

    def get_account_campaigns_details(self, ad_account_id: str) -> typing.List[messages.CampaignDetails]:
        try:
            response = self.get_rest_api_client().get_account_campaigns(
                ad_account=ad_account_id,
                fields=self._get_resource_details_fields(resource_type=enums.ResourceType.CAMPAIGN),
            )
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to fetch campaign details (platform={}, ad_account_id={}) through provider. Error: {}".format(
                    enums.Platform.FACEBOOK.name,
                    ad_account_id,
                    utils.get_exception_message(exception=e),
                )
            )

        validated_data = utils.validate_marshmallow_schema(
            data=response, schema=facebook_client_schemas.CampaignsDetails()
        )
        if not validated_data:
            raise client_exceptions.ResponseDataNotValidError(
                "Campaign details data fetched (platform={}, ad_account_id={}, response_data={}) is not valid".format(
                    enums.Platform.FACEBOOK.name, ad_account_id, response
                )
            )

        message_to_return = [
            messages.CampaignDetails(
                account_id=data["account_id"],
                campaign_id=data["id"],
                campaign_name=data["name"],
                effective_status=data["effective_status"],
                configured_status=data["configured_status"],
                created_time=data["created_time"],
                updated_time=data["updated_time"],
            )
            for data in validated_data["campaigns_details"]
        ]

        return message_to_return

    def get_account_adsets_details(self, ad_account_id: str) -> typing.List[messages.AdSetDetails]:
        try:
            response = self.get_rest_api_client().get_account_adsets(
                ad_account=ad_account_id,
                fields=self._get_resource_details_fields(resource_type=enums.ResourceType.AD_SET),
            )
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to fetch adset details (platform={}, ad_account_id={}) through provider. Error: {}".format(
                    enums.Platform.FACEBOOK.name,
                    ad_account_id,
                    utils.get_exception_message(exception=e),
                )
            )

        validated_data = utils.validate_marshmallow_schema(
            data=response, schema=facebook_client_schemas.AdSetsDetails()
        )
        if not validated_data:
            raise client_exceptions.ResponseDataNotValidError(
                "Adset details data (platform={}, ad_account_id={}, response_data={}) is not valid".format(
                    enums.Platform.FACEBOOK.name, ad_account_id, response
                )
            )

        message_to_return = [
            messages.AdSetDetails(
                account_id=data["account_id"],
                campaign_id=data["campaign_id"],
                adset_id=data["id"],
                adset_name=data["name"],
                effective_status=data["effective_status"],
                configured_status=data["configured_status"],
                created_time=data["created_time"],
                updated_time=data["updated_time"],
            )
            for data in validated_data["adsets_details"]
        ]

        return message_to_return

    def get_account_ads_details(self, ad_account_id: str) -> typing.List[messages.AdDetails]:
        try:
            response = self.get_rest_api_client().get_account_ads(
                ad_account=ad_account_id,
                fields=self._get_resource_details_fields(resource_type=enums.ResourceType.AD),
            )
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to fetch ad details (platform={}, ad_account_id={}) through provider. Error: {}".format(
                    enums.Platform.FACEBOOK.name,
                    ad_account_id,
                    utils.get_exception_message(exception=e),
                )
            )

        validated_data = utils.validate_marshmallow_schema(data=response, schema=facebook_client_schemas.AdsDetails())
        if not validated_data:
            raise client_exceptions.ResponseDataNotValidError(
                "Ad details data (platform={}, ad_account_id={}, response_data={}) is not valid".format(
                    enums.Platform.FACEBOOK.name, ad_account_id, response
                )
            )

        message_to_return = [
            messages.AdDetails(
                account_id=data["account_id"],
                campaign_id=data["campaign_id"],
                adset_id=data["ad_id"],
                ad_id=data["id"],
                ad_name=data["name"],
                effective_status=data["effective_status"],
                configured_status=data["configured_status"],
                created_time=data["created_time"],
                updated_time=data["updated_time"],
            )
            for data in validated_data["ads_details"]
        ]

        return message_to_return

    def get_account_ad_creatives(self, ad_account_id: str) -> typing.List[messages.AdCreativeDetails]:
        try:
            response = self.get_rest_api_client().get_account_adcreatives(
                ad_account=ad_account_id,
                fields=self._get_resource_details_fields(resource_type=enums.ResourceType.AD_CREATIVE),
            )
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to fetch ad creative details (platform={}, ad_account_id={}) through provider. Error: {}".format(
                    enums.Platform.FACEBOOK.name,
                    ad_account_id,
                    utils.get_exception_message(exception=e),
                )
            )

        validated_data = utils.validate_marshmallow_schema(
            data=response, schema=facebook_client_schemas.AdCreativesDetails()
        )
        if not validated_data:
            raise client_exceptions.ResponseDataNotValidError(
                "Ad creatives data (platform={}, ad_account_id={}, response_data={}) is not valid".format(
                    enums.Platform.FACEBOOK.name, ad_account_id, response
                )
            )

        message_to_return = [
            messages.AdCreativeDetails(
                account_id=data["account_id"],
                creative_id=data["id"],
                creative_name=data.get("name", None),
                title=data.get("title", None),
                body=data.get("body", None),
                image_url=data.get("image_url", None),
            )
            for data in validated_data["adcreatives_details"]
        ]

        return message_to_return

    def get_ad_creative(self, ad_creative_id: str) -> messages.AdCreativeDetails:
        try:
            response = self.get_rest_api_client().get_resource_details(
                resource_id=ad_creative_id,
                fields=self._get_resource_details_fields(resource_type=enums.ResourceType.AD_CREATIVE),
            )
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to fetch ad creative details (platform={}, ad_creative_id={}) through provider. Error: {}".format(
                    enums.Platform.FACEBOOK,
                    ad_creative_id,
                    utils.get_exception_message(exception=e),
                )
            )

        validated_data = utils.validate_marshmallow_schema(
            data=response, schema=facebook_client_schemas.AdCreativeDetails()
        )
        if not validated_data:
            raise client_exceptions.ResponseDataNotValidError(
                "Ad creative data (platform={}, ad_creative_id={}, response_data={}) is not valid".format(
                    enums.Platform.FACEBOOK.name, ad_creative_id, response
                )
            )

        message_to_return = messages.AdCreativeDetails(
            account_id=validated_data["account_id"],
            creative_id=validated_data["id"],
            creative_name=validated_data.get("name", None),
            title=validated_data.get("title", None),
            body=validated_data.get("body", None),
            image_url=validated_data.get("image_url", None),
        )

        return message_to_return

    def get_insights(
        self,
        ad_account_id: str,
        resource_type: enums.ResourceType,
        from_datetime: datetime.datetime,
        to_datetime: datetime.datetime,
    ) -> typing.List[messages.ResourceInsightsReport]:
        try:
            report = self.get_rest_api_client().create_insights_report(
                ad_account=ad_account_id,
                level=resource_type.value,
                fields=self._get_resource_insights_fields(resource_type=resource_type),
                time_increment=enums.TimeIncrement.DAY.value,
                from_datetime=from_datetime,
                to_datetime=to_datetime,
            )
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to create insights report job (platform={}, ad_account_id={}, resource_type={}, from_datetime={}, to_datetime={}) through provider. Error: {}".format(
                    enums.Platform.FACEBOOK.name,
                    ad_account_id,
                    resource_type.name,
                    from_datetime,
                    to_datetime,
                    utils.get_exception_message(exception=e),
                )
            )

        logger.info("Created report (data={})".format(report))

        report_id = report.get("report_run_id")
        if not report_id:
            raise client_exceptions.ResponseDataNotValidError(
                "Report job id is not received from provider (platform={}, response_data={})".format(
                    enums.Platform.FACEBOOK.name, report_id
                )
            )

        while True:
            report_status = self.get_rest_api_client().get_insights_report_status(report_id=report_id)
            report_status_validated_data = utils.validate_marshmallow_schema(
                data=report_status, schema=facebook_client_schemas.ReportStatus()
            )
            if not report_status_validated_data:
                raise client_exceptions.ResponseDataNotValidError(
                    "Report status data (platform={}, report_id={}, response_data={}) is not valid".format(
                        enums.Platform.FACEBOOK.name, report_id, report_status
                    )
                )

            if (
                not report_status_validated_data["is_running"]
                and report_status_validated_data["async_percent_completion"] == 100
            ):
                break

            logger.warning("Waiting for report {}: {}".format(report_id, json.dumps(report_status)))
            time.sleep(5)

        logger.warning("Report {} for account {} is ready".format(report_id, ad_account_id))

        try:
            report_results = self.get_rest_api_client().get_insights_report_results(report_id=report_id)
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to get insights report results (platform={}, ad_account_id={}, resource_type={}, from_datetime={}, to_datetime={}) through provider. Error: {}".format(
                    enums.Platform.FACEBOOK.name,
                    ad_account_id,
                    resource_type.name,
                    from_datetime,
                    to_datetime,
                    utils.get_exception_message(exception=e),
                )
            )

        validated_report_results = utils.validate_marshmallow_schema(
            data=report_results,
            schema=facebook_client_constants.FACEBOOK_INSIGHTS_SCHEMAS[resource_type](),
        )
        if not validated_report_results:
            raise client_exceptions.ResponseDataNotValidError(
                "Insights report data obtained from provider is not valid (platform={}, report_id={}, resource_type={})".format(
                    enums.Platform.FACEBOOK.name, report_id, resource_type.name
                )
            )

        message_to_return = [
            messages.ResourceInsightsReport(
                account_id=data["account_id"],
                account_name=data["account_name"],
                resource_type=resource_type.name,
                campaign_id=data["campaign_id"],
                campaign_name=data["campaign_name"],
                adset_id=data.get("adset_id", None),
                adset_name=data.get("adset_name", None),
                ad_id=data.get("ad_id", None),
                ad_name=data.get("ad_name", None),
                spend="{}".format(data["spend"]),
                impressions=data["impressions"],
                clicks=data["clicks"],
                ctr="{}".format(data["ctr"]) if data["ctr"] is not None else None,
                cpm="{}".format(data["cpm"]) if data["cpm"] is not None else None,
                cpc="{}".format(data["cpc"]) if data["cpc"] is not None else None,
                reach=data["reach"],
                actions=data["actions"],
                conversions=data["conversions"],
                cost_per_conversion=data["cost_per_conversion"],
                conversion_rate=[
                    {
                        "action_type": conversion["action_type"],
                        "value": (float(conversion["value"]) / float(data["clicks"])) * 100,
                    }
                    for conversion in data["conversions"]
                ],
                date_start=data["date_start"],
                date_stop=data["date_stop"],
            )
            for data in validated_report_results["insights"]
        ]

        return message_to_return

    def create_campaign(
        self,
        ad_account_id: str,
        campaign_details: typing.Dict,
    ) -> str:
        validated_campaign_details = utils.validate_marshmallow_schema(
            data=campaign_details, schema=facebook_client_schemas.Campaign()
        )

        if not validated_campaign_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate campaign details (platform={}, campaign_details={})".format(
                    enums.Platform.FACEBOOK.name,
                    campaign_details,
                )
            )

        try:
            created_campaign = self.get_rest_api_client().create_campaign(
                ad_account=ad_account_id, params=validated_campaign_details
            )
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to create campaign (platform={}, ad_account_id={}, campaign_details={}). Error: {}".format(
                    enums.Platform.FACEBOOK.name,
                    ad_account_id,
                    campaign_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return created_campaign["id"]

    def update_campaign(
        self,
        ad_account_id: str,
        campaign_id: str,
        campaign_details: typing.Dict,
    ) -> bool:
        try:
            updated_campaign = self.get_rest_api_client().update_campaign(
                campaign_id=campaign_id, params=campaign_details
            )
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to update campaign (platform={}, campaign_id={}, campaign_details={}). Error: {}".format(
                    enums.Platform.FACEBOOK.name,
                    campaign_id,
                    campaign_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return updated_campaign["success"]

    def create_adset(
        self,
        ad_account_id: str,
        adset_details: typing.Dict,
    ) -> str:
        validated_adset_details = utils.validate_marshmallow_schema(
            data=adset_details, schema=facebook_client_schemas.AdSet()
        )

        if not validated_adset_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate adset details from provider (platform={}, adset_details={})".format(
                    enums.Platform.FACEBOOK.name,
                    adset_details,
                )
            )

        try:
            created_adset = self.get_rest_api_client().create_adset(
                ad_account_id=ad_account_id, params=validated_adset_details
            )
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to create adset (platform={}, ad_account_id={}, adset_details={}). Error: {}".format(
                    enums.Platform.FACEBOOK.name,
                    ad_account_id,
                    adset_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return created_adset["id"]

    def update_adset(
        self,
        ad_account_id: str,
        adset_id: str,
        adset_details: typing.Dict,
    ) -> bool:
        try:
            updated_adset = self.get_rest_api_client().update_adset(adset_id=adset_id, params=adset_details)
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to update adset (platform={}, adset_id={}, adset_details={}). Error: {}".format(
                    enums.Platform.FACEBOOK.name,
                    adset_id,
                    adset_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return updated_adset["success"]

    def create_adcreative(
        self,
        ad_account_id: str,
        adcreative_details: typing.Dict,
    ) -> str:
        validated_adcreative_details = utils.validate_marshmallow_schema(
            data=adcreative_details, schema=facebook_client_schemas.AdCreative()
        )

        if not validated_adcreative_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate adcreative details (platform={}, adcreative_details={})".format(
                    enums.Platform.FACEBOOK.name,
                    adcreative_details,
                )
            )

        try:
            created_adcreative = self.get_rest_api_client().create_adcreative(
                ad_account_id=ad_account_id, params=validated_adcreative_details
            )
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to create adcreative (platform={}, ad_account_id={}, adcreative_details={}). Error: {}".format(
                    enums.Platform.FACEBOOK.name,
                    ad_account_id,
                    adcreative_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return created_adcreative["id"]

    def update_adcreative(
        self,
        adcreative_id: str,
        adcreative_details: typing.Dict,
    ) -> bool:
        try:
            updated_adcreative = self.get_rest_api_client().update_adcreative(
                adcreative_id=adcreative_id, params=adcreative_details
            )
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to update adcreative (platform={}, adcreative_id={}, adcreative_details={}). Error: {}".format(
                    enums.Platform.FACEBOOK.name,
                    adcreative_id,
                    adcreative_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return updated_adcreative["success"]

    def create_ad(
        self,
        ad_account_id: str,
        ad_details: typing.Dict,
    ) -> str:
        validated_ad_details = utils.validate_marshmallow_schema(data=ad_details, schema=facebook_client_schemas.Ad())

        if not validated_ad_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate ad details (platform={}, ad_details={})".format(
                    enums.Platform.FACEBOOK.name,
                    ad_details,
                )
            )

        try:
            created_ad = self.get_rest_api_client().create_ad(ad_account_id=ad_account_id, params=validated_ad_details)
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to create ad (platform={}, ad_account_id={}, ad_details={}). Error: {}".format(
                    enums.Platform.FACEBOOK.name,
                    ad_account_id,
                    ad_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return created_ad["id"]

    def create_ads(self, ad_account_id: str, ads_details: typing.Dict) -> typing.List[str]:
        created_ad_ids = []

        for ad_details in ads_details:
            created_ad_ids.append(self.create_ad(ad_account_id=ad_account_id, ad_details=ad_details))

        return created_ad_ids

    def update_ad(
        self,
        ad_id: str,
        ad_details: typing.Dict,
    ) -> bool:
        try:
            updated_ad = self.get_rest_api_client().update_ad(ad_id=ad_id, params=ad_details)
        except facebook_api_client_exceptions.FacebookAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to update ad (platform={}, ad_id={}, ad_details={}). Error: {}".format(
                    enums.Platform.FACEBOOK.name,
                    ad_id,
                    ad_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return updated_ad["success"]

    @staticmethod
    def _get_resource_details_fields(resource_type: enums.ResourceType) -> str:
        return ",".join(facebook_client_constants.FACEBOOK_RESOURCE_DETAILS_FIELDS[resource_type])

    @staticmethod
    def _get_resource_insights_fields(resource_type: enums.ResourceType) -> str:
        return ",".join(facebook_client_constants.FACEBOOK_INSIGHTS_DETAILS_FIELDS[resource_type])
