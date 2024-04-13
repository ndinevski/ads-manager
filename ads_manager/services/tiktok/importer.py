import logging
import typing

from ads_manager import enums, exceptions, utils
from ads_manager.integrations.clients import exceptions as client_exceptions
from ads_manager.integrations.clients import factory

logger = logging.getLogger(__name__)


def create_campaign(
    user_access_token: str, ad_account_id: str, campaign_details: typing.Dict, params: typing.Dict
) -> str:
    try:
        campaign_id = factory.Factory.create(
            platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
        ).create_campaign(ad_account_id=ad_account_id, campaign_details=campaign_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Created tiktok campaign (id={})".format(campaign_id))

    return campaign_id


def update_campaign(
    user_access_token: str, ad_account_id: str, campaign_id: str, campaign_details: typing.Dict, params: typing.Dict
) -> bool:
    try:
        campaign_updated = factory.Factory.create(
            platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
        ).update_campaign(
            ad_account_id=ad_account_id,
            campaign_id=campaign_id,
            campaign_details=campaign_details,
        )
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Updated tiktok campaign (id={}, success={})".format(campaign_id, campaign_updated))

    return campaign_updated


def create_ad_group(
    user_access_token: str, ad_account_id: str, adgroup_details: typing.Dict, params: typing.Dict
) -> str:
    try:
        adgroup_id = factory.Factory.create(
            platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
        ).create_adset(ad_account_id=ad_account_id, adset_details=adgroup_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Created tiktok adgroup (id={})".format(adgroup_id))

    return adgroup_id


def update_ad_group(
    user_access_token: str, ad_account_id: str, adgroup_id: str, adgroup_details: typing.Dict, params: typing.Dict
) -> bool:
    try:
        adgroup_updated = factory.Factory.create(
            platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
        ).update_adset(
            ad_account_id=ad_account_id,
            adset_id=adgroup_id,
            adset_details=adgroup_details,
        )
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Updated tiktok adgroup (id={}, success={})".format(adgroup_id, adgroup_updated))

    return adgroup_updated


def create_ads(
    user_access_token: str, ad_account_id: str, ads_details: typing.Dict, params: typing.Dict
) -> typing.List[str]:
    try:
        ad_ids = factory.Factory.create(
            platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
        ).create_ads(ad_account_id=ad_account_id, ads_details=ads_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Created tiktok ads (ids={})".format(ad_ids))

    return ad_ids


def update_ads(
    user_access_token: str, ad_account_id: str, adgroup_id: str, ad_details: typing.Dict, params: typing.Dict
) -> bool:
    try:
        ad_updated = factory.Factory.create(
            platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
        ).update_ads(ad_account_id=ad_account_id, adgroup_id=adgroup_id, ad_details=ad_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Updated tiktok ads (success={})".format(ad_updated))

    return ad_updated


def update_ads_status(
    user_access_token: str, ad_account_id: str, ads_status_details: typing.Dict, params: typing.Dict
) -> bool:
    try:
        updated_ads_status = factory.Factory.create(
            platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
        ).update_ads_status(ad_account_id=ad_account_id, ads_status_details=ads_status_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Updated tiktok ad statuses (success={})".format(updated_ads_status))

    return updated_ads_status


def create_image(user_access_token: str, ad_account_id: str, image_details: typing.Dict, params: typing.Dict) -> str:
    try:
        image_id = factory.Factory.create(
            platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
        ).create_image(ad_account_id=ad_account_id, image_details=image_details)
    except client_exceptions.ClientError as e:
        raise exceptions.AdAssetsException(utils.get_exception_message(exception=e))

    logger.warning("Created image (id={})".format(image_id))

    return image_id


def update_image_name(
    user_access_token: str, ad_account_id: str, image_id: str, image_name: str, params: typing.Dict
) -> bool:
    try:
        image_updated = factory.Factory.create(
            platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
        ).update_image_name(
            ad_account_id=ad_account_id,
            image_id=image_id,
            image_name=image_name,
        )
    except client_exceptions.ClientError as e:
        raise exceptions.AdAssetsException(utils.get_exception_message(exception=e))

    logger.warning("Updated image name (id={}, success={})".format(image_id, image_updated))

    return image_updated


def create_video(user_access_token: str, ad_account_id: str, video_details: typing.Dict, params: typing.Dict) -> str:
    try:
        video_id = factory.Factory.create(
            platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
        ).create_video(ad_account_id=ad_account_id, video_details=video_details)
    except client_exceptions.ClientError as e:
        raise exceptions.AdAssetsException(utils.get_exception_message(exception=e))

    logger.warning("Created video (id={})".format(video_id))

    return video_id


def update_video_name(
    user_access_token: str, ad_account_id: str, video_id: str, video_name: str, params: typing.Dict
) -> bool:
    try:
        video_updated = factory.Factory.create(
            platform=enums.Platform.TIKTOK, user_access_token=user_access_token, params=params
        ).update_video_name(
            ad_account_id=ad_account_id,
            video_id=video_id,
            video_name=video_name,
        )
    except client_exceptions.ClientError as e:
        raise exceptions.AdAssetsException(utils.get_exception_message(exception=e))

    logger.warning("Updated video name (id={}, success={})".format(video_id, video_updated))

    return video_updated
