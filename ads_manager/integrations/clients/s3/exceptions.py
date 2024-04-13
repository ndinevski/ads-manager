class S3UploaderError(Exception):
    pass


class S3PathIsNotValidError(S3UploaderError):
    pass


class S3ClientError(S3UploaderError):
    pass
