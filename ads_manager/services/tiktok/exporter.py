import datetime
import json
import logging
import typing
from dataclasses import asdict

from ads_manager import enums, exceptions, utils
from ads_manager.integrations.clients import exceptions as client_exceptions
from ads_manager.integrations.clients import factory

logger = logging.getLogger(__name__)


def get_account_ids(user_access_token: str, params: typing.Dict) -> typing.List[str]:
    try:
        ad_accounts = factory.Factory.create(
            platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
        ).get_account_ids()

        logger.warning("Fetched {} tiktok advertiser ids".format(len(ad_accounts)))

        ad_account_ids = [ad_account.account_id for ad_account in ad_accounts]

        return ad_account_ids
    except client_exceptions.ClientError as e:
        raise exceptions.ImporterException(utils.get_exception_message(exception=e))


def get_campaigns_details(user_access_token: str, account_ids: typing.List[str], params: typing.Dict) -> str:
    campaigns_details = []

    tiktok_integration_client = factory.Factory.create(
        platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
    )

    logger.warning("Fetched {} tiktok advertiser ids".format(len(account_ids)))

    for account_id in account_ids:
        try:
            campaign_details = tiktok_integration_client.get_account_campaigns_details(ad_account_id=account_id)
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        campaign_details = [asdict(campaigns_detail) for campaigns_detail in campaign_details]
        campaigns_details.extend(campaign_details)

    logger.warning("Fetched {} tiktok campaigns".format(len(campaigns_details)))

    return json.dumps(campaigns_details, indent=4)


def get_adgroups_details(user_access_token: str, account_ids: typing.List[str], params: typing.Dict) -> str:
    adgroups_details = []

    tiktok_integration_client = factory.Factory.create(
        platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
    )

    logger.warning("Fetched {} tiktok advertiser ids".format(len(account_ids)))

    for account_id in account_ids:
        try:
            adgroup_details = tiktok_integration_client.get_account_adsets_details(ad_account_id=account_id)
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        adgroup_details = [asdict(adgroup_detail) for adgroup_detail in adgroup_details]
        adgroups_details.extend(adgroup_details)

    logger.warning("Fetched {} tiktok adgroups".format(len(adgroups_details)))

    return json.dumps(adgroups_details, indent=4)


def get_ads_details(user_access_token: str, account_ids: typing.List[str], params: typing.Dict) -> str:
    ads_details = []

    tiktok_integration_client = factory.Factory.create(
        platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
    )

    logger.warning("Fetched {} tiktok advertiser ids".format(len(account_ids)))

    for account_id in account_ids:
        try:
            ad_details = tiktok_integration_client.get_account_ads_details(ad_account_id=account_id)
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        ad_details = [asdict(ad_detail) for ad_detail in ad_details]
        ads_details.extend(ad_details)

    logger.warning("Fetched {} tiktok ads".format(len(ads_details)))

    return json.dumps(ads_details, indent=4)


def get_campaign_insights(
    user_access_token: str,
    account_ids: typing.List[str],
    date_from: datetime.datetime,
    date_to: datetime.datetime,
    params: typing.Dict,
) -> str:
    campaigns_insights = []

    tiktok_integration_client = factory.Factory.create(
        platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
    )

    logger.warning("Fetched {} tiktok advertiser ids".format(len(account_ids)))

    for account_id in account_ids:
        try:
            campaign_insights = tiktok_integration_client.get_insights(
                ad_account_id=account_id,
                resource_type=enums.ResourceType.CAMPAIGN,
                from_datetime=date_from,
                to_datetime=date_to,
            )
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        campaign_insights = [asdict(campaign_insight) for campaign_insight in campaign_insights]
        campaigns_insights.extend(campaign_insights)

    return json.dumps(campaigns_insights, indent=4)


def get_adgroup_insights(
    user_access_token: str,
    account_ids: typing.List[str],
    date_from: datetime.datetime,
    date_to: datetime.datetime,
    params: typing.Dict,
) -> str:
    adgroups_insights = []

    tiktok_integration_client = factory.Factory.create(
        platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
    )

    logger.warning("Fetched {} tiktok advertiser ids".format(len(account_ids)))

    for account_id in account_ids:
        try:
            adgroup_insights = tiktok_integration_client.get_insights(
                ad_account_id=account_id,
                resource_type=enums.TiktokResourceType.AD_GROUP,
                from_datetime=date_from,
                to_datetime=date_to,
            )
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        adgroup_insights = [asdict(adgroup_insight) for adgroup_insight in adgroup_insights]
        adgroups_insights.extend(adgroup_insights)

    return json.dumps(adgroups_insights, indent=4)


def get_ad_insights(
    user_access_token: str,
    account_ids: typing.List[str],
    date_from: datetime.datetime,
    date_to: datetime.datetime,
    params: typing.Dict,
) -> str:
    ads_insights = []

    tiktok_integration_client = factory.Factory.create(
        platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
    )

    logger.warning("Fetched {} tiktok advertiser ids".format(len(account_ids)))

    for account_id in account_ids:
        try:
            ad_insights = tiktok_integration_client.get_insights(
                ad_account_id=account_id,
                resource_type=enums.ResourceType.AD,
                from_datetime=date_from,
                to_datetime=date_to,
            )
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        ad_insights = [asdict(ad_insight) for ad_insight in ad_insights]
        ads_insights.extend(ad_insights)

    return json.dumps(ads_insights, indent=4)


def get_images_details(
    user_access_token: str,
    advertiser_id: str,
    image_ids: typing.List[str],
) -> str:
    try:
        images_info = factory.Factory.create(
            platform=enums.Platform.TIKTOK, user_access_token=user_access_token
        ).get_images_info(
            ad_account_id=advertiser_id,
            image_ids=image_ids,
        )
    except client_exceptions.ClientError as e:
        raise exceptions.AdAssetsException(utils.get_exception_message(exception=e))

    logger.warning(
        "Got info for images (id={}, image_ids={}, images_info={})".format(advertiser_id, image_ids, images_info)
    )

    images_info = [asdict(image_info) for image_info in images_info]

    return json.dumps(images_info, indent=4)


def get_videos_details(
    user_access_token: str,
    advertiser_id: str,
    video_ids: typing.List[str],
) -> str:
    try:
        videos_info = factory.Factory.create(
            platform=enums.Platform.TIKTOK, user_access_token=user_access_token
        ).get_videos_info(
            ad_account_id=advertiser_id,
            video_ids=video_ids,
        )
    except client_exceptions.ClientError as e:
        raise exceptions.AdAssetsException(utils.get_exception_message(exception=e))

    logger.warning(
        "Got info for videos (id={}, video_ids={}, videos_info={})".format(advertiser_id, video_ids, videos_info)
    )

    videos_info = [asdict(video_info) for video_info in videos_info]

    return json.dumps(videos_info, indent=4)
