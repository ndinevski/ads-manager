class ClientError(Exception):
    pass


class ClientProviderError(ClientError):
    pass


class ResponseDataNotValidError(ClientError):
    pass
