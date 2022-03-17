import json
import os
from typing import Union

from flask import request, Response

from swagger_server.models.api_cilogon_tokens import ApiCilogonTokens
from swagger_server.models.api_cookie_encoded import ApiCookieEncoded
from swagger_server.models.api_jwt_decoded import ApiJwtDecoded
from swagger_server.models.api_jwt_fully_decoded import ApiJwtFullyDecoded
from swagger_server.models.status401_unauthorized import Status401Unauthorized, Status401UnauthorizedErrors
from swagger_server.models.status500_internal_server_error import Status500InternalServerError, \
    Status500InternalServerErrorErrors

# Constants
_INDENT = int(os.getenv('API_JSON_RESPONSE_INDENT', '0'))


def delete_none(_dict):
    """
    Delete None values recursively from all of the dictionaries, tuples, lists, sets
    """
    if isinstance(_dict, dict):
        for key, value in list(_dict.items()):
            if isinstance(value, (list, dict, tuple, set)):
                _dict[key] = delete_none(value)
            elif value is None or key is None:
                del _dict[key]

    elif isinstance(_dict, (list, set, tuple)):
        _dict = type(_dict)(delete_none(item) for item in _dict if item is not None)

    return _dict


def cors_response(req: request, status_code: int = 200, body: object = None, x_error: str = None) -> Response:
    """
    Return CORS Response object
    """
    response = Response()
    response.status_code = status_code
    response.data = body
    response.headers['Access-Control-Allow-Origin'] = req.headers.get('Origin', '*')
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = \
        'DNT, User-Agent, X-Requested-With, If-Modified-Since, Cache-Control, Content-Type, Range, Authorization'
    response.headers['Access-Control-Expose-Headers'] = 'Content-Length, Content-Range, X-Error'

    if x_error:
        response.headers['X-Error'] = x_error

    return response


def cors_200(response_body: Union[
    ApiCilogonTokens, ApiCookieEncoded, ApiJwtDecoded, ApiJwtFullyDecoded
] = None) -> cors_response:
    """
    Return 200 - OK
    """
    return cors_response(
        req=request,
        status_code=200,
        body=json.dumps(delete_none(response_body.to_dict()), indent=_INDENT, sort_keys=True)
        if _INDENT != 0 else json.dumps(delete_none(response_body.to_dict()), sort_keys=True)
    )


def cors_401(details: str = None) -> cors_response:
    """
    Return 401 - Unauthorized
    """
    errors = Status401UnauthorizedErrors()
    errors.details = details
    error_object = Status401Unauthorized([errors])
    return cors_response(
        req=request,
        status_code=401,
        body=json.dumps(delete_none(error_object.to_dict()), indent=_INDENT, sort_keys=True)
        if _INDENT != 0 else json.dumps(delete_none(error_object.to_dict()), sort_keys=True),
        x_error=details
    )


def cors_500(details: str = None) -> cors_response:
    """
    Return 500 - Internal Server Error
    """
    errors = Status500InternalServerErrorErrors()
    errors.details = details
    error_object = Status500InternalServerError([errors])
    return cors_response(
        req=request,
        status_code=500,
        body=json.dumps(delete_none(error_object.to_dict()), indent=_INDENT, sort_keys=True)
        if _INDENT != 0 else json.dumps(delete_none(error_object.to_dict()), sort_keys=True),
        x_error=details
    )
