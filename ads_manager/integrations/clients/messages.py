import dataclasses
import typing


@dataclasses.dataclass
class AdAccount(object):
    id_token: typing.Optional[
        str
    ]  # FB token with structure: AdAccount ID (https://developers.facebook.com/docs/marketing-api/reference/business/adaccount/)
    account_id: str  # FB numeric string | TT Authorising Advertiser ID
    account_name: typing.Optional[
        str
    ]  # TT Authorising Advertiser Name (https://business-api.tiktok.com/portal/docs?id=1738455508553729)


@dataclasses.dataclass
class CampaignDetails(object):
    account_id: str
    campaign_id: str
    campaign_name: str
    effective_status: str
    configured_status: typing.Optional[str]
    created_time: str
    updated_time: str


@dataclasses.dataclass
class AdSetDetails(object):
    account_id: str
    campaign_id: str
    adset_id: str
    adset_name: str
    effective_status: str
    configured_status: typing.Optional[str]
    created_time: str
    updated_time: str


@dataclasses.dataclass
class AdDetails(object):
    account_id: str
    campaign_id: str
    adset_id: str
    ad_id: str
    ad_name: str
    effective_status: str
    configured_status: typing.Optional[str]
    created_time: str
    updated_time: str


@dataclasses.dataclass
class ResourceInsightsReport(object):
    account_id: str
    account_name: typing.Optional[str]
    resource_type: str  # Identify resource (campaign, ad set, ad)
    campaign_id: str
    campaign_name: str
    adset_id: typing.Optional[str]
    adset_name: typing.Optional[str]
    ad_id: typing.Optional[str]
    ad_name: typing.Optional[str]
    spend: str
    impressions: str
    clicks: str
    ctr: typing.Optional[str]
    cpm: typing.Optional[str]
    cpc: typing.Optional[str]
    reach: str
    actions: typing.Optional[typing.List[typing.Dict]]
    conversions: typing.List[typing.Dict]
    cost_per_conversion: typing.List[typing.Dict]
    conversion_rate: typing.List[typing.Dict]
    date_start: str
    date_stop: str


# Facebook AdCreative
@dataclasses.dataclass
class AdCreativeDetails(object):
    account_id: str
    creative_id: str
    creative_name: typing.Optional[str]
    title: typing.Optional[str]
    body: typing.Optional[str]
    image_url: typing.Optional[str]


# TikTok ImageDetails
@dataclasses.dataclass
class ImageDetails(object):
    image_id: str
    material_id: str
    size: float
    width: float
    height: float
    format: str
    image_url: str
    signature: str
    file_name: str
    create_time: str
    modify_time: str
    displayable: bool


# TikTok VideoDetails
@dataclasses.dataclass
class VideoDetails(object):
    video_id: str
    material_id: str
    duration: float
    bit_rate: float
    size: float
    width: float
    height: float
    format: str
    video_cover_url: str
    preview_url: str
    preview_url_expire_time: str
    signature: str
    file_name: str
    create_time: str
    modify_time: str
    displayable: bool
    allow_download: bool
    allowed_placements: typing.List[str]
