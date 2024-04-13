import datetime
import typing

from ads_manager import enums, utils
from ads_manager.integrations.clients import base_client
from ads_manager.integrations.clients import exceptions as client_exceptions
from ads_manager.integrations.clients import messages
from ads_manager.integrations.clients.tiktok import constants as tiktok_client_constants
from ads_manager.integrations.clients.tiktok import enums as tiktok_client_enums
from ads_manager.integrations.clients.tiktok import schemas as tiktok_client_schemas
from ads_manager.integrations.gateways.tiktok import client as tiktok_api_client
from ads_manager.integrations.gateways.tiktok import (
    exceptions as tiktok_api_client_exceptions,
)


class TiktokClient(base_client.BaseClient):
    def __init__(self, user_access_token: str, params: typing.Optional[typing.Dict] = None) -> None:
        super().__init__(user_access_token=user_access_token, params=params)

    def get_rest_api_client(self) -> tiktok_api_client.TikTokApiClient:
        if not self._rest_api_client:
            self._rest_api_client = tiktok_api_client.TikTokApiClient(
                user_access_token=self._user_access_token, params=self._params
            )
        return self._rest_api_client

    def get_account_ids(
        self,
    ) -> typing.List[messages.AdAccount]:
        utils.validate_params(self._params)

        try:
            response = self.get_rest_api_client().get_ad_accounts(params=self._params)
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to fetch account ids (platform={}, app_id={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    self._params["app_id"],
                    utils.get_exception_message(exception=e),
                )
            )

        validated_data = utils.validate_marshmallow_schema(data=response, schema=tiktok_client_schemas.AdAccounts())
        if not validated_data:
            raise client_exceptions.ResponseDataNotValidError(
                "Account data fetched (platform={}, app_id={}, response_data={}) is not valid".format(
                    enums.Platform.TIKTOK.name, self._params["app_id"], response
                )
            )

        message_to_return = [
            messages.AdAccount(id_token=None, account_id=data["advertiser_id"], account_name=data["advertiser_name"])
            for data in validated_data["ad_accounts"]
        ]

        # return [data["advertiser_id"] for data in validated_data["ad_accounts"]]
        return message_to_return

    def get_account_campaigns_details(self, ad_account_id: str) -> typing.List[messages.CampaignDetails]:
        try:
            response = self.get_rest_api_client().get_advertiser_campaigns(
                advertiser_id=ad_account_id,
                fields=tiktok_client_constants.TIKTOK_RESOURCE_DETAILS_FIELDS[enums.ResourceType.CAMPAIGN],
            )
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to fetch campaign details (platform={}, advertiser_id={}) through provider. Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    utils.get_exception_message(exception=e),
                )
            )

        validated_data = utils.validate_marshmallow_schema(
            data=response, schema=tiktok_client_schemas.CampaignsDetails()
        )
        if not validated_data:
            raise client_exceptions.ResponseDataNotValidError(
                "Campaign details data (platform={}, advertiser_id={}, response_data={}) is not valid".format(
                    enums.Platform.TIKTOK.name, ad_account_id, response
                )
            )

        message_to_return = [
            messages.CampaignDetails(
                account_id=data["account_id"],
                campaign_id=data["id"],
                campaign_name=data["name"],
                effective_status=data["effective_status"],
                configured_status=data.get("configured_status", None),
                created_time=data["created_time"],
                updated_time=data["updated_time"],
            )
            for data in validated_data["campaigns_details"]
        ]

        return message_to_return

    def get_account_adsets_details(self, ad_account_id: str) -> typing.List[messages.AdSetDetails]:
        try:
            response = self.get_rest_api_client().get_advertiser_adgroups(
                advertiser_id=ad_account_id,
                fields=tiktok_client_constants.TIKTOK_RESOURCE_DETAILS_FIELDS[enums.TiktokResourceType.AD_GROUP],
            )
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to fetch adgroup details (platform={}, advertiser_id={}) through provider. Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    utils.get_exception_message(exception=e),
                )
            )

        validated_data = utils.validate_marshmallow_schema(
            data=response, schema=tiktok_client_schemas.AdGroupsDetails()
        )
        if not validated_data:
            raise client_exceptions.ResponseDataNotValidError(
                "Adgroup details data (platform={}, advertiser_id={}, response_data={}) is not valid".format(
                    enums.Platform.TIKTOK.name, ad_account_id, response
                )
            )

        message_to_return = [
            messages.AdSetDetails(
                account_id=data["account_id"],
                campaign_id=data["campaign_id"],
                adset_id=data["id"],
                adset_name=data["name"],
                effective_status=data["effective_status"],
                configured_status=data.get("configured_status", None),
                created_time=data["created_time"],
                updated_time=data["updated_time"],
            )
            for data in validated_data["adgroups_details"]
        ]

        return message_to_return

    def get_account_ads_details(self, ad_account_id: str) -> typing.List[messages.AdDetails]:
        try:
            response = self.get_rest_api_client().get_advertiser_ads(
                advertiser_id=ad_account_id,
                fields=tiktok_client_constants.TIKTOK_RESOURCE_DETAILS_FIELDS[enums.ResourceType.AD],
            )
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to fetch ad details (platform={}, advertiser_id={}) through provider. Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    utils.get_exception_message(exception=e),
                )
            )

        validated_data = utils.validate_marshmallow_schema(data=response, schema=tiktok_client_schemas.AdsDetails())
        if not validated_data:
            raise client_exceptions.ResponseDataNotValidError(
                "Ad details data (platform={}, advertiser_id={}, response_data={}) is not valid".format(
                    enums.Platform.TIKTOK.name, ad_account_id, response
                )
            )

        message_to_return = [
            messages.AdDetails(
                account_id=data["account_id"],
                campaign_id=data["campaign_id"],
                adset_id=data["adgroup_id"],
                ad_id=data["id"],
                ad_name=data["name"],
                effective_status=data["effective_status"],
                configured_status=data.get("configured_status", None),
                created_time=data["created_time"],
                updated_time=data["updated_time"],
            )
            for data in validated_data["ads_details"]
        ]

        return message_to_return

    def create_ads(self, ad_account_id: str, ads_details: typing.Dict) -> typing.List[str]:
        if "adset_id" in ads_details:
            ads_details.update({"adgroup_id": ads_details["adset_id"]})
            del ads_details["adset_id"]

        ads_details["advertiser_id"] = ad_account_id

        validated_ad_details = utils.validate_marshmallow_schema(
            data=ads_details, schema=tiktok_client_schemas.AdCreate()
        )
        if not validated_ad_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate ad details (platform={}, advertiser_id={}, ad_details={})".format(
                    enums.Platform.TIKTOK.name, ad_account_id, ads_details
                )
            )

        try:
            created_ad = self.get_rest_api_client().create_ads(ad_params=validated_ad_details)
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to create ads (platform={}, advertiser_id={}, ad_details={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    validated_ad_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return created_ad["ad_ids"]

    def update_ads(self, ad_account_id: str, adgroup_id: str, ad_details: typing.Dict) -> bool:
        ad_details.update({"advertiser_id": ad_account_id, "adgroup_id": adgroup_id})
        validated_ad_details = utils.validate_marshmallow_schema(
            data=ad_details, schema=tiktok_client_schemas.AdUpdate()
        )
        if not validated_ad_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate ad details (platform={}, advertiser_id={}, adgroup_id={}, ad_details={})".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    adgroup_id,
                    ad_details,
                )
            )

        try:
            updated_ads = self.get_rest_api_client().update_ads(ad_params=validated_ad_details)
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to update ad (platform={}, advertiser_id={}, adgroup_id={}, ad_details={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    adgroup_id,
                    validated_ad_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return bool(updated_ads)

    def update_ads_status(self, ad_account_id: str, ads_status_details: typing.Dict) -> bool:
        ads_status_details["advertiser_id"] = ad_account_id
        validated_ads_status_details = utils.validate_marshmallow_schema(
            data=ads_status_details, schema=tiktok_client_schemas.AdStatusUpdate()
        )
        if not validated_ads_status_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate ads status details (platform={}, advertiser_id={}, ads_status_details={})".format(
                    enums.Platform.TIKTOK.name, ad_account_id, ads_status_details
                )
            )

        try:
            updated_ads = self.get_rest_api_client().update_ads_status(ads_status_params=validated_ads_status_details)
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to update ads status details (platform={}, advertiser_id={}, ads_status_details={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    validated_ads_status_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return bool(updated_ads["ad_ids"])

    def create_campaign(self, ad_account_id: str, campaign_details: typing.Dict) -> str:
        campaign_details["advertiser_id"] = ad_account_id
        validated_campaign_details = utils.validate_marshmallow_schema(
            data=campaign_details, schema=tiktok_client_schemas.CampaignCreate()
        )
        if not validated_campaign_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate campaign details (platform={}, advertiser_id={}, campaign_details={})".format(
                    enums.Platform.TIKTOK.name, ad_account_id, campaign_details
                )
            )

        try:
            created_campaign = self.get_rest_api_client().create_campaign(campaign_params=validated_campaign_details)
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to create campaign (platform={}, advertiser_id={}, campaign_details={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    validated_campaign_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return created_campaign["campaign_id"]

    def update_campaign(
        self,
        ad_account_id: str,
        campaign_id: str,
        campaign_details: typing.Dict,
    ) -> bool:
        campaign_details.update({"advertiser_id": ad_account_id, "campaign_id": campaign_id})
        validated_campaign_details = utils.validate_marshmallow_schema(
            data=campaign_details, schema=tiktok_client_schemas.CampaignUpdate()
        )
        if not validated_campaign_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate campaign details (platform={}, advertiser_id={}, campaign_id={}, campaign_details={})".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    campaign_id,
                    campaign_details,
                )
            )

        try:
            updated_campaign = self.get_rest_api_client().update_campaign(campaign_params=validated_campaign_details)
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to update campaign (platform={}, advertiser_id={}, campaign_id={}, campaign_details={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    campaign_id,
                    validated_campaign_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return bool(updated_campaign)

    def create_adset(self, ad_account_id: str, adset_details: typing.Dict) -> str:
        adset_details["advertiser_id"] = ad_account_id
        validated_adgroup_details = utils.validate_marshmallow_schema(
            data=adset_details, schema=tiktok_client_schemas.AdGroupCreate()
        )
        if not validated_adgroup_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate adgroup details (platform={}, advertiser_id={}, adgroup_details={})".format(
                    enums.Platform.TIKTOK.name, ad_account_id, adset_details
                )
            )

        try:
            created_adgroup = self.get_rest_api_client().create_adgroup(adgroup_params=validated_adgroup_details)
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to create adgroup (platform={}, advertiser_id={}, adgroup_details={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    validated_adgroup_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return created_adgroup["adgroup_id"]

    def update_adset(
        self,
        ad_account_id: str,
        adset_id: str,
        adset_details: typing.Dict,
    ) -> bool:
        adset_details.update({"advertiser_id": ad_account_id, "adgroup_id": adset_id})
        validated_adgroup_details = utils.validate_marshmallow_schema(
            data=adset_details, schema=tiktok_client_schemas.AdGroupUpdate()
        )
        if not validated_adgroup_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate adgroup details (platform={}, advertiser_id={}, adgroup_id={}, adgroup_details={})".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    adset_id,
                    adset_details,
                )
            )

        try:
            updated_adgroup = self.get_rest_api_client().update_adgroup(adgroup_params=validated_adgroup_details)
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to update adgroup (platform={}, advertiser_id={}, adgroup_id={}, adgroup_details={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    adset_id,
                    validated_adgroup_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return bool(updated_adgroup)

    def create_image(self, ad_account_id: str, image_details: typing.Dict) -> str:
        image_details["advertiser_id"] = ad_account_id
        validated_image_details = utils.validate_marshmallow_schema(
            data=image_details, schema=tiktok_client_schemas.ImageCreate()
        )
        if not validated_image_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate image details (platform={}, advertiser_id={}, image_details={})".format(
                    enums.Platform.TIKTOK.name, ad_account_id, image_details
                )
            )

        try:
            created_image = self.get_rest_api_client().upload_image(image_params=validated_image_details)
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to create image (platform={}, advertiser_id={}, image_details={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    validated_image_details,
                    utils.get_exception_message(exception=e),
                )
            )

        return created_image["image_id"]

    def update_image_name(self, ad_account_id: str, image_id: str, image_name: str) -> bool:
        image_details = {
            "advertiser_id": ad_account_id,
            "image_id": image_id,
            "file_name": image_name,
        }

        validated_image_details = utils.validate_marshmallow_schema(
            data=image_details, schema=tiktok_client_schemas.ImageUpdate()
        )
        if not validated_image_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate image details (platform={}, advertiser_id={}, image_id={}, image_name={})".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    image_id,
                    image_name,
                )
            )

        try:
            updated_image = self.get_rest_api_client().update_image_name(image_params=validated_image_details)
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to update image (platform={}, advertiser_id={}, image_id={}, image_name={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    image_id,
                    image_name,
                    utils.get_exception_message(exception=e),
                )
            )

        return bool(updated_image)

    def get_images_info(self, ad_account_id: str, image_ids: typing.List[str]) -> typing.List[messages.ImageDetails]:
        image_params = {
            "advertiser_id": ad_account_id,
            "image_ids": image_ids,
        }

        validated_image_params = utils.validate_marshmallow_schema(
            data=image_params, schema=tiktok_client_schemas.ImageInfoParams()
        )

        if not validated_image_params:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate image details (platform={}, advertiser_id={}, image_ids={})".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    image_ids,
                )
            )

        try:
            images_info_details = self.get_rest_api_client().get_images_info(image_params=validated_image_params)
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to get images info details (platform={}, advertiser_id={}, image_ids={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    image_ids,
                    utils.get_exception_message(exception=e),
                )
            )

        validated_image_details = utils.validate_marshmallow_schema(
            data=images_info_details,
            schema=tiktok_client_schemas.ImageDetailsResponse(),
        )
        if not validated_image_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate image details (platform={}, advertiser_id={}, image_ids={})".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    image_ids,
                )
            )

        message_to_return = [
            messages.ImageDetails(
                image_id=data["image_id"],
                material_id=data["material_id"],
                size=data["size"],
                width=data["width"],
                height=data["height"],
                format=data["format"],
                image_url=data["image_url"],
                signature=data["signature"],
                file_name=data["file_name"],
                create_time=data["create_time"],
                modify_time=data["modify_time"],
                displayable=data["displayable"],
            )
            for data in validated_image_details["image_details"]
        ]

        return message_to_return

    def create_video(self, ad_account_id: str, video_details: typing.Dict) -> str:
        video_details["advertiser_id"] = ad_account_id
        validated_video_params = utils.validate_marshmallow_schema(
            data=video_details, schema=tiktok_client_schemas.VideoCreate()
        )
        if not validated_video_params:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate video details (platform={}, advertiser_id={}, video_details={})".format(
                    enums.Platform.TIKTOK.name, ad_account_id, video_details
                )
            )

        try:
            created_video = self.get_rest_api_client().upload_video(video_params=validated_video_params)
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to create video (platform={}, advertiser_id={}, video_details={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    validated_video_params,
                    utils.get_exception_message(exception=e),
                )
            )

        return created_video[0]["video_id"]

    def update_video_name(self, ad_account_id: str, video_id: str, video_name: str) -> bool:
        video_details = {
            "advertiser_id": ad_account_id,
            "video_id": video_id,
            "file_name": video_name,
        }

        validated_video_params = utils.validate_marshmallow_schema(
            data=video_details, schema=tiktok_client_schemas.VideoUpdate()
        )
        if not validated_video_params:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate video details (platform={}, advertiser_id={}, video_id={}, video_name={})".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    video_id,
                    video_name,
                )
            )

        try:
            updated_video = self.get_rest_api_client().update_video_name(video_params=validated_video_params)
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to update video (platform={}, advertiser_id={}, video_id={}, video_name={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    video_id,
                    video_name,
                    utils.get_exception_message(exception=e),
                )
            )

        return bool(updated_video)

    def get_videos_info(self, ad_account_id: str, video_ids: typing.List[str]) -> typing.List[messages.VideoDetails]:
        video_params = {
            "advertiser_id": ad_account_id,
            "video_ids": video_ids,
        }

        validated_video_params = utils.validate_marshmallow_schema(
            data=video_params, schema=tiktok_client_schemas.VideoInfoParams()
        )
        if not validated_video_params:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate video info params (platform={}, advertiser_id={}, video_ids={})".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    video_ids,
                )
            )

        try:
            video_details = self.get_rest_api_client().get_videos_info(video_params=validated_video_params)
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to get video details (platform={}, advertiser_id={}, video_ids={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    video_ids,
                    utils.get_exception_message(exception=e),
                )
            )

        validated_video_details = utils.validate_marshmallow_schema(
            data=video_details, schema=tiktok_client_schemas.VideoDetailsResponse()
        )
        if not validated_video_details:
            raise client_exceptions.ResponseDataNotValidError(
                "Failed to validate video details (platform={}, advertiser_id={}, video_ids={})".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    video_ids,
                )
            )

        message_to_return = [
            messages.VideoDetails(
                video_id=data["image_id"],
                material_id=data["material_id"],
                duration=data["duration"],
                bit_rate=data["bit_rate"],
                size=data["size"],
                width=data["width"],
                height=data["height"],
                format=data["format"],
                video_cover_url=data["video_cover_url"],
                preview_url=data["preview_url"],
                preview_url_expire_time=data["preview_url_expire_time"],
                signature=data["signature"],
                file_name=data["file_name"],
                create_time=data["create_time"],
                modify_time=data["modify_time"],
                displayable=data["displayable"],
                allow_download=data["allow_download"],
                allowed_placements=data["allowed_placements"],
            )
            for data in validated_video_details["video_details"]
        ]

        return message_to_return

    def get_insights(
        self,
        ad_account_id: str,
        resource_type: typing.Union[enums.ResourceType, enums.TiktokResourceType],
        from_datetime: datetime.datetime,
        to_datetime: datetime.datetime,
    ) -> typing.List[messages.ResourceInsightsReport]:
        if resource_type == enums.ResourceType.AD_SET:
            resource_type = enums.TiktokResourceType.AD_GROUP

        try:
            insights_report = self.get_rest_api_client().get_insights_report(
                advertiser_id=ad_account_id,
                service_type=tiktok_client_enums.ServiceType.AUCTION.value,
                report_type=tiktok_client_enums.ReportType.BASIC.value,
                data_level=tiktok_client_enums.DataLevel.from_service_and_resource_type(
                    service_type=tiktok_client_enums.ServiceType.AUCTION,
                    resource_type=resource_type,
                ).value,
                dimensions=tiktok_client_constants.TIKTOK_INSIGHTS_DETAILS_FIELDS[resource_type]["dimensions"],
                metrics=tiktok_client_constants.TIKTOK_INSIGHTS_DETAILS_FIELDS[resource_type]["metrics"],
                from_datetime=from_datetime,
                to_datetime=to_datetime,
            )
        except tiktok_api_client_exceptions.TikTokAPIClientError as e:
            raise client_exceptions.ClientProviderError(
                "Unable to get insights report (platform={}, advertiser_id={}, resource_type={}, from_datetime={}, to_datetime={}). Error: {}".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    resource_type.name,
                    from_datetime,
                    to_datetime,
                    utils.get_exception_message(exception=e),
                )
            )

        validated_insights_report = utils.validate_marshmallow_schema(
            data=insights_report,
            schema=tiktok_client_constants.TIKTOK_INSIGHTS_SCHEMAS[resource_type](advertiser_id=ad_account_id),
        )
        if not validated_insights_report:
            raise client_exceptions.ResponseDataNotValidError(
                "Resource insights data fetched from provider (platform={}, advertiser_id={}, resource_type={}, from_datetime={}, to_datetime={}, insights_report={}) is not valid".format(
                    enums.Platform.TIKTOK.name,
                    ad_account_id,
                    resource_type.name,
                    from_datetime,
                    to_datetime,
                    insights_report,
                )
            )

        message_to_return = [
            messages.ResourceInsightsReport(
                account_id=data["advertiser_id"],
                account_name=None,
                resource_type=resource_type.name,
                campaign_id=data["campaign_id"],
                campaign_name=data["campaign_name"],
                adset_id=data.get("adgroup_id", None),
                adset_name=data.get("adgroup_name", None),
                ad_id=data.get("ad_id", None),
                ad_name=data.get("ad_name", None),
                spend="{}".format(data["spend"]),
                impressions=data["impressions"],
                clicks=data["clicks"],
                ctr="{}".format(data["ctr"]),
                cpm="{}".format(data["cpm"]),
                cpc="{}".format(data["cpc"]),
                reach=data["reach"],
                actions=None,
                conversions=[{"action_type": "conversion", "value": data["conversions"]}],
                cost_per_conversion=[{"action_type": "conversion", "value": data["cost_per_conversion"]}],
                conversion_rate=[{"action_type": "conversion", "value": data["conversion_rate"]}],
                date_start=data["start_date"],
                date_stop=data["end_date"],
            )
            for data in validated_insights_report["resource_insights"]
        ]

        return message_to_return
