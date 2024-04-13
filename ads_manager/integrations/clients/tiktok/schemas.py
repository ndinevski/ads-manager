import typing

from marshmallow import EXCLUDE, fields, post_load, pre_load, schema

from ads_manager import utils


class Schema(schema.Schema):
    class Meta:
        unknown = EXCLUDE


class AdAccount(Schema):
    advertiser_id = fields.Str(required=True, data_key="advertiser_id")
    advertiser_name = fields.Str(required=True, data_key="advertiser_name")


class AdAccounts(Schema):
    ad_accounts = fields.Nested(AdAccount, many=True)

    @pre_load
    def pre_process_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"ad_accounts": data}


class CampaignDetails(Schema):
    account_id = fields.Str(required=True, data_key="advertiser_id")
    id = fields.Str(required=True, data_key="campaign_id")
    name = fields.Str(required=True, data_key="campaign_name")
    effective_status = fields.Str(required=True, data_key="operation_status")
    configured_status = fields.Str(required=False, data_key="secondary_status")
    created_time = fields.Str(required=True, data_key="create_time")
    updated_time = fields.Str(required=True, data_key="modify_time")


class CampaignsDetails(Schema):
    campaigns_details = fields.Nested(CampaignDetails, many=True)

    @pre_load
    def pre_process_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"campaigns_details": data}


class AdGroupDetails(Schema):
    account_id = fields.Str(required=True, data_key="advertiser_id")
    campaign_id = fields.Str(required=True, data_key="campaign_id")
    id = fields.Str(required=True, data_key="adgroup_id")
    name = fields.Str(required=True, data_key="adgroup_name")
    effective_status = fields.Str(required=True, data_key="operation_status")
    configured_status = fields.Str(required=False, data_key="secondary_status")
    created_time = fields.Str(required=True, data_key="create_time")
    updated_time = fields.Str(required=True, data_key="modify_time")


class AdGroupsDetails(Schema):
    adgroups_details = fields.Nested(AdGroupDetails, many=True)

    @pre_load
    def pre_process_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"adgroups_details": data}


class AdDetails(Schema):
    account_id = fields.Str(required=True, data_key="advertiser_id")
    campaign_id = fields.Str(required=True, data_key="campaign_id")
    adgroup_id = fields.Str(required=True, data_key="adgroup_id")
    id = fields.Str(required=True, data_key="ad_id")
    name = fields.Str(required=True, data_key="ad_name")
    effective_status = fields.Str(required=True, data_key="operation_status")
    configured_status = fields.Str(required=False, data_key="secondary_status")
    created_time = fields.Str(required=True, data_key="create_time")
    updated_time = fields.Str(required=True, data_key="modify_time")


class AdsDetails(Schema):
    ads_details = fields.Nested(AdDetails, many=True)

    @pre_load
    def pre_process_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"ads_details": data}


