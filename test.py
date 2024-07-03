import datetime
import ast
import os
from dotenv import load_dotenv

from ads_manager.services.unified import exporter, importer
from ads_manager.services.facebook import importer as facebook_importer
from ads_manager.services.facebook import exporter as facebook_exporter
from ads_manager.services.tiktok import importer as tiktok_importer
from ads_manager.services.tiktok import exporter as tiktok_exporter
from ads_manager import enums


def print_json(message):
    print(message)


def main():
    load_dotenv()

    fb_token = "EAANY2CrI0jUBO80TYU3COJfdSOQw0POgUuTmg69nWSt1cFwqfyjqgFiOXoCIgFXtcYvren482XwZC5RbHPZAktZByJomwzQpEZC5drDNq0V1tg5C23emycb7oaHECFeybQAiCCq3IxdmPJzEbeMCNQpBCqr8djUEFiZCxkgmHYcfPHUsjw8yuLHJwIOabrF4waUWXQ6WW"
    fb_account_ids = ["act_366883153087738"]
    tt_token = os.getenv("TT_TOKEN")
    tt_account_ids = ast.literal_eval(os.getenv("TT_ACCOUNT_IDS"))
    tt_app_id = os.getenv("TT_APP_ID")
    tt_secret = os.getenv("TT_SECRET")

    # I. EXPORTER SERVICES (TikTok, Facebook, Unified)
    #
    # - REPORT:
    # Note:
    # except for comments in brackets '()' next to functionalities,
    # everything is functioning properly and no issues detected
    # there is use of labels, empty (explained at the first appearance)
    # and not supported in sandbox. As well as other descriptive labels.
    # Additionally, in all tests invalid or incorrect inputs were tested,
    # similar to invalid inputs tests for get_campaigns_details in TikTok.
    #
    # 1. Verified and tested TIKTOK exporter functionalities:
    #   - get_account_ids (not supported in sandbox)
    #   - get_campaigns_details
    #   - get_adgroups_details
    #   - get_ads_details (IMPORTANT : checked docs, works properly and fields are correct
    #                      but no ads in response, response is empty. Probably because of
    #                      no ads created and there is no data. I will denote all upcoming
    #                      same instances with the 'empty')
    #   - get_campaign_insights (empty)
    #   - get_adset_insights (empty)
    #   - get_ad_insights (empty)
    #   - get_images_details (not supported in sandbox)
    #   - get_videos_details (not supported in sandbox)
    # 2. Verified and tested FACEBOOK exporter functionalities:
    #   - get_account_ids
    #   - get_campaigns_details
    #   - get_adsets_details (empty)
    #   - get_ads_details (empty)
    #   - get_campaign_insights (empty)
    #   - get_adset_insights (empty)
    #   - get_ad_insights (empty)
    #   - get_ad_creatives_list (empty)
    #   - get_ad_creatives (don't have asset_ids to test)
    # 3. Verified and tested UNIFIED exporter functionalities:
    #   - get_account_ids (not supported for TikTok)
    #   - get_campaigns_details
    #   - get_adsets_details (Facebook empty | TikTok okay)
    #   - get_ads_details (empty)
    #   - get_campaign_insights (empty)
    #   - get_adset_insights (empty)
    #   - get_ad_insights (empty)
    #   - get_insights_by_resource_type (Campaign, Ad set, Ad) (empty)

    # - TESTS:

    # TIKTOK :

    # print_json(tiktok_exporter.get_campaigns_details(
    #     user_access_token=tt_token,
    #     params={'sandbox': True},
    #     account_ids=tt_account_ids))

    # print_json(tiktok_exporter.get_campaigns_details(
    #     user_access_token="incorrect_token",
    #     params={'sandbox': True},
    #     account_ids=tt_account_ids))

    # print_json(tiktok_exporter.get_campaigns_details(
    #     user_access_token=tt_token,
    #     params={'sandbox': True},
    #     account_ids=["incorrect_account_id"]))

    # print_json(tiktok_exporter.get_adgroups_details(
    #     user_access_token=tt_token,
    #     params={'sandbox': True},
    #     account_ids=tt_account_ids))

    # print_json(tiktok_exporter.get_ads_details(
    #     user_access_token=tt_token,
    #     params={'sandbox': True},
    #     account_ids=tt_account_ids))

    # print_json(tiktok_exporter.get_campaign_insights(
    #     user_access_token=tt_token,
    #     account_ids=tt_account_ids,
    #     date_from=datetime.datetime(2023, 7, 25),
    #     date_to=datetime.datetime(2023, 8, 15),
    #     params={'sandbox': True}))

    # print_json(tiktok_exporter.get_adgroup_insights(
    #     user_access_token=tt_token,
    #     account_ids=tt_account_ids,
    #     date_from=datetime.datetime(2023, 7, 25),
    #     date_to=datetime.datetime(2023, 8, 15),
    #     params={'sandbox': True}))

    # print_json(tiktok_exporter.get_ad_insights(
    #     user_access_token=tt_token,
    #     account_ids=tt_account_ids,
    #     date_from=datetime.datetime(2023, 7, 25),
    #     date_to=datetime.datetime(2023, 8, 15),
    #     params={'sandbox': True}))

    # FACEBOOK:

    # print_json(facebook_exporter.get_account_ids(
    #     user_access_token=fb_token
    # ))

    # print_json(facebook_importer.create_campaign(
    #     user_access_token=fb_token,
    #     ad_account_id=fb_account_ids[0],
    #     campaign_details={
    #        'name': 'My Campaign 2',
    #        'objective': 'OUTCOME_TRAFFIC',
    #        'status':'PAUSED',
    #        'special_ad_categories': ['NONE']
    #      }
    # ))

    # print_json(facebook_exporter.get_campaigns_details(
    #     user_access_token=fb_token,
    #     account_ids=fb_account_ids,
    # ))

    # print_json(facebook_importer.create_ad_set(
    #     user_access_token=fb_token,
    #     ad_account_id=fb_account_ids[0],
    #     adset_details={
    #         'name': 'My AdSet 2',
    #         'optimization_goal': 'IMPRESSIONS',
    #         'billing_event': 'IMPRESSIONS',
    #         'bid_amount': 20,
    #         'promoted_object': {},
    #         'daily_budget': 1000,
    #         'campaign_id': ['120330000915611219'],
    #         'targeting': {'geo_locations':{'countries':['US']}},
    #         'status': 'PAUSED',
    #     }
    # ))

    # print_json(facebook_exporter.get_adsets_details(
    #     user_access_token=fb_token,
    #     account_ids=fb_account_ids))

    # print_json(facebook_exporter.get_ads_details(
    #     user_access_token=fb_token,
    #     account_ids=fb_account_ids))

    # print_json(facebook_exporter.get_campaign_insights(
    #     user_access_token=fb_token,
    #     account_ids=fb_account_ids,
    #     date_from=datetime.datetime(2023, 1, 1),
    #     date_to=datetime.datetime(2023, 12, 30)))

    # print_json(facebook_exporter.get_adset_insights(
    #     user_access_token=fb_token,
    #     account_ids=fb_account_ids,
    #     date_from=datetime.datetime(2023, 1, 1),
    #     date_to=datetime.datetime(2023, 12, 30)))

    # print_json(facebook_exporter.get_ad_insights(
    #     user_access_token=fb_token,
    #     account_ids=fb_account_ids,
    #     date_from=datetime.datetime(2023, 1, 1),
    #     date_to=datetime.datetime(2023, 12, 30)))

    # print_json(facebook_exporter.get_ad_creatives_list(
    #     user_access_token=fb_token,
    #     account_ids=fb_account_ids))

    # UNIFIED:

    # print_json(exporter.get_account_ids(
    #     user_access_token=fb_token,
    #     platform=enums.Platform.FACEBOOK,
    # ))

    # print_json(exporter.get_campaigns_details(
    #     user_access_token=tt_token,
    #     params={'sandbox': True},
    #     account_ids=tt_account_ids,
    #     platform=enums.Platform.TIKTOK))

    # print_json(exporter.get_campaigns_details(
    #     user_access_token=fb_token,
    #     account_ids=fb_account_ids,
    #     platform=enums.Platform.FACEBOOK))

    # print_json(exporter.get_adsets_details(
    #     user_access_token=tt_token,
    #     account_ids=tt_account_ids,
    #     platform=enums.Platform.TIKTOK,
    #     params={"sandbox": True}))

    # print_json(exporter.get_adsets_details(
    #     user_access_token=fb_token,
    #     account_ids=fb_account_ids,
    #     platform=enums.Platform.FACEBOOK))

    # print_json(exporter.get_ads_details(
    #     user_access_token=tt_token,
    #     account_ids=tt_account_ids,
    #     platform=enums.Platform.TIKTOK,
    #     params={'sandbox': True}))

    # print_json(exporter.get_ads_details(
    #     user_access_token=fb_token,
    #     account_ids=fb_account_ids,
    #     platform=enums.Platform.FACEBOOK))

    # print_json(exporter.get_campaign_insights(
    #     user_access_token=tt_token,
    #     account_ids=tt_account_ids,
    #     platform=enums.Platform.TIKTOK,
    #     params={'sandbox': True},
    #     date_from=datetime.datetime(2023, 7, 25),
    #     date_to=datetime.datetime(2023, 8, 15)))

    # print_json(exporter.get_campaign_insights(
    #     user_access_token=fb_token,
    #     account_ids=fb_account_ids,
    #     platform=enums.Platform.FACEBOOK,
    #     date_from=datetime.datetime(2023, 1, 1),
    #     date_to=datetime.datetime(2023, 12, 30)))

    # print_json(exporter.get_adset_insights(
    #     user_access_token=tt_token,
    #     account_ids=tt_account_ids,
    #     platform=enums.Platform.TIKTOK,
    #     params={'sandbox': True},
    #     date_from=datetime.datetime(2023, 7, 25),
    #     date_to=datetime.datetime(2023, 8, 15)))

    # print_json(exporter.get_adset_insights(
    #     user_access_token=fb_token,
    #     account_ids=fb_account_ids,
    #     platform=enums.Platform.FACEBOOK,
    #     date_from=datetime.datetime(2023, 1, 1),
    #     date_to=datetime.datetime(2023, 12, 30)))

    # print_json(exporter.get_ad_insights(
    #     user_access_token=tt_token,
    #     account_ids=tt_account_ids,
    #     platform=enums.Platform.TIKTOK,
    #     params={'sandbox': True},
    #     date_from=datetime.datetime(2023, 7, 25),
    #     date_to=datetime.datetime(2023, 8, 15)))

    # print_json(exporter.get_ad_insights(
    #     user_access_token=fb_token,
    #     account_ids=fb_account_ids,
    #     platform=enums.Platform.FACEBOOK,
    #     date_from=datetime.datetime(2023, 1, 1),
    #     date_to=datetime.datetime(2023, 12, 30)))

    # print_json(exporter.get_insights_by_resource_type(
    #     user_access_token=tt_token,
    #     account_ids=tt_account_ids,
    #     platform=enums.Platform.TIKTOK,
    #     resource_type=enums.ResourceType.AD_SET,
    #     params={'sandbox': True},
    #     date_from=datetime.datetime(2023, 7, 25),
    #     date_to=datetime.datetime(2023, 8, 15)))

    # print_json(exporter.get_insights_by_resource_type(
    #     user_access_token=fb_token,
    #     account_ids=fb_account_ids,
    #     platform=enums.Platform.FACEBOOK,
    #     resource_type=enums.ResourceType.CAMPAIGN,
    #     date_from=datetime.datetime(2023, 1, 1),
    #     date_to=datetime.datetime(2023, 12, 30)))

    # QUESTIONS:
    #     - To make params in unified default value None, so when used
    #       with Facebook platform it is not needed to imput an empty
    #       params dictionary.

    # II. IMPORTER SERVICES (TikTok, Facebook, Unified)
    #
    # - REPORT:
    # Note:
    # except for comments in brackets '()' next to functionalities,
    # everything is functioning properly and no issues detected
    # there is use of labels, empty (explained at the first appearance)
    # and not supported in sandbox. As well as other descriptive labels.
    # Additionally, in all tests invalid or incorrect inputs were tested,
    # similar to invalid inputs tests for get_campaigns_details in TikTok.

    # 1. Verified and tested TIKTOK importer functionalities:
    #   - create_campaign
    #   - update_campaign
    #   - create_ad_group
    #   - update_ad_group
    #   - create_ads (Invalid identity_id)
    #   - update_ads (Invalid identity_id)
    #   - update_ads_status
    #   - create_image
    #   - update_image_name (not supported in sandbox)
    #   - create_video
    #   - update_video_name (not supported in sandbox)
    # 2. Verified and tested FACEBOOK importer functionalities:
    #   - Waiting for sandbox account to test importer functionalities
    # 3. Verified and tested UNIFIED importer functionalities (tested for TT):
    #   - create_campaign
    #   - update_campaign
    #   - create_ad_group
    #   - update_ad_group
    #   - create_ads (Invalid identity_id)

    # - TESTS:

    # TIKTOK :

    # print_json(tiktok_importer.create_campaign(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     campaign_details={
    #         "account_id": tt_account_ids[0],
    #         "campaign_name": "create_campaign_test_1",
    #         "objective_type": "TRAFFIC",
    #         "budget": 100.01,
    #         "budget_mode": "BUDGET_MODE_TOTAL"
    #     },
    #     params={'sandbox': True}
    # ))

    # print_json(tiktok_importer.update_campaign(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     campaign_id="1785827819043841",
    #     campaign_details={
    #         "account_id": "7261141933878165506",
    #         "campaign_name": "create_campaign_test_1_and_update_1",
    #         "objective_type": "TRAFFIC",
    #         "budget": 105.02,
    #         "budget_mode": "BUDGET_MODE_TOTAL"
    #     },
    #     params={'sandbox': True}
    # ))

    # print_json(tiktok_importer.create_ad_group(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     adgroup_details={
    #         "advertiser_id": tt_account_ids[0],
    #         "campaign_id": "1785827819043841",
    #         "adgroup_name": "Test_adgroup_create_1",
    #         "promotion_type": "WEBSITE",
    #         "placement_type": "PLACEMENT_TYPE_NORMAL",
    #         "placements": ["PLACEMENT_TIKTOK"],
    #         "video_download_disabled": "false",
    #         "location_ids": ["6252001"],
    #         "gender": "GENDER_UNLIMITED",
    #         "operating_systems": ["ANDROID"],
    #         "budget_mode": "BUDGET_MODE_TOTAL",
    #         "budget": 200,
    #         "schedule_type": "SCHEDULE_START_END",
    #         "schedule_end_time": "2023-12-30 00:00:00",
    #         "schedule_start_time": "2023-12-25 00:00:00",
    #         "optimization_goal": "CLICK",
    #         "bid_type": "BID_TYPE_NO_BID",
    #         "billing_event": "CPC",
    #         "pacing": "PACING_MODE_SMOOTH",
    #         "operation_status": "ENABLE"
    #     },
    #     params={'sandbox': True}
    # ))

    # print_json(tiktok_importer.update_ad_group(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     adgroup_id="1785996489115698",
    #     adgroup_details={
    #         "advertiser_id": tt_account_ids[0],
    #         "campaign_id": "1785827819043841",
    #         "adgroup_name": "Test_adgroup_create_and_update_1",
    #         "promotion_type": "WEBSITE",
    #         "placement_type": "PLACEMENT_TYPE_NORMAL",
    #         "placements": ["PLACEMENT_TIKTOK"],
    #         "video_download_disabled": "false",
    #         "location_ids": ["6252001"],
    #         "gender": "GENDER_UNLIMITED",
    #         "operating_systems": ["ANDROID"],
    #         "budget_mode": "BUDGET_MODE_TOTAL",
    #         "budget": 202,
    #         "schedule_type": "SCHEDULE_START_END",
    #         "schedule_end_time": "2023-12-30 00:00:00",
    #         "schedule_start_time": "2023-12-25 00:00:00",
    #         "optimization_goal": "CLICK",
    #         "bid_type": "BID_TYPE_NO_BID",
    #         "billing_event": "CPC",
    #         "pacing": "PACING_MODE_SMOOTH",
    #         "operation_status": "ENABLE"
    #     },
    #     params={'sandbox': True}
    # ))

    # print_json(tiktok_importer.create_ads(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     ads_details={
    #         "adgroup_id": "1785996489115698",
    #         "advertiser_id": tt_account_ids[0],
    #         "creatives": [{
    #             "ad_format": "SINGLE_VIDEO",
    #             "ad_name": "Test_ad_create_1",
    #             "ad_text": "thisisAD_TEXTandthisisAD_TEXT",
    #             "app_name": "test_create_ad_1",
    #             "avatar_icon_web_uri": "xxxxxxxx",
    #             "call_to_action": "SHOP_NOW",
    #             "catalog_id": "123",
    #             "display_name": "thisisdisplayname",
    #             "dynamic_format": "UNSET",
    #             "video_display_mode": "CUSTOM",
    #             "shopping_ads_video_package_id": "add37fc7-cc65-4b50-953a-d85f52efdf8a",
    #             "deeplink_type": "DEFERRED_DEEPLINK",
    #             "deeplink": "https://www.baidu.com",
    #             "identity_id": "11111111",
    #             "identity_type": "CUSTOMIZED_USER",
    #             "product_specific_type": "PRODUCT_SET",
    #             "product_set_id": "1234",
    #             "vertical_video_strategy": "CATALOG_VIDEOS",
    #             "shopping_ads_deeplink_type": "CUSTOM"
    #         }]
    #     },
    #     params={'sandbox': True}
    # ))

    # print_json(tiktok_importer.update_ads(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     ads_details={
    #         "adgroup_id": "1785996489115698",
    #         "advertiser_id": tt_account_ids[0],
    #         "creatives": [{
    #             "ad_format": "SINGLE_VIDEO",
    #             "ad_name": "Test_ad_create_1",
    #             "ad_text": "thisisAD_TEXTandthisisAD_TEXT",
    #             "app_name": "test_create_ad_1",
    #             "avatar_icon_web_uri": "xxxxxxxx",
    #             "call_to_action": "SHOP_NOW",
    #             "catalog_id": "123",
    #             "display_name": "thisisdisplayname",
    #             "dynamic_format": "UNSET",
    #             "video_display_mode": "CUSTOM",
    #             "shopping_ads_video_package_id": "add37fc7-cc65-4b50-953a-d85f52efdf8a",
    #             "deeplink_type": "DEFERRED_DEEPLINK",
    #             "deeplink": "https://www.baidu.com",
    #             "identity_id": "11111111",
    #             "identity_type": "CUSTOMIZED_USER",
    #             "product_specific_type": "PRODUCT_SET",
    #             "product_set_id": "1234",
    #             "vertical_video_strategy": "CATALOG_VIDEOS",
    #             "shopping_ads_deeplink_type": "CUSTOM"
    #         }]
    #     },
    #     params={'sandbox': True}
    # ))

    # print_json(tiktok_importer.update_ads_status(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     ads_status_details={
    #         "advertiser_id": tt_account_ids[0],
    #         "operation_status": "ENABLE"
    #     },
    #     params={'sandbox': True}
    # ))

    # print_json(tiktok_importer.create_image(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     image_details={
    #         "advertiser_id": tt_account_ids[0],
    #         "file_name": "Create_image_1",
    #         "upload_type": "UPLOAD_BY_URL",
    #         "image_url": "https://images.pexels.com/photos/7539498/pexels-photo-7539498.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    #     },
    #     params={'sandbox': True}
    # ))

    # print_json(tiktok_importer.update_image_name(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     image_id="ad-site-i18n-sg/202308115d0dce96a57abc294e9d9abe",
    #     image_name="Create_image_and_update_name_1",
    #     params={'sandbox': True}
    # ))

    # print_json(tiktok_importer.create_video(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     video_details={
    #         "advertiser_id": tt_account_ids[0],
    #         "file_name": "Test_create_video_1",
    #         "upload_type": "UPLOAD_BY_URL",
    #         "video_url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4"
    #     },
    #     params={'sandbox': True}
    # ))

    # print_json(tiktok_importer.update_video_name(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     video_id="v07033cf0000bvcet7lq768v0krodaug",
    #     video_name="Test_create_video_and_update_name_1",
    #     params={'sandbox': True}
    # ))

    # FACEBOOK :

    # UNIFIED :

    # print_json(importer.create_campaign(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     platform=enums.Platform.TIKTOK,
    #     campaign_details={
    #         "account_id": tt_account_ids[0],
    #         "campaign_name": "create_campaign_test_2",
    #         "objective_type": "TRAFFIC",
    #         "budget": 100.01,
    #         "budget_mode": "BUDGET_MODE_TOTAL"
    #     },
    #     params={'sandbox': True}
    # ))

    # print_json(importer.update_campaign(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     platform=enums.Platform.TIKTOK,
    #     campaign_id="1786000567586833",
    #     campaign_details={
    #         "account_id": "7261141933878165506",
    #         "campaign_name": "create_campaign_test_2_and_update_2",
    #         "objective_type": "TRAFFIC",
    #         "budget": 105.02,
    #         "budget_mode": "BUDGET_MODE_TOTAL"
    #     },
    #     params={'sandbox': True}
    # ))

    # print_json(importer.create_ad_set(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     platform=enums.Platform.TIKTOK,
    #     adset_details={
    #         "advertiser_id": tt_account_ids[0],
    #         "campaign_id": "1786000567586833",
    #         "adgroup_name": "Test_adgroup_create_2",
    #         "promotion_type": "WEBSITE",
    #         "placement_type": "PLACEMENT_TYPE_NORMAL",
    #         "placements": ["PLACEMENT_TIKTOK"],
    #         "video_download_disabled": "false",
    #         "location_ids": ["6252001"],
    #         "gender": "GENDER_UNLIMITED",
    #         "operating_systems": ["ANDROID"],
    #         "budget_mode": "BUDGET_MODE_TOTAL",
    #         "budget": 200,
    #         "schedule_type": "SCHEDULE_START_END",
    #         "schedule_end_time": "2023-12-30 00:00:00",
    #         "schedule_start_time": "2023-12-25 00:00:00",
    #         "optimization_goal": "CLICK",
    #         "bid_type": "BID_TYPE_NO_BID",
    #         "billing_event": "CPC",
    #         "pacing": "PACING_MODE_SMOOTH",
    #         "operation_status": "ENABLE"
    #     },
    #     params={'sandbox': True}
    # ))

    # print_json(importer.update_ad_set(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     platform=enums.Platform.TIKTOK,
    #     adset_id="1786000780176417",
    #     adset_details={
    #         "advertiser_id": tt_account_ids[0],
    #         "campaign_id": "1786000567586833",
    #         "adgroup_name": "Test_adgroup_create_and_update_2",
    #         "promotion_type": "WEBSITE",
    #         "placement_type": "PLACEMENT_TYPE_NORMAL",
    #         "placements": ["PLACEMENT_TIKTOK"],
    #         "video_download_disabled": "false",
    #         "location_ids": ["6252001"],
    #         "gender": "GENDER_UNLIMITED",
    #         "operating_systems": ["ANDROID"],
    #         "budget_mode": "BUDGET_MODE_TOTAL",
    #         "budget": 202,
    #         "schedule_type": "SCHEDULE_START_END",
    #         "schedule_end_time": "2023-12-30 00:00:00",
    #         "schedule_start_time": "2023-12-25 00:00:00",
    #         "optimization_goal": "CLICK",
    #         "bid_type": "BID_TYPE_NO_BID",
    #         "billing_event": "CPC",
    #         "pacing": "PACING_MODE_SMOOTH",
    #         "operation_status": "ENABLE"
    #     },
    #     params={'sandbox': True}
    # ))

    # print_json(importer.create_ads(
    #     user_access_token=tt_token,
    #     ad_account_id=tt_account_ids[0],
    #     platform=enums.Platform.TIKTOK,
    #     ads_details={
    #         "adgroup_id": "1786000780176417",
    #         "advertiser_id": tt_account_ids[0],
    #         "creatives": [{
    #             "ad_format": "SINGLE_VIDEO",
    #             "ad_name": "Test_ad_create_1",
    #             "ad_text": "thisisAD_TEXTandthisisAD_TEXT",
    #             "app_name": "test_create_ad_1",
    #             "avatar_icon_web_uri": "xxxxxxxx",
    #             "call_to_action": "SHOP_NOW",
    #             "catalog_id": "123",
    #             "display_name": "thisisdisplayname",
    #             "dynamic_format": "UNSET",
    #             "video_display_mode": "CUSTOM",
    #             "shopping_ads_video_package_id": "add37fc7-cc65-4b50-953a-d85f52efdf8a",
    #             "deeplink_type": "DEFERRED_DEEPLINK",
    #             "deeplink": "https://www.baidu.com",
    #             "identity_id": "11111111",
    #             "identity_type": "CUSTOMIZED_USER",
    #             "product_specific_type": "PRODUCT_SET",
    #             "product_set_id": "1234",
    #             "vertical_video_strategy": "CATALOG_VIDEOS",
    #             "shopping_ads_deeplink_type": "CUSTOM"
    #         }]
    #     },
    #     params={'sandbox': True}
    # ))


if __name__ == "__main__":
    main()
