import logging
import typing

from ads_manager import enums, exceptions, utils
from ads_manager.integrations.clients import exceptions as client_exceptions
from ads_manager.integrations.clients import factory

logger = logging.getLogger(__name__)


def create_campaign(
    user_access_token: str,
    platform: enums.Platform,
    ad_account_id: str,
    campaign_details: typing.Dict,
    params: typing.Dict = None,
) -> str:
    try:
        campaign_id = factory.Factory.create(
            platform=platform, user_access_token=user_access_token, params=params
        ).create_campaign(ad_account_id=ad_account_id, campaign_details=campaign_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Created {} campaign (id={})".format(platform.value, campaign_id))

    return campaign_id


def update_campaign(
    user_access_token: str,
    platform: enums.Platform,
    ad_account_id: str,
    campaign_id: str,
    campaign_details: typing.Dict,
    params: typing.Dict = None,
) -> bool:
    try:
        campaign_updated = factory.Factory.create(
            platform=platform, user_access_token=user_access_token, params=params
        ).update_campaign(
            ad_account_id=ad_account_id,
            campaign_id=campaign_id,
            campaign_details=campaign_details,
        )
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Updated {} campaign (id={}, success={})".format(platform.value, campaign_id, campaign_updated))

    return campaign_updated


def create_ad_set(
    user_access_token: str,
    platform: enums.Platform,
    ad_account_id: str,
    adset_details: typing.Dict,
    params: typing.Dict = None,
) -> str:
    try:
        adset_id = factory.Factory.create(
            platform=platform, user_access_token=user_access_token, params=params
        ).create_adset(ad_account_id=ad_account_id, adset_details=adset_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Created {} adset (id={})".format(platform.value, adset_id))

    return adset_id


def update_ad_set(
    user_access_token: str,
    platform: enums.Platform,
    ad_account_id: str,
    adset_id: str,
    adset_details: typing.Dict,
    params: typing.Dict = None,
) -> bool:
    try:
        adset_updated = factory.Factory.create(
            platform=platform, user_access_token=user_access_token, params=params
        ).update_adset(
            ad_account_id=ad_account_id,
            adset_id=adset_id,
            adset_details=adset_details,
        )
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Updated {} adset (id={}, success={})".format(platform.value, adset_id, adset_updated))

    return adset_updated


def create_ads(
    user_access_token: str,
    platform: enums.Platform,
    ad_account_id: str,
    ads_details: typing.Dict,
    params: typing.Dict = None,
) -> typing.List[str]:
    try:
        ad_ids = factory.Factory.create(
            platform=platform, user_access_token=user_access_token, params=params
        ).create_ads(ad_account_id=ad_account_id, ads_details=ads_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Created {} ads (ids={})".format(platform.value, ad_ids))

    return ad_ids
