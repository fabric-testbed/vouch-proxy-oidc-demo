import connexion
import six

from swagger_server.models.api_cilogon_tokens import ApiCilogonTokens  # noqa: E501
from swagger_server.models.api_cookie_encoded import ApiCookieEncoded  # noqa: E501
from swagger_server.models.api_jwt_decoded import ApiJwtDecoded  # noqa: E501
from swagger_server.models.api_jwt_fully_decoded import ApiJwtFullyDecoded  # noqa: E501
from swagger_server.models.status401_unauthorized import Status401Unauthorized  # noqa: E501
from swagger_server.models.status500_internal_server_error import Status500InternalServerError  # noqa: E501
from swagger_server import util
from swagger_server.response_code import vouch_proxy_controller as rc


def step1_encoded_vouch_cookie_get():  # noqa: E501
    """Encoded JWT as Vouch-Proxy cookie

    GET encoded JWT as cookie from Vouch-Proxy # noqa: E501


    :rtype: ApiCookieEncoded
    """
    return rc.step1_encoded_vouch_cookie_get()


def step2_decoded_vouch_jwt_get():  # noqa: E501
    """Decoded JWT from Vouch-Proxy cookie

    GET decoded JWT from the cookie (alg HS256) # noqa: E501


    :rtype: ApiJwtDecoded
    """
    return rc.step2_decoded_vouch_jwt_get()


def step3_decoded_cilogon_tokens_get():  # noqa: E501
    """CILogon Tokens

    GET CILogon tokens with decoded PIdToken JWT (alg RS256) # noqa: E501


    :rtype: ApiCilogonTokens
    """
    return rc.step3_decoded_cilogon_tokens_get()


def step4_fully_decoded_jwt_get():  # noqa: E501
    """Fully decoded JWT

    GET fully decoded JWT including CILogon tokens # noqa: E501


    :rtype: ApiJwtFullyDecoded
    """
    return rc.step4_fully_decoded_jwt_get()
