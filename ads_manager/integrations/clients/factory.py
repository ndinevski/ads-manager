import logging
import typing

from ads_manager import enums, exceptions
from ads_manager.integrations.clients import exceptions as client_exceptions
from ads_manager.integrations.clients.facebook import client as facebook_client
from ads_manager.integrations.clients.tiktok import client as tiktok_client

logger = logging.getLogger(__name__)


class Factory(object):
    _PLATFORM_CLIENTS_IMPLEMENTATION_MAP = {
        enums.Platform.FACEBOOK: facebook_client.FacebookClient,
        enums.Platform.TIKTOK: tiktok_client.TiktokClient,
    }

    _LOG_PREFIX = "[PLATFORM-CLIENT-FACTORY]"

    @classmethod
    def create(
        cls, platform: enums.Platform, user_access_token: str, params: typing.Optional[typing.Dict] = None
    ) -> typing.Union[facebook_client.FacebookClient, tiktok_client.TiktokClient]:
        if platform not in cls._PLATFORM_CLIENTS_IMPLEMENTATION_MAP:
            msg = "Platform {} is not supported".format(platform.name)
            logger.error("{} {}.".format(cls._LOG_PREFIX, msg))
            raise client_exceptions.ClientProviderError()

        return cls._PLATFORM_CLIENTS_IMPLEMENTATION_MAP[platform](user_access_token=user_access_token, params=params)
