import datetime
import json
import typing

from marshmallow import EXCLUDE, fields, post_load, pre_load, schema


class Schema(schema.Schema):
    class Meta:
        unknown = EXCLUDE


class AdAccount(Schema):
    id = fields.Str(required=True, data_key="id")
    account_id = fields.Str(required=True, data_key="account_id")


class AdAccounts(Schema):
    ad_accounts = fields.Nested(AdAccount, many=True)

    @pre_load
    def prepare_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"ad_accounts": data}


class CampaignDetails(Schema):
    account_id = fields.Str(required=True, data_key="account_id")
    id = fields.Str(required=True, data_key="id")
    name = fields.Str(required=True, data_key="name")
    effective_status = fields.Str(required=True, data_key="effective_status")
    configured_status = fields.Str(required=True, data_key="configured_status")
    created_time = fields.Str(required=True, data_key="created_time")
    updated_time = fields.Str(required=True, data_key="updated_time")


class CampaignsDetails(Schema):
    campaigns_details = fields.Nested(CampaignDetails, many=True)

    @pre_load
    def prepare_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"campaigns_details": data}


class AdSetDetails(Schema):
    account_id = fields.Str(required=True, data_key="account_id")
    campaign_id = fields.Str(required=True, data_key="campaign_id")
    id = fields.Str(required=True, data_key="id")
    name = fields.Str(required=True, data_key="name")
    effective_status = fields.Str(required=True, data_key="effective_status")
    configured_status = fields.Str(required=True, data_key="configured_status")
    created_time = fields.Str(required=True, data_key="created_time")
    updated_time = fields.Str(required=True, data_key="updated_time")


class AdSetsDetails(Schema):
    adsets_details = fields.Nested(AdSetDetails, many=True)

    @pre_load
    def prepare_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"adsets_details": data}


class AdDetails(Schema):
    account_id = fields.Str(required=True, data_key="account_id")
    campaign_id = fields.Str(required=True, data_key="campaign_id")
    ad_id = fields.Str(required=True, data_key="ad_id")
    id = fields.Str(required=True, data_key="id")
    name = fields.Str(required=True, data_key="name")
    effective_status = fields.Str(required=True, data_key="effective_status")
    configured_status = fields.Str(required=True, data_key="configured_status")
    created_time = fields.Str(required=True, data_key="created_time")
    updated_time = fields.Str(required=True, data_key="updated_time")


class AdsDetails(Schema):
    ads_details = fields.Nested(AdDetails, many=True)

    @pre_load
    def prepare_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"ads_details": data}


class AdCreativeDetails(Schema):
    account_id = fields.Str(required=True, data_key="account_id")
    id = fields.Str(required=True, data_key="id")
    name = fields.Str(required=False, data_key="name")
    title = fields.Str(required=False, data_key="title")
    body = fields.Str(required=False, data_key="body")
    image_url = fields.Str(required=False, data_key="image_url")


class AdCreativesDetails(Schema):
    adcreatives_details = fields.Nested(AdCreativeDetails, many=True)

    @pre_load
    def prepare_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"adcreatives_details": data}


class ReportStatus(Schema):
    async_percent_completion = fields.Integer(required=True, data_key="async_percent_completion")
    is_running = fields.Bool(data_key="is_running", missing=False)


class Action(Schema):
    action_type = fields.Str(required=True, data_key="action_type")
    value = fields.Str(required=True, data_key="value")


class InsightReport(Schema):
    account_id = fields.Str(required=True, data_key="account_id")
    account_name = fields.Str(required=True, data_key="account_name")
    spend = fields.Str(required=True, data_key="spend")
    impressions = fields.Str(required=True, data_key="impressions")
    clicks = fields.Str(required=True, data_key="clicks")
    ctr = fields.Str(required=False, data_key="ctr")
    cpm = fields.Str(required=False, data_key="cpm")
    cpc = fields.Str(required=False, data_key="cpc")
    reach = fields.Str(required=True, data_key="reach")
    actions = fields.Nested(Action, many=True, data_key="actions")
    conversions = fields.Nested(Action, many=True, data_key="conversions")
    cost_per_conversion = fields.Nested(Action, many=True, data_key="cost_per_conversion")
    date_start = fields.Str(required=True, data_key="date_start")
    date_stop = fields.Str(required=True, data_key="date_stop")


