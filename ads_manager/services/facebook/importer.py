import logging
import typing

from ads_manager import enums, exceptions, utils
from ads_manager.integrations.clients import exceptions as client_exceptions
from ads_manager.integrations.clients import factory

logger = logging.getLogger(__name__)


def create_campaign(
    user_access_token: str,
    ad_account_id: str,
    campaign_details: typing.Dict,
) -> str:
    try:
        campaign_id = factory.Factory.create(
            platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
        ).create_campaign(ad_account_id=ad_account_id, campaign_details=campaign_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Created facebook campaign (id={})".format(campaign_id))

    return campaign_id


def update_campaign(
    user_access_token: str,
    ad_account_id: str,
    campaign_id: str,
    campaign_details: typing.Dict,
) -> bool:
    try:
        campaign_updated = factory.Factory.create(
            platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
        ).update_campaign(ad_account_id=ad_account_id, campaign_id=campaign_id, campaign_details=campaign_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Updated facebook campaign (id={}, success={})".format(campaign_id, campaign_updated))

    return campaign_updated


def create_ad_set(
    user_access_token: str,
    ad_account_id: str,
    adset_details: typing.Dict,
) -> str:
    try:
        adset_id = factory.Factory.create(
            platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
        ).create_adset(ad_account_id=ad_account_id, adset_details=adset_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Created facebook adset (id={})".format(adset_id))

    return adset_id


def update_ad_set(
    user_access_token: str,
    ad_account_id: str,
    adset_id: str,
    adset_details: typing.Dict,
) -> bool:
    try:
        adset_updated = factory.Factory.create(
            platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
        ).update_adset(ad_account_id=ad_account_id, adset_id=adset_id, adset_details=adset_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Updated facebook adset (id={}, success={})".format(adset_id, adset_updated))

    return adset_updated


def create_ad_creative(
    user_access_token: str,
    ad_account_id: str,
    adcreative_details: typing.Dict,
) -> str:
    try:
        adcreative_id = factory.Factory.create(
            platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
        ).create_adcreative(ad_account_id=ad_account_id, adcreative_details=adcreative_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Created facebook adcreative (id={})".format(adcreative_id))

    return adcreative_id


def update_ad_creative(
    user_access_token: str,
    adcreative_id: str,
    adcreative_details: typing.Dict,
) -> bool:
    try:
        adcreative_updated = factory.Factory.create(
            platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
        ).update_adcreative(adcreative_id=adcreative_id, adcreative_details=adcreative_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Updated facebook adcreative (id={}, success={})".format(adcreative_id, adcreative_updated))

    return adcreative_updated


def create_ads(
    user_access_token: str,
    ad_account_id: str,
    ads_details: typing.Dict,
) -> typing.List[str]:
    try:
        ad_ids = factory.Factory.create(
            platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
        ).create_ads(ad_account_id=ad_account_id, ads_details=ads_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Created facebook ads (ids={})".format(ad_ids))

    return ad_ids


def create_ad(
    user_access_token: str,
    ad_account_id: str,
    ad_details: typing.Dict,
) -> str:
    try:
        ad_id = factory.Factory.create(platform=enums.Platform.FACEBOOK, user_access_token=user_access_token).create_ad(
            ad_account_id=ad_account_id, ad_details=ad_details
        )
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Created facebook ad (id={})".format(ad_id))

    return ad_id


def set_ad_status(
    user_access_token: str,
    ad_id: str,
    ad_details: typing.Dict,
) -> bool:
    try:
        ad_updated = factory.Factory.create(
            platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
        ).update_ad(ad_id=ad_id, ad_details=ad_details)
    except client_exceptions.ClientError as e:
        raise exceptions.ActionException(utils.get_exception_message(exception=e))

    logger.warning("Updated facebook ad (id={}, success={})".format(ad_id, ad_updated))

    return ad_updated
