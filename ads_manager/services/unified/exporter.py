import datetime
import json
import logging
import typing
from dataclasses import asdict

from ads_manager import enums, exceptions, utils
from ads_manager.integrations.clients import exceptions as client_exceptions
from ads_manager.integrations.clients import factory

logger = logging.getLogger(__name__)


def get_account_ids(user_access_token: str, platform: enums.Platform, params: typing.Dict = None) -> typing.List[str]:
    try:
        ad_accounts = factory.Factory.create(
            platform=platform, user_access_token=user_access_token, params=params
        ).get_account_ids()

        logger.warning("Fetched {} {} ad account ids".format(len(ad_accounts), platform.value))

        ad_account_ids = [ad_account.account_id for ad_account in ad_accounts]

        return ad_account_ids

    except client_exceptions.ClientError as e:
        raise exceptions.ImporterException(utils.get_exception_message(exception=e))


def get_campaigns_details(
    user_access_token: str, platform: enums.Platform, account_ids: typing.List[str], params: typing.Dict = None
) -> str:
    campaigns_details = []

    integration_client = factory.Factory.create(platform=platform, user_access_token=user_access_token, params=params)

    logger.warning("Fetched {} {} ad account ids".format(len(account_ids), platform.value))

    for account_id in account_ids:
        try:
            campaign_details = integration_client.get_account_campaigns_details(ad_account_id=account_id)
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        campaign_details = [asdict(campaigns_detail) for campaigns_detail in campaign_details]
        campaigns_details.extend(campaign_details)

    logger.warning("Fetched {} {} campaigns".format(len(campaigns_details), platform.value))

    return json.dumps(campaigns_details, indent=4)


def get_adsets_details(
    user_access_token: str, platform: enums.Platform, account_ids: typing.List[str], params: typing.Dict = None
) -> str:
    adsets_details = []

    integration_client = factory.Factory.create(platform=platform, user_access_token=user_access_token, params=params)

    logger.warning("Fetched {} {} ad account ids".format(len(account_ids), platform.value))

    for account_id in account_ids:
        try:
            adset_details = integration_client.get_account_adsets_details(ad_account_id=account_id)
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        adset_details = [asdict(adset_detail) for adset_detail in adset_details]
        adsets_details.extend(adset_details)

    logger.warning("Fetched {} {} adsets".format(len(adsets_details), platform.value))

    return json.dumps(adsets_details, indent=4)


def get_ads_details(
    user_access_token: str, platform: enums.Platform, account_ids: typing.List[str], params: typing.Dict = None
) -> str:
    ads_details = []

    integration_client = factory.Factory.create(platform=platform, user_access_token=user_access_token, params=params)

    logger.warning("Fetched {} {} ad account ids".format(len(account_ids), platform.value))

    for account_id in account_ids:
        try:
            ad_details = integration_client.get_account_ads_details(ad_account_id=account_id)
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        ad_details = [asdict(ad_detail) for ad_detail in ad_details]
        ads_details.extend(ad_details)

    logger.warning("Fetched {} {} adsets".format(len(ads_details), platform.value))

    return json.dumps(ads_details, indent=4)


def get_insights_by_resource_type(
    user_access_token: str,
    platform: enums.Platform,
    account_ids: typing.List[str],
    resource_type: enums.ResourceType,
    date_from: typing.Optional[datetime.datetime],
    date_to: typing.Optional[datetime.datetime],
    params: typing.Dict = None,
) -> str:
    resources_performance = []

    integration_client = factory.Factory.create(platform=platform, user_access_token=user_access_token, params=params)

    logger.warning("Fetched {} {} ad account ids".format(len(account_ids), platform.value))

    for account_id in account_ids:
        try:
            resource_performances = integration_client.get_insights(
                ad_account_id=account_id,
                resource_type=resource_type,
                from_datetime=date_from,
                to_datetime=date_to,
            )
        except client_exceptions.ClientError as e:
            raise exceptions.ImporterException(utils.get_exception_message(exception=e))

        resource_performances = [asdict(resource_performance) for resource_performance in resource_performances]
        resources_performance.extend(resource_performances)

    return json.dumps(resources_performance, indent=4)


def get_campaign_insights(
    user_access_token: str,
    platform: enums.Platform,
    account_ids: typing.List[str],
    date_from: typing.Optional[datetime.datetime],
    date_to: typing.Optional[datetime.datetime],
    params: typing.Dict = None,
) -> str:
    campaigns_performance = []

    integration_client = factory.Factory.create(platform=platform, user_access_token=user_access_token, params=params)

    logger.warning("Fetched {} {} ad account ids".format(len(account_ids), platform.value))

    for account_id in account_ids:
        try:
            campaign_performances = integration_client.get_insights(
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
    platform: enums.Platform,
    account_ids: typing.List[str],
    date_from: typing.Optional[datetime.datetime],
    date_to: typing.Optional[datetime.datetime],
    params: typing.Dict = None,
) -> str:
    adsets_performance = []

    integration_client = factory.Factory.create(platform=platform, user_access_token=user_access_token, params=params)

    logger.warning("Fetched {} {} ad account ids".format(len(account_ids), platform.value))

    for account_id in account_ids:
        try:
            adset_performances = integration_client.get_insights(
                ad_account_id=account_id,
                resource_type=enums.ResourceType.AD_SET
                if platform == enums.Platform.FACEBOOK
                else enums.TiktokResourceType.AD_GROUP,
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
    platform: enums.Platform,
    account_ids: typing.List[str],
    date_from: typing.Optional[datetime.datetime],
    date_to: typing.Optional[datetime.datetime],
    params: typing.Dict = None,
) -> str:
    ads_performance = []

    integration_client = factory.Factory.create(platform=platform, user_access_token=user_access_token, params=params)

    logger.warning("Fetched {} {} ad account ids".format(len(account_ids), platform.value))

    for account_id in account_ids:
        try:
            ad_performances = integration_client.get_insights(
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
