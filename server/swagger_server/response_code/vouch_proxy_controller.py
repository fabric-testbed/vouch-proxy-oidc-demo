import base64
import gzip
import logging
import os

import jwt
from flask import request
from jwt import PyJWKClient

from swagger_server.models.api_cilogon_tokens import ApiCilogonTokens, CilogonTokens
from swagger_server.models.api_cookie_encoded import ApiCookieEncoded, CookieEncoded
from swagger_server.models.api_jwt_decoded import ApiJwtDecoded, JwtDecoded
from swagger_server.models.api_jwt_fully_decoded import ApiJwtFullyDecoded, JwtFullyDecoded
from swagger_server.response_code.cors_response import cors_200, cors_500
from swagger_server.response_code.decorators import login_required

logger = logging.getLogger(__name__)


@login_required
def step1_encoded_vouch_cookie_get() -> ApiCookieEncoded:  # noqa: E501
    """Encoded JWT as Vouch-Proxy cookie

    GET encoded JWT as cookie from Vouch-Proxy # noqa: E501


    :rtype: ApiCookieEncoded
    """
    try:
        logger.info('step1_encoded_vouch_cookie_get():')
        # cookie holder
        cookie = CookieEncoded()
        cookie.cookie_name = os.getenv('VOUCH_COOKIE_NAME')
        cookie.cookie_value = request.cookies.get(os.getenv('VOUCH_COOKIE_NAME'))
        # create data container
        data = [cookie]
        # set response
        response = ApiCookieEncoded()
        response.data = data
        response.size = len(response.data)
        response.status = 200
        response.type = 'vouch.cookie.encoded'
        return cors_200(response_body=response)
    except Exception as exc:
        details = 'Oops!! Something went wrong at: step1_encoded_vouch_cookie_get(): {0}'.format(exc)
        logger.error(details)
        return cors_500(details=details)


@login_required
def step2_decoded_vouch_jwt_get() -> ApiJwtDecoded:  # noqa: E501
    """Decoded JWT from Vouch-Proxy cookie

    GET decoded JWT from the cookie (alg HS256) # noqa: E501


    :rtype: ApiJwtDecoded
    """
    try:
        logger.info('step2_decoded_vouch_jwt_get():')
        # get base64 encoded gzipped vouch JWT
        base64_encoded_gzip_vouch_jwt = request.cookies.get(os.getenv('VOUCH_COOKIE_NAME'))
        # decode base64
        encoded_gzip_vouch_jwt_bytes = base64.urlsafe_b64decode(base64_encoded_gzip_vouch_jwt)
        # gzip decompress
        vouch_jwt_bytes = gzip.decompress(encoded_gzip_vouch_jwt_bytes)
        # decode bytes
        vouch_jwt = vouch_jwt_bytes.decode('utf-8')
        # decode JWT using Vouch Proxy secret key (do not verify aud)
        print(vouch_jwt)
        vouch_json = jwt.decode(
            jwt=vouch_jwt,
            key=os.getenv('VOUCH_JWT_SECRET'),
            algorithms=["HS256"],
            options={"verify_aud": False}
        )
        # vouch_jwt holder for decoded JWT
        vouch_jwt = JwtDecoded()
        vouch_jwt.aud = vouch_json.get('aud')
        vouch_jwt.custom_claims = vouch_json.get('CustomClaims')
        vouch_jwt.exp = vouch_json.get('exp')
        vouch_jwt.iss = vouch_json.get('iss')
        vouch_jwt.p_access_token = vouch_json.get('PAccessToken')
        vouch_jwt.p_id_token = vouch_json.get('PIdToken')
        vouch_jwt.p_refresh_token = vouch_json.get('PRefreshToken')
        vouch_jwt.username = vouch_json.get('username')
        # create data container
        data = [vouch_jwt]
        # set response
        response = ApiJwtDecoded()
        response.data = data
        response.size = len(data)
        response.status = 200
        response.type = 'vouch.jwt.decoded'
        return cors_200(response_body=response)
    except Exception as exc:
        details = 'Oops!! Something went wrong at: step2_decoded_vouch_jwt_get(): {0}'.format(exc)
        logger.error(details)
        return cors_500(details=details)