class CreativeCreate(Schema):
    operation_status = fields.Str(required=False, data_key="operation_status")
    identity_id = fields.Str(required=True, data_key="identity_id")
    identity_type = fields.Str(required=True, data_key="identity_type")
    identity_authorized_bc_id = fields.Str(required=False, data_key="identity_authorized_bc_id")
    catalog_id = fields.Str(required=False, data_key="catalog_id")
    call_to_action = fields.Str(required=False, data_key="call_to_action")
    call_to_action_id = fields.Str(required=False, data_key="call_to_action_id")
    card_id = fields.Str(required=False, data_key="card_id")
    ad_name = fields.Str(required=True, data_key="ad_name")
    ad_format = fields.Str(required=False, data_key="ad_format")
    carousel_image_index = fields.Int(required=False, data_key="carousel_image_index")
    ad_text = fields.Str(required=False, data_key="ad_text")
    image_ids = fields.List(fields.Str(), required=False, data_key="image_ids")
    video_id = fields.Str(required=False, data_key="video_id")
    tiktok_item_id = fields.Str(required=False, data_key="tiktok_item_id")
    music_id = fields.Str(required=False, data_key="music_id")
    creative_type = fields.Str(required=False, data_key="creative_type")
    app_name = fields.Str(required=False, data_key="app_name")
    landing_page_url = fields.Str(required=False, data_key="landing_page_url")
    utm_params = fields.List(fields.Dict(), required=False, data_key="utm_params")
    display_name = fields.Str(required=False, data_key="display_name")
    avatar_icon_web_uri = fields.Str(required=False, data_key="avatar_icon_web_uri")
    impression_tracking_url = fields.Str(required=False, data_key="impression_tracking_url")
    click_tracking_url = fields.Str(required=False, data_key="click_tracking_url")
    video_view_tracking_url = fields.Str(required=False, data_key="video_view_tracking_url")
    deeplink = fields.Str(required=False, data_key="deeplink")
    deeplink_type = fields.Str(required=False, data_key="deeplink_type")
    fallback_type = fields.Str(required=False, data_key="fallback_type")
    playable_url = fields.Str(required=False, data_key="playable_url")
    page_id = fields.Number(required=False, data_key="page_id")
    vast_moat_enabled = fields.Boolean(required=False, data_key="vast_moat_enabled")
    creative_authorized = fields.Boolean(required=False, data_key="creative_authorized")
    shopping_ads_fallback_type = fields.Str(required=False, data_key="shopping_ads_fallback_type")
    shopping_ads_deeplink_type = fields.Str(required=False, data_key="shopping_ads_deeplink_type")
    shopping_ads_video_package_id = fields.Str(required=False, data_key="shopping_ads_video_package_id")
    promotional_music_disabled = fields.Boolean(required=False, data_key="promotional_music_disabled")
    dark_post_status = fields.Str(required=False, data_key="dark_post_status")
    item_duet_status = fields.Str(required=False, data_key="item_duet_status")
    item_stitch_status = fields.Str(required=False, data_key="item_stitch_status")
    brand_safety_postbid_partner = fields.Str(required=False, data_key="brand_safety_postbid_partner")
    brand_safety_vast_url = fields.Str(required=False, data_key="brand_safety_vast_url")
    viewability_postbid_partner = fields.Str(required=False, data_key="viewability_postbid_partner")
    viewability_vast_url = fields.Str(required=False, data_key="viewability_vast_url")
    tracking_pixel_id = fields.Number(required=False, data_key="tracking_pixel_id")
    tracking_app_id = fields.Str(required=False, data_key="tracking_app_id")
    tracking_offline_event_set_ids = fields.List(
        fields.Str(), required=False, data_key="tracking_offline_event_set_ids"
    )
    product_specific_type = fields.Str(required=False, data_key="product_specific_type")
    item_group_ids = fields.List(fields.Str(), required=False, data_key="item_group_ids")
    product_set_id = fields.Str(required=False, data_key="product_set_id")
    sku_ids = fields.Str(required=False, data_key="sku_ids")
    dynamic_format = fields.Str(required=False, data_key="dynamic_format")
    vertical_video_strategy = fields.Str(required=False, data_key="vertical_video_strategy")
    dynamic_destination = fields.Str(required=False, data_key="dynamic_destination")
    instant_product_page_used = fields.Boolean(required=False, data_key="instant_product_page_used")
    page_image_index = fields.Int(required=False, data_key="page_image_index")
    disclaimer_type = fields.Str(required=False, data_key="disclaimer_type")
    disclaimer_text = fields.Dict(required=False, data_key="disclaimer_text")
    disclaimer_clickable_texts = fields.List(fields.Dict(), required=False, data_key="disclaimer_clickable_texts")
    showcase_products = fields.List(fields.Dict(), required=False, data_key="showcase_products")

    @post_load
    def post_process_data(self, data: typing.Dict, **kwargs: typing.Any) -> typing.Dict:
        return utils.convert_schema_list_and_dict_fields_to_json_string(data=data)


class CreativeUpdate(CreativeCreate):
    ad_id = fields.Str(required=False, data_key="ad_id")


class AdCreate(Schema):
    advertiser_id = fields.Str(required=True, data_key="advertiser_id")
    adgroup_id = fields.Str(required=True, data_key="adgroup_id")
    creatives = fields.Nested(CreativeCreate, many=True, required=True, data_key="creatives")


class AdUpdate(AdCreate):
    creatives = fields.Nested(CreativeUpdate, many=True, required=True, data_key="creatives")


class AdStatusUpdate(Schema):
    advertiser_id = fields.Str(required=True, data_key="advertiser_id")
    ad_ids = fields.List(fields.Str(), required=False, data_key="ad_ids")
    aco_ad_ids = fields.List(fields.Str(), required=False, data_key="aco_ad_ids")
    operation_status = fields.Str(required=True, data_key="operation_status")

    @post_load
    def post_process_data(self, data: typing.Dict, **kwargs: typing.Any) -> typing.Dict:
        return utils.convert_schema_list_and_dict_fields_to_json_string(data=data)


