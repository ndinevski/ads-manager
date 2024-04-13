from ads_manager import enums
from ads_manager.integrations.clients.tiktok import schemas as tiktok_client_schemas

TIKTOK_RESOURCE_DETAILS_FIELDS = {
    enums.ResourceType.CAMPAIGN: [
        "advertiser_id",
        "campaign_id",
        "campaign_name",
        "operation_status",
        "secondary_status",
        "create_time",
        "modify_time",
    ],
    enums.TiktokResourceType.AD_GROUP: [
        "advertiser_id",
        "campaign_id",
        "adgroup_id",
        "adgroup_name",
        "operation_status",
        "secondary_status",
        "create_time",
        "modify_time",
    ],
    enums.ResourceType.AD: [
        "advertiser_id",
        "campaign_id",
        "adgroup_id",
        "ad_id",
        "ad_name",
        "operation_status",
        "secondary_status",
        "create_time",
        "modify_time",
    ],
}


TIKTOK_INSIGHTS_DETAILS_FIELDS = {
    enums.ResourceType.CAMPAIGN: {
        "dimensions": ["campaign_id", "stat_time_day"],
        "metrics": [
            "campaign_name",
            "spend",
            "impressions",
            "clicks",
            "conversion",
            "cost_per_conversion",
            "conversion_rate",
            "ctr",
            "cpm",
            "cpc",
            "reach",
        ],
    },
    enums.TiktokResourceType.AD_GROUP: {
        "dimensions": ["adgroup_id", "stat_time_day"],
        "metrics": [
            "campaign_id",
            "campaign_name",
            "adgroup_name",
            "spend",
            "impressions",
            "clicks",
            "conversion",
            "cost_per_conversion",
            "conversion_rate",
            "ctr",
            "cpm",
            "cpc",
            "reach",
        ],
    },
    enums.ResourceType.AD: {
        "dimensions": ["ad_id", "stat_time_day"],
        "metrics": [
            "campaign_id",
            "campaign_name",
            "adgroup_id",
            "adgroup_name",
            "ad_name",
            "spend",
            "impressions",
            "clicks",
            "conversion",
            "cost_per_conversion",
            "conversion_rate",
            "ctr",
            "cpm",
            "cpc",
            "reach",
        ],
    },
}

TIKTOK_INSIGHTS_SCHEMAS = {
    enums.ResourceType.CAMPAIGN: tiktok_client_schemas.CampaignInsightsReport,
    enums.TiktokResourceType.AD_GROUP: tiktok_client_schemas.AdGroupInsightsReport,
    enums.ResourceType.AD: tiktok_client_schemas.AdInsightsReport,
}
