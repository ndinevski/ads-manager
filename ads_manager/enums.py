import enum


class HttpMethod(enum.Enum):
    GET = "get"
    POST = "post"


class ResourceType(enum.Enum):
    AD = "ad"
    CAMPAIGN = "campaign"
    AD_SET = "adset"
    AD_CREATIVE = "adcreative"


class FacebookResourceType(enum.Enum):
    AD = "ad"
    CAMPAIGN = "campaign"
    AD_SET = "adset"
    AD_CREATIVE = "adcreative"


class TiktokResourceType(enum.Enum):
    AD = "ad"
    CAMPAIGN = "campaign"
    AD_GROUP = "adgroup"  # This is equivalent to AD_SET from ResourceType


class TimeIncrement(enum.Enum):
    DAY = 1
    WEEK = 7
    MONTH = 30


class Platform(enum.Enum):
    FACEBOOK = "facebook"
    TIKTOK = "tiktok"