class CampaignCreate(Schema):
    advertiser_id = fields.Str(required=True, data_key="advertiser_id")
    campaign_name = fields.Str(required=True, data_key="campaign_name")
    objective_type = fields.Str(required=True, data_key="objective_type")
    operation_status = fields.Str(required=False, data_key="operation_status")
    campaign_type = fields.Str(required=False, data_key="campaign_type")
    app_id = fields.Str(required=False, data_key="app_id")
    budget = fields.Float(required=False, data_key="budget")
    budget_mode = fields.Str(required=False, data_key="budget_mode")
    budget_optimize_on = fields.Boolean(required=False, data_key="budget_optimize_on", default=False)
    request_id = fields.Str(required=False, data_key="request_id")
    app_promotion_type = fields.Str(required=False, data_key="app_promotion_type")
    campaign_app_profile_page_state = fields.Str(required=False, data_key="campaign_app_profile_page_state")
    special_industries = fields.List(fields.Str(), required=False, data_key="special_industries")
    rf_campaign_type = fields.Str(required=False, data_key="rf_campaign_type")
    campaign_product_source = fields.Str(required=False, data_key="campaign_product_source")


class CampaignUpdate(Schema):
    advertiser_id = fields.Str(required=True, data_key="advertiser_id")
    campaign_name = fields.Str(required=True, data_key="campaign_name")
    campaign_id = fields.Str(required=True, data_key="campaign_id")
    budget = fields.Float(required=False, data_key="budget")
    budget_mode = fields.Str(required=False, data_key="budget_mode")
    special_industries = fields.List(fields.Str(), required=False, data_key="special_industries")


