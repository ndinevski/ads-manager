class FacebookAPIClientError(Exception):
    pass


class BadResponseCodeError(FacebookAPIClientError):
    def __init__(self, message: str, code: int) -> None:
        FacebookAPIClientError.__init__(self)
        self.message = message
        self.code = code