@login_required
def step3_decoded_cilogon_tokens_get() -> ApiCilogonTokens:  # noqa: E501
    """CILogon Tokens

    GET CILogon tokens with decoded PIdToken JWT (alg RS256) # noqa: E501


    :rtype: ApiCilogonTokens
    """
    try:
        logger.info('step3_decoded_cilogon_tokens_get():')
        # get base64 encoded gzipped vouch JWT
        base64_encoded_gzip_vouch_jwt = request.cookies.get(os.getenv('VOUCH_COOKIE_NAME'))
        # decode base64
        encoded_gzip_vouch_jwt_bytes = base64.urlsafe_b64decode(base64_encoded_gzip_vouch_jwt)
        # gzip decompress
        vouch_jwt_bytes = gzip.decompress(encoded_gzip_vouch_jwt_bytes)
        # decode bytes
        vouch_jwt = vouch_jwt_bytes.decode('utf-8')
        # decode JWT using Vouch Proxy secret key (do not verify aud) - HS256
        vouch_json = jwt.decode(
            jwt=vouch_jwt,
            key=os.getenv('VOUCH_JWT_SECRET'),
            algorithms=["HS256"],
            options={"verify_aud": False}
        )
        # decode CILogon Identity Token (JWT)
        # CILogon's JWKS endpoint for verifying signed JWTs
        jwks_url = "https://cilogon.org/oauth2/certs"
        # create jwks client object
        jwks_client = PyJWKClient(jwks_url)
        # get the signing key from the jwks endpoint
        signing_key = jwks_client.get_signing_key_from_jwt(vouch_json.get('PIdToken'))
        # decode JWT using CILogon signing key (do not verify aud or exp) - RS256
        print(vouch_json.get('PIdToken'))
        identity_json = jwt.decode(
            jwt=vouch_json.get('PIdToken'),
            key=signing_key.key,
            algorithms=["RS256"],
            options={"verify_aud": False, "verify_exp": False}
        )
        # tokens holder for CILogon tokens and decoded PIdToken JWT
        tokens = CilogonTokens()
        tokens.access_token = vouch_json.get('PAccessToken')
        tokens.identity_token = identity_json
        tokens.refresh_token = vouch_json.get('PRefreshToken')
        # create data container
        data = [tokens]
        # set response
        response = ApiCilogonTokens()
        response.data = data
        response.size = len(data)
        response.status = 200
        response.type = 'cilogon.tokens'
        return cors_200(response_body=response)
    except Exception as exc:
        details = 'Oops!! Something went wrong at: step3_decoded_cilogon_tokens_get(): {0}'.format(exc)
        logger.error(details)
        return cors_500(details=details)


@login_required
def step4_fully_decoded_jwt_get() -> ApiJwtFullyDecoded:  # noqa: E501
    """Fully decoded JWT

    GET fully decoded JWT including CILogon tokens # noqa: E501


    :rtype: ApiJwtFullyDecoded
    """
    try:
        logger.info('step4_fully_decoded_jwt_get():')
        # get base64 encoded gzipped vouch JWT
        base64_encoded_gzip_vouch_jwt = request.cookies.get(os.getenv('VOUCH_COOKIE_NAME'))
        # decode base64
        encoded_gzip_vouch_jwt_bytes = base64.urlsafe_b64decode(base64_encoded_gzip_vouch_jwt)
        # gzip decompress
        vouch_jwt_bytes = gzip.decompress(encoded_gzip_vouch_jwt_bytes)
        # decode bytes
        vouch_jwt = vouch_jwt_bytes.decode('utf-8')
        # decode JWT using Vouch Proxy secret key (do not verify aud)
        vouch_json = jwt.decode(
            jwt=vouch_jwt,
            key=os.getenv('VOUCH_JWT_SECRET'),
            algorithms=["HS256"],
            options={"verify_aud": False}
        )
        # decode CILogon Identity Token (JWT)
        # CILogon's JWKS endpoint for verifying signed JWTs
        jwks_url = "https://cilogon.org/oauth2/certs"
        # create jwks client object
        jwks_client = PyJWKClient(jwks_url)
        # get the signing key from the jwks endpoint
        signing_key = jwks_client.get_signing_key_from_jwt(vouch_json.get('PIdToken'))
        # decode JWT using CILogon signing key (do not verify aud or exp) - RS256
        identity_json = jwt.decode(
            jwt=vouch_json.get('PIdToken'),
            key=signing_key.key,
            algorithms=["RS256"],
            options={"verify_aud": False, "verify_exp": False}
        )
        # vouch_jwt holder for fully decoded JWT
        vouch_jwt = JwtFullyDecoded()
        vouch_jwt.aud = vouch_json.get('aud')
        vouch_jwt.custom_claims = vouch_json.get('CustomClaims')
        vouch_jwt.exp = vouch_json.get('exp')
        vouch_jwt.iss = vouch_json.get('iss')
        vouch_jwt.cilogon_access_token = vouch_json.get('PAccessToken')
        vouch_jwt.cilogon_identity_token = identity_json
        vouch_jwt.cilogon_refresh_token = vouch_json.get('PRefreshToken')
        vouch_jwt.username = vouch_json.get('username')
        data = [vouch_jwt]
        # set response
        response = ApiJwtFullyDecoded()
        response.data = data
        response.size = len(data)
        response.status = 200
        response.type = 'vouch.jwt.fullydecoded'
        return cors_200(response_body=response)
    except Exception as exc:
        details = 'Oops!! Something went wrong at: step4_fully_decoded_jwt_get(): {0}'.format(exc)
        logger.error(details)
        return cors_500(details=details)