class AdGroupCreate(Schema):
    advertiser_id = fields.Str(required=True, data_key="advertiser_id")
    campaign_id = fields.Str(required=True, data_key="campaign_id")
    adgroup_name = fields.Str(required=True, data_key="adgroup_name")
    operation_status = fields.Str(required=False, data_key="operation_status")
    placement_type = fields.Str(required=False, data_key="placement_type")
    placements = fields.List(fields.Str(), required=False, data_key="placements")
    request_id = fields.Str(required=False, data_key="request_id")
    comment_disabled = fields.Boolean(required=False, data_key="comment_disabled", default=False)
    app_id = fields.Str(required=False, data_key="app_id")
    promotion_type = fields.Str(required=False, data_key="promotion_type")
    promotion_target_type = fields.Str(required=False, data_key="promotion_target_type")
    shopping_ads_type = fields.Str(required=False, data_key="shopping_ads_type")
    product_source = fields.Str(required=False, data_key="product_source")
    shopping_ads_retargeting_type = fields.Str(required=False, data_key="shopping_ads_retargeting_type")
    shopping_ads_retargeting_actions_days = fields.Number(
        required=False, data_key="shopping_ads_retargeting_actions_days"
    )
    included_custom_actions = fields.List(fields.Dict, required=False, data_key="included_custom_actions")
    excluded_custom_actions = fields.List(fields.Dict, required=False, data_key="excluded_custom_actions")
    store_id = fields.Str(required=False, data_key="store_id")
    store_authorized_bc_id = fields.Str(required=False, data_key="store_authorized_bc_id")
    identity_id = fields.Str(required=False, data_key="identity_id")
    identity_type = fields.Str(required=False, data_key="identity_type")
    identity_authorized_bc_id = fields.Str(required=False, data_key="identity_authorized_bc_id")
    pixel_id = fields.Str(required=False, data_key="pixel_id")
    creative_material_mode = fields.Str(required=False, data_key="creative_material_mode")
    audience_ids = fields.List(fields.Str(), required=False, data_key="audience_ids")
    excluded_audience_ids = fields.List(fields.Str(), required=False, data_key="excluded_audience_ids")
    audience_rule = fields.Dict(required=False, data_key="audience_rule")
    audience_type = fields.Str(required=False, data_key="audience_type")
    location_ids = fields.List(fields.Str(), required=False, data_key="location_ids")
    zipcode_ids = fields.List(fields.Str(), required=False, data_key="zipcode_ids")
    isp_ids = fields.List(fields.Str(), required=False, data_key="isp_ids")
    is_hfss = fields.Boolean(required=False, data_key="is_hfss", default=False)
    interest_category_ids = fields.List(fields.Str(), required=False, data_key="interest_category_ids")
    interest_keyword_ids = fields.List(fields.Str(), required=False, data_key="interest_keyword_ids")
    age_groups = fields.List(fields.Str(), required=False, data_key="age_groups")
    gender = fields.Str(required=False, data_key="gender")
    languages = fields.List(fields.Str(), required=False, data_key="languages")
    operating_systems = fields.List(fields.Str(), required=False, data_key="operating_systems")
    network_types = fields.List(fields.Str(), required=False, data_key="network_types")
    device_price_ranges = fields.List(fields.Number, required=False, data_key="device_price_ranges")
    min_android_version = fields.Str(required=False, data_key="min_android_version")
    min_ios_version = fields.Str(required=False, data_key="min_ios_version")
    ios14_targeting = fields.Str(required=False, data_key="ios14_targeting")
    device_model_ids = fields.List(fields.Str(), required=False, data_key="device_model_ids")
    household_income = fields.List(fields.Str(), required=False, data_key="household_income")
    spending_power = fields.Str(required=False, data_key="spending_power")
    budget = fields.Float(required=True, data_key="budget")
    budget_mode = fields.Str(required=True, data_key="budget_mode")
    budget_optimize_on = fields.Boolean(required=False, data_key="budget_optimize_on", default=False)
    schedule_type = fields.Str(required=True, data_key="schedule_type")
    schedule_start_time = fields.Str(required=True, data_key="schedule_start_time")
    schedule_end_time = fields.Str(required=False, data_key="schedule_end_time")
    dayparting = fields.Str(required=False, data_key="dayparting")
    optimization_goal = fields.Str(required=False, data_key="optimization_goal")
    optimization_event = fields.Str(required=False, data_key="optimization_event")
    secondary_optimization_event = fields.Str(required=False, data_key="secondary_optimization_event")
    pacing = fields.Str(required=True, data_key="pacing")
    billing_event = fields.Str(required=True, data_key="billing_event")
    bid_type = fields.Str(required=False, data_key="bid_type")
    bid_price = fields.Float(required=False, data_key="bid_price")
    conversion_bid_price = fields.Float(required=False, data_key="conversion_bid_price")
    deep_bid_type = fields.Str(required=False, data_key="deep_bid_type")
    bid_display_mode = fields.Str(required=False, data_key="bid_display_mode")
    next_day_retention = fields.Float(required=False, data_key="next_day_retention")
    frequency = fields.Number(required=False, data_key="frequency")
    frequency_schedule = fields.Number(required=False, data_key="frequency_schedule")
    statistic_type = fields.Str(required=False, data_key="statistic_type")
    carrier_ids = fields.List(fields.Str(), required=False, data_key="carrier_ids")
    video_download_disabled = fields.Boolean(required=False, data_key="video_download_disabled", default=False)
    blocked_pangle_app_ids = fields.List(fields.Str(), required=False, data_key="blocked_pangle_app_ids")
    actions = fields.List(fields.Dict(), required=False, data_key="actions")
    included_pangle_audience_package_ids = fields.List(
        fields.Str(), required=False, data_key="included_pangle_audience_package_ids"
    )
    excluded_pangle_audience_package_ids = fields.List(
        fields.Str(), required=False, data_key="excluded_pangle_audience_package_ids"
    )
    catalog_id = fields.Str(required=False, data_key="catalog_id")
    product_set_id = fields.Str(required=False, data_key="product_set_id")
    catalog_authorized_bc_id = fields.Str(required=False, data_key="catalog_authorized_bc_id")
    roas_bid = fields.Float(required=False, data_key="roas_bid")
    brand_safety_type = fields.Str(required=False, data_key="brand_safety_type")
    brand_safety_partner = fields.Str(required=False, data_key="brand_safety_partner")
    adgroup_app_profile_page_state = fields.Str(required=False, data_key="adgroup_app_profile_page_state")
    contextual_tag_ids = fields.List(fields.Str(), required=False, data_key="contextual_tag_ids")
    purchase_intention_keyword_ids = fields.List(
        fields.Str(), required=False, data_key="purchase_intention_keyword_ids"
    )
    share_disabled = fields.Boolean(required=False, data_key="share_disabled", default=False)
    category_exclusion_ids = fields.List(fields.Str(), required=False, data_key="category_exclusion_ids")
    vertical_sensitivity_id = fields.Str(required=False, data_key="vertical_sensitivity_id")

    @post_load
    def post_process_data(self, data: typing.Dict, **kwargs: typing.Any) -> typing.Dict:
        return utils.convert_schema_list_and_dict_fields_to_json_string(data=data)


