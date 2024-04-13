class TikTokAPIClientError(Exception):
    pass


class BadResponseCodeError(TikTokAPIClientError):
    def __init__(self, message: str, code: int) -> None:
        TikTokAPIClientError.__init__(self)
        self.message = message
        self.code = code


class BadPayloadCodeError(TikTokAPIClientError):
    def __init__(self, message: str, code: int, payload_code: int) -> None:
        TikTokAPIClientError.__init__(self)
        self.message = message
        self.code = code
        self.payload_code = payload_code
