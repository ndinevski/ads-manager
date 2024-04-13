import abc
import datetime
import typing

from ads_manager import enums
from ads_manager.integrations.clients import messages
from ads_manager.integrations.gateways.facebook import client as facebook_api_client
from ads_manager.integrations.gateways.tiktok import client as tiktok_api_client


class BaseClient(object):
    @abc.abstractmethod
    def __init__(self, user_access_token: str, params: typing.Optional[typing.Dict] = None) -> None:
        self._user_access_token = user_access_token
        self._rest_api_client = None
        self._params = params

    @property
    @abc.abstractmethod
    def get_rest_api_client(
        self,
    ) -> typing.Union[facebook_api_client.FacebookApiClient, tiktok_api_client.TikTokApiClient]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_account_ids(
        self,
    ) -> typing.List[messages.AdAccount]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_account_campaigns_details(self, ad_account_id: str) -> typing.List[messages.CampaignDetails]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_account_adsets_details(self, ad_account_id: str) -> typing.List[messages.AdSetDetails]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_account_ads_details(self, ad_account_id: str) -> typing.List[messages.AdDetails]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_account_ad_creatives(self, ad_account_id: str) -> typing.List[messages.AdCreativeDetails]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_ad_creative(self, ad_creative_id: str) -> messages.AdCreativeDetails:
        raise NotImplementedError

    @abc.abstractmethod
    def get_insights(
        self,
        ad_account_id: str,
        resource_type: enums.ResourceType,
        from_datetime: datetime.datetime,
        to_datetime: datetime.datetime,
    ) -> typing.List[messages.ResourceInsightsReport]:
        raise NotImplementedError

    @abc.abstractmethod
    def create_campaign(self, ad_account_id: str, campaign_details: typing.Dict) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def update_campaign(
        self,
        ad_account_id,
        campaign_id: str,
        campaign_details: typing.Dict,
    ) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def create_adset(self, ad_account_id: str, adset_details: typing.Dict) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def update_adset(
        self,
        ad_account_id: str,
        adset_id: str,
        adset_details: typing.Dict,
    ) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def create_adcreative(self, ad_account_id: str, adcreative_details: typing.Dict) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def update_adcreative(self, adcreative_id: str, adcreative_details: typing.Dict) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def create_ad(
        self,
        ad_account_id: str,
        ad_details: typing.Dict,
    ) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def create_ads(
        self,
        ad_account_id: str,
        ads_details: typing.Dict,
    ) -> typing.List[str]:
        raise NotImplementedError

    @abc.abstractmethod
    def update_ad(
        self,
        ad_id: str,
        ad_details: typing.Dict,
    ) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def update_ads(self, ad_account_id: str, adgroup_id: str, ad_details: typing.Dict) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def update_ads_status(self, ad_account_id: str, ads_status_details: typing.Dict) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def create_image(self, ad_account_id: str, image_details: typing.Dict) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def update_image_name(self, ad_account_id: str, image_id: str, image_name: str) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def get_images_info(self, ad_account_id: str, image_ids: typing.List[str]) -> typing.List[messages.ImageDetails]:
        raise NotImplementedError

    @abc.abstractmethod
    def create_video(self, ad_account_id: str, video_details: typing.Dict) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def update_video_name(self, ad_account_id: str, video_id: str, video_name: str) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def get_videos_info(self, ad_account_id: str, video_ids: typing.List[str]) -> typing.List[messages.VideoDetails]:
        raise NotImplementedError