class AdGroupUpdate(AdGroupCreate):
    adgroup_id = fields.Str(required=True, data_key="adgroup_id")
    deep_cpa_bid = fields.Float(required=False, data_key="deep_cpa_bid")
    adgroup_name = fields.Str(required=False, data_key="adgroup_name")


class ImageCreate(Schema):
    advertiser_id = fields.Str(required=True, data_key="advertiser_id")
    file_name = fields.Str(required=False, data_key="file_name")
    upload_type = fields.Str(required=True, data_key="upload_type")
    image_file = fields.Field(required=False, data_key="image_file")
    image_signature = fields.Str(required=False, data_key="image_signature")
    image_url = fields.Str(required=False, data_key="image_url")
    file_id = fields.Str(required=False, data_key="file_id")


class ImageUpdate(Schema):
    advertiser_id = fields.Str(required=True, data_key="advertiser_id")
    file_name = fields.Str(required=True, data_key="file_name")
    image_id = fields.Str(required=True, data_key="image_id")


class ImageInfoParams(Schema):
    advertiser_id = fields.Str(required=True, data_key="advertiser_id")
    image_ids = fields.List(fields.Str(), required=True, data_key="image_ids")

    @post_load
    def post_process_data(self, data: typing.Dict, **kwargs: typing.Any) -> typing.Dict:
        return utils.convert_schema_list_and_dict_fields_to_json_string(data=data)


class ImageDetails(Schema):
    image_id = fields.Str(required=True, data_key="image_id")
    material_id = fields.Str(required=True, data_key="material_id")
    size = fields.Number(required=True, data_key="size")
    width = fields.Number(required=True, data_key="width")
    height = fields.Number(required=True, data_key="height")
    format = fields.Str(required=True, data_key="format")
    image_url = fields.Str(required=True, data_key="image_url")
    signature = fields.Str(required=True, data_key="signature")
    file_name = fields.Str(required=True, data_key="file_name")
    create_time = fields.Str(required=True, data_key="create_time")
    modify_time = fields.Str(required=True, data_key="modify_time")
    displayable = fields.Boolean(required=True, data_key="displayable")


class ImageDetailsResponse(Schema):
    image_details = fields.Nested(ImageDetails, many=True)

    @pre_load
    def pre_process_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"image_details": data}


class VideoCreate(Schema):
    advertiser_id = fields.Str(required=True, data_key="advertiser_id")
    file_name = fields.Str(required=False, data_key="file_name")
    upload_type = fields.Str(required=True, data_key="upload_type")
    video_file = fields.Field(required=False, data_key="video_file")
    video_signature = fields.Str(required=False, data_key="video_signature")
    video_url = fields.Str(required=False, data_key="video_url")
    file_id = fields.Str(required=False, data_key="file_id")
    video_id = fields.Str(required=False, data_key="video_id")
    is_third_party = fields.Boolean(required=False, data_key="is_third_party")
    flaw_detect = fields.Boolean(required=False, data_key="flaw_detect")
    auto_fix_enabled = fields.Boolean(required=False, data_key="auto_fix_enabled")
    auto_bind_enabled = fields.Boolean(required=False, data_key="auto_bind_enabled")


class VideoUpdate(Schema):
    advertiser_id = fields.Str(required=True, data_key="advertiser_id")
    file_name = fields.Str(required=True, data_key="file_name")
    video_id = fields.Str(required=True, data_key="video_id")


class VideoInfoParams(Schema):
    advertiser_id = fields.Str(required=True, data_key="advertiser_id")
    video_ids = fields.List(fields.Str(), required=True, data_key="video_ids")

    @post_load
    def post_process_data(self, data: typing.Dict, **kwargs: typing.Any) -> typing.Dict:
        return utils.convert_schema_list_and_dict_fields_to_json_string(data=data)


