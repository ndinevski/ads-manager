import datetime
import json
import typing

import marshmallow

from ads_manager import enums


def get_exception_message(exception: Exception) -> str:
    if isinstance(exception, type):
        return exception.__name__

    if hasattr(exception, "message") and exception.message:
        return exception.message
    return exception.args[0] if len(exception.args) else ""


def validate_marshmallow_schema(
    data: typing.Union[typing.Dict, typing.List[typing.Dict]],
    schema: marshmallow.schema.Schema,
) -> typing.Optional[typing.Dict]:
    try:
        validated_data = schema.load(data=data, unknown=marshmallow.EXCLUDE)
    except marshmallow.exceptions.ValidationError:
        return None

    return validated_data


def convert_schema_list_and_dict_fields_to_json_string(
    data: typing.Dict,
) -> typing.Dict:
    for key, value in data.items():
        if isinstance(value, dict):
            data[key] = json.dumps(value)

        if isinstance(value, list):
            data[key] = json.dumps(value)

    return data


def format_tiktok_date(date_start: datetime.datetime) -> str:
    return date_start.strftime("%Y-%m-%d")


def validate_params(params: typing.Dict) -> None:
    if params is None:
        raise ValueError('Parameters "app_id" and "secret" are required for tiktok platform.')

    app_id = params.get("app_id")
    secret = params.get("secret")
    sandbox = params.get("sandbox")

    if app_id is None or not isinstance(app_id, str):
        raise ValueError("app_id must exist and be a string in params dictionary.")

    if secret is None or not isinstance(secret, str):
        raise ValueError("secret must exist and be a string in params dictionary.")

    if sandbox is not isinstance(sandbox, bool):
        raise ValueError("sandbox must be a boolean value in params dictionary.")