class CampaignInsightReport(InsightReport):
    campaign_id = fields.Str(required=True, data_key="campaign_id")
    campaign_name = fields.Str(required=True, data_key="campaign_name")


class CampaignsInsightReport(Schema):
    insights = fields.Nested(CampaignInsightReport, many=True)

    @pre_load
    def prepare_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"insights": data}


class AdSetInsightReport(CampaignInsightReport):
    adset_id = fields.Str(required=True, data_key="adset_id")
    adset_name = fields.Str(required=True, data_key="adset_name")


class AdSetsInsightReport(Schema):
    insights = fields.Nested(AdSetInsightReport, many=True)

    @pre_load
    def prepare_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"insights": data}


class AdInsightReport(AdSetInsightReport):
    ad_id = fields.Str(required=True, data_key="ad_id")
    ad_name = fields.Str(required=True, data_key="ad_name")


class AdsInsightReport(Schema):
    insights = fields.Nested(AdInsightReport, many=True)

    @pre_load
    def prepare_data(self, data: typing.List[typing.Dict], **kwargs: typing.Any) -> typing.Dict:
        return {"insights": data}


class Campaign(Schema):
    name = fields.Str(required=True, data_key="name")
    special_ad_categories = fields.List(fields.Str(), required=True, data_key="special_ad_categories")
    objective = fields.Str(required=True, data_key="objective")

    @post_load
    def prepare_data(self, data: typing.Dict, **kwargs: typing.Any) -> typing.Dict:
        data["special_ad_categories"] = json.dumps(data["special_ad_categories"])
        return data


class AdSet(Schema):
    daily_budget = fields.Integer(required=True, data_key="daily_budget")
    name = fields.Str(required=True, data_key="name")
    campaign_id = fields.List(fields.Str(), required=True, data_key="campaign_id")
    bid_amount = fields.Integer(required=True, data_key="bid_amount")
    billing_event = fields.Str(required=True, data_key="billing_event")
    optimization_goal = fields.Str(required=True, data_key="optimization_goal")
    promoted_object = fields.Dict(required=True, data_key="promoted_object")
    targeting = fields.Dict(required=True, data_key="targeting")
    status = fields.Str(required=True, data_key="status")

    @post_load
    def prepare_data(self, data: typing.Dict, **kwargs: typing.Any) -> typing.Dict:
        data["targeting"] = json.dumps(data["targeting"])
        data["promoted_object"] = json.dumps(data["promoted_object"])
        return data


class AdCreativeObjectStorySpec(Schema):
    page_id = fields.Str(required=True, data_key="str")
    link_data = fields.Dict(required=True, data_key="link_data")


class AdCreative(Schema):
    name = fields.Str(required=True, data_key="name")
    object_story_spec = fields.Nested(AdCreativeObjectStorySpec, data_key="object_story_spec")

    @post_load
    def prepare_data(self, data: typing.Dict, **kwargs: typing.Any) -> typing.Dict:
        data["object_story_spec"] = json.dumps(data["object_story_spec"])
        return data


class Ad(Schema):
    name = fields.Str(required=True, data_key="name")
    adset_id = fields.Str(required=True, data_key="adset_id")
    creative = fields.Dict(required=True, data_key="creative")
    status = fields.Str(required=True, data_key="status")

    @post_load
    def prepare_data(self, data: typing.Dict, **kwargs: typing.Any) -> typing.Dict:
        data["creative"] = json.dumps(data["creative"])
        return data
