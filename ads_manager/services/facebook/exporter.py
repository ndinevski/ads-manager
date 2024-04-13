import datetime
import json
import logging
import typing
from dataclasses import asdict

from ads_manager import enums, exceptions, utils
from ads_manager.integrations.clients import exceptions as client_exceptions
from ads_manager.integrations.clients import factory

logger = logging.getLogger(__name__)


def get_account_ids(user_access_token: str) -> typing.List[str]:
    try:
        ad_accounts = factory.Factory.create(
            platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
        ).get_account_ids()

        logger.warning("Fetched {} facebook ad account ids".format(len(ad_accounts)))

        ad_account_ids = [ad_account.account_id for ad_account in ad_accounts]

        return ad_account_ids

    except client_exceptions.ClientError as e:
        raise exceptions.ImporterException(utils.get_exception_message(exception=e))


def get_campaigns_details(user_access_token: str, account_ids: typing.List[str]) -> str:
    campaigns_details = []

    facebook_integration_client = factory.Factory.create(
        platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
    )

    logger.warning("Fetched {} facebook ad account ids".format(len(account_ids)))

    for account_id in account_ids:
        try:
            campaign_details = facebook_integration_client.get_account_campaigns_details(ad_account_id=account_id)
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        campaign_details = [asdict(campaigns_detail) for campaigns_detail in campaign_details]
        campaigns_details.extend(campaign_details)

    logger.warning("Fetched {} facebook campaigns".format(len(campaigns_details)))

    return json.dumps(campaigns_details, indent=4)


def get_adsets_details(user_access_token: str, account_ids: typing.List[str]) -> str:
    adsets_details = []

    facebook_integration_client = factory.Factory.create(
        platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
    )

    logger.warning("Fetched {} facebook ad account ids".format(len(account_ids)))

    for account_id in account_ids:
        try:
            adset_details = facebook_integration_client.get_account_adsets_details(ad_account_id=account_id)
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        adset_details = [asdict(adset_detail) for adset_detail in adset_details]
        adsets_details.extend(adset_details)

    logger.warning("Fetched {} facebook adsets".format(len(adsets_details)))

    return json.dumps(adsets_details, indent=4)


def get_ads_details(user_access_token: str, account_ids: typing.List[str]) -> str:
    ads_details = []

    facebook_integration_client = factory.Factory.create(
        platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
    )

    logger.warning("Fetched {} facebook ad account ids".format(len(account_ids)))

    for account_id in account_ids:
        try:
            ad_details = facebook_integration_client.get_account_ads_details(ad_account_id=account_id)
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        ad_details = [asdict(ad_detail) for ad_detail in ad_details]
        ads_details.extend(ad_details)

    logger.warning("Fetched {} facebook adsets".format(len(ads_details)))

    return json.dumps(ads_details, indent=4)


def get_campaign_insights(
    user_access_token: str,
    account_ids: typing.List[str],
    date_from: typing.Optional[datetime.datetime],
    date_to: typing.Optional[datetime.datetime],
) -> str:
    campaigns_performance = []

    facebook_integration_client = factory.Factory.create(
        platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
    )

    logger.warning("Fetched {} facebook ad account ids".format(len(account_ids)))

    for account_id in account_ids:
        try:
            campaign_performances = facebook_integration_client.get_insights(
                ad_account_id=account_id,
                resource_type=enums.ResourceType.CAMPAIGN,
                from_datetime=date_from,
                to_datetime=date_to,
            )
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        campaign_performances = [asdict(campaign_performance) for campaign_performance in campaign_performances]
        campaigns_performance.extend(campaign_performances)

    return json.dumps(campaigns_performance, indent=4)


def get_adset_insights(
    user_access_token: str,
    account_ids: typing.List[str],
    date_from: typing.Optional[datetime.datetime],
    date_to: typing.Optional[datetime.datetime],
) -> str:
    adsets_performance = []

    facebook_integration_client = factory.Factory.create(
        platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
    )

    logger.warning("Fetched {} facebook ad account ids".format(len(account_ids)))

    for account_id in account_ids:
        try:
            adset_performances = facebook_integration_client.get_insights(
                ad_account_id=account_id,
                resource_type=enums.ResourceType.AD_SET,
                from_datetime=date_from,
                to_datetime=date_to,
            )
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        adset_performances = [asdict(adset_performance) for adset_performance in adset_performances]
        adsets_performance.extend(adset_performances)

    return json.dumps(adsets_performance, indent=4)


def get_ad_insights(
    user_access_token: str,
    account_ids: typing.List[str],
    date_from: typing.Optional[datetime.datetime],
    date_to: typing.Optional[datetime.datetime],
) -> str:
    ads_performance = []

    facebook_integration_client = factory.Factory.create(
        platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
    )

    logger.warning("Fetched {} facebook ad account ids".format(len(account_ids)))

    for account_id in account_ids:
        try:
            ad_performances = facebook_integration_client.get_insights(
                ad_account_id=account_id,
                resource_type=enums.ResourceType.AD,
                from_datetime=date_from,
                to_datetime=date_to,
            )
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        ad_performances = [asdict(ad_performance) for ad_performance in ad_performances]
        ads_performance.extend(ad_performances)

    return json.dumps(ads_performance, indent=4)


def get_ad_creatives_list(user_access_token: str, account_ids: typing.List[str]) -> typing.List[str]:
    return [
        ad_creative["id"]
        for ad_creative in _get_all_ad_creatives(user_access_token=user_access_token, account_ids=account_ids)
    ]


def get_ad_creatives(user_access_token: str, account_ids: typing.List[str], asset_ids: typing.List[str]) -> str:
    ad_creatives = (
        _get_all_ad_creatives(user_access_token=user_access_token, account_ids=account_ids)
        if not asset_ids
        else _get_ad_creatives(user_access_token=user_access_token, ad_creative_ids=asset_ids)
    )

    return json.dumps(ad_creatives, indent=4)


def _get_ad_creatives(user_access_token: str, ad_creative_ids: typing.List[str]) -> typing.List[typing.Dict]:
    ad_creatives = []

    for ad_creative_id in ad_creative_ids:
        try:
            ad_creative = factory.Factory.create(
                platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
            ).get_ad_creative(ad_creative_id=ad_creative_id)
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        ad_creatives.append(asdict(ad_creative))

    return ad_creatives


def _get_all_ad_creatives(user_access_token: str, account_ids: typing.List[str]) -> typing.List[typing.Dict]:
    facebook_integration_client = factory.Factory.create(
        platform=enums.Platform.FACEBOOK, user_access_token=user_access_token
    )

    all_ad_creatives = []

    logger.warning("Fetched {} facebook ad account ids".format(len(account_ids)))

    for account_id in account_ids:
        try:
            ad_creatives = facebook_integration_client.get_account_ad_creatives(ad_account_id=account_id)
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        ad_creatives = [asdict(ad_creative) for ad_creative in ad_creatives]
        all_ad_creatives.extend(ad_creatives)

    return all_ad_creatives