class VideoDetails(Schema):
    video_id = fields.Str(required=True, data_key="video_id")
    material_id = fields.Str(required=True, data_key="material_id")
    duration = fields.Number(required=True, data_key="duration")
    bit_rate = fields.Number(required=True, data_key="bit_rate")
    size = fields.Number(required=True, data_key="size")
    width = fields.Number(required=True, data_key="width")
    height = fields.Number(required=True, data_key="height")
    format = fields.Str(required=True, data_key="format")
    video_cover_url = fields.Str(required=True, data_key="video_cover_url")
    preview_url = fields.Str(required=True, data_key="preview_url")
    preview_url_expire_time = fields.Str(required=True, data_key="preview_url_expire_time")
    signature = fields.Str(required=True, data_key="signature")
    file_name = fields.Str(required=True, data_key="file_name")
    create_time = fields.Str(required=True, data_key="create_time")
    modify_time = fields.Str(required=True, data_key="modify_time")
    displayable = fields.Boolean(required=True, data_key="displayable")
    allow_download = fields.Boolean(required=True, data_key="allow_download")
    allowed_placements = fields.List(fields.Str(), required=True, data_key="allowed_placements")


class VideoDetailsResponse(Schema):
    video_details = fields.Nested(VideoDetails, many=True)

    @pre_load
    def pre_process_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"video_details": data}


class CampaignInsightMetrics(Schema):
    campaign_name = fields.Str(required=True, data_key="campaign_name")
    spend = fields.Str(required=True, data_key="spend")
    impressions = fields.Str(required=True, data_key="impressions")
    clicks = fields.Str(required=True, data_key="clicks")
    ctr = fields.Str(required=True, data_key="ctr")
    cpm = fields.Str(required=True, data_key="cpm")
    cpc = fields.Str(required=True, data_key="cpc")
    reach = fields.Str(required=True, data_key="reach")
    conversions = fields.Str(required=True, data_key="conversion")
    cost_per_conversion = fields.Str(required=True, data_key="cost_per_conversion")
    conversion_rate = fields.Str(required=True, data_key="conversion_rate")


class AdGroupInsightMetrics(CampaignInsightMetrics):
    campaign_id = fields.Str(required=True, data_key="campaign_id")
    adgroup_name = fields.Str(required=True, data_key="adgroup_name")


class AdInsightsMetrics(AdGroupInsightMetrics):
    adgroup_id = fields.Str(required=True, data_key="adgroup_id")
    ad_name = fields.Str(required=True, data_key="ad_name")


class InsightDimensions(Schema):
    stat_time_day = fields.Str(required=True, data_key="stat_time_day")


class CampaignInsightDimensions(InsightDimensions):
    campaign_id = fields.Str(required=True, data_key="campaign_id")


class AdGroupInsightDimensions(InsightDimensions):
    adgroup_id = fields.Str(required=True, data_key="adgroup_id")


class AdInsightDimensions(InsightDimensions):
    ad_id = fields.Str(required=True, data_key="ad_id")


class ResourceInsights(Schema):
    @pre_load
    def pre_process_data(self, data: typing.Dict, **kwargs: typing.Any) -> typing.Dict:
        metrics = data.get("metrics", {})
        dimensions = data.get("dimensions", {})
        return {**metrics, **dimensions}

    @post_load
    def post_process_data(self, data: typing.Dict, **kwargs: typing.Any) -> typing.Dict:
        time_day = data.pop("stat_time_day", None)
        data["start_date"] = time_day
        data["end_date"] = time_day
        return data


class CampaignInsights(ResourceInsights, CampaignInsightMetrics, CampaignInsightDimensions):
    pass


class AdGroupInsights(ResourceInsights, AdGroupInsightMetrics, AdGroupInsightDimensions):
    pass


class AdInsights(ResourceInsights, AdInsightsMetrics, AdInsightDimensions):
    pass


class InsightsReport(Schema):
    def __init__(self, advertiser_id):
        super(InsightsReport, self).__init__()
        self.advertiser_id = advertiser_id

    resource_insights = fields.Nested(ResourceInsights, many=True)

    @pre_load
    def pre_process_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"resource_insights": data}

    @post_load
    def post_process_data(self, data: typing.Dict, **kwargs: typing.Any) -> typing.Dict:
        for entry in data["resource_insights"]:
            entry["advertiser_id"] = self.advertiser_id
        return data


class CampaignInsightsReport(InsightsReport):
    resource_insights = fields.Nested(CampaignInsights, many=True)


class AdGroupInsightsReport(InsightsReport):
    resource_insights = fields.Nested(AdGroupInsights, many=True)


class AdInsightsReport(InsightsReport):
    resource_insights = fields.Nested(AdInsights, many=True)
