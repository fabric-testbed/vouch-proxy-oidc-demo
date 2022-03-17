# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.jwt_decoded_custom_claims import JwtDecodedCustomClaims  # noqa: F401,E501
from swagger_server import util


class JwtDecoded(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, aud: str=None, custom_claims: JwtDecodedCustomClaims=None, exp: str=None, iss: str=None, p_access_token: str=None, p_id_token: str=None, p_refresh_token: str=None, username: str=None):  # noqa: E501
        """JwtDecoded - a model defined in Swagger

        :param aud: The aud of this JwtDecoded.  # noqa: E501
        :type aud: str
        :param custom_claims: The custom_claims of this JwtDecoded.  # noqa: E501
        :type custom_claims: JwtDecodedCustomClaims
        :param exp: The exp of this JwtDecoded.  # noqa: E501
        :type exp: str
        :param iss: The iss of this JwtDecoded.  # noqa: E501
        :type iss: str
        :param p_access_token: The p_access_token of this JwtDecoded.  # noqa: E501
        :type p_access_token: str
        :param p_id_token: The p_id_token of this JwtDecoded.  # noqa: E501
        :type p_id_token: str
        :param p_refresh_token: The p_refresh_token of this JwtDecoded.  # noqa: E501
        :type p_refresh_token: str
        :param username: The username of this JwtDecoded.  # noqa: E501
        :type username: str
        """
        self.swagger_types = {
            'aud': str,
            'custom_claims': JwtDecodedCustomClaims,
            'exp': str,
            'iss': str,
            'p_access_token': str,
            'p_id_token': str,
            'p_refresh_token': str,
            'username': str
        }

        self.attribute_map = {
            'aud': 'aud',
            'custom_claims': 'CustomClaims',
            'exp': 'exp',
            'iss': 'iss',
            'p_access_token': 'PAccessToken',
            'p_id_token': 'PIdToken',
            'p_refresh_token': 'PRefreshToken',
            'username': 'username'
        }
        self._aud = aud
        self._custom_claims = custom_claims
        self._exp = exp
        self._iss = iss
        self._p_access_token = p_access_token
        self._p_id_token = p_id_token
        self._p_refresh_token = p_refresh_token
        self._username = username

    @classmethod
    def from_dict(cls, dikt) -> 'JwtDecoded':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The jwt_decoded of this JwtDecoded.  # noqa: E501
        :rtype: JwtDecoded
        """
        return util.deserialize_model(dikt, cls)

    @property
    def aud(self) -> str:
        """Gets the aud of this JwtDecoded.


        :return: The aud of this JwtDecoded.
        :rtype: str
        """
        return self._aud

    @aud.setter
    def aud(self, aud: str):
        """Sets the aud of this JwtDecoded.


        :param aud: The aud of this JwtDecoded.
        :type aud: str
        """

        self._aud = aud

    @property
    def custom_claims(self) -> JwtDecodedCustomClaims:
        """Gets the custom_claims of this JwtDecoded.


        :return: The custom_claims of this JwtDecoded.
        :rtype: JwtDecodedCustomClaims
        """
        return self._custom_claims

    @custom_claims.setter
    def custom_claims(self, custom_claims: JwtDecodedCustomClaims):
        """Sets the custom_claims of this JwtDecoded.


        :param custom_claims: The custom_claims of this JwtDecoded.
        :type custom_claims: JwtDecodedCustomClaims
        """

        self._custom_claims = custom_claims

    @property
    def exp(self) -> str:
        """Gets the exp of this JwtDecoded.


        :return: The exp of this JwtDecoded.
        :rtype: str
        """
        return self._exp

    @exp.setter
    def exp(self, exp: str):
        """Sets the exp of this JwtDecoded.


        :param exp: The exp of this JwtDecoded.
        :type exp: str
        """

        self._exp = exp

    @property
    def iss(self) -> str:
        """Gets the iss of this JwtDecoded.


        :return: The iss of this JwtDecoded.
        :rtype: str
        """
        return self._iss

    @iss.setter
    def iss(self, iss: str):
        """Sets the iss of this JwtDecoded.


        :param iss: The iss of this JwtDecoded.
        :type iss: str
        """

        self._iss = iss

    @property
    def p_access_token(self) -> str:
        """Gets the p_access_token of this JwtDecoded.


        :return: The p_access_token of this JwtDecoded.
        :rtype: str
        """
        return self._p_access_token

    @p_access_token.setter
    def p_access_token(self, p_access_token: str):
        """Sets the p_access_token of this JwtDecoded.


        :param p_access_token: The p_access_token of this JwtDecoded.
        :type p_access_token: str
        """

        self._p_access_token = p_access_token

    @property
    def p_id_token(self) -> str:
        """Gets the p_id_token of this JwtDecoded.


        :return: The p_id_token of this JwtDecoded.
        :rtype: str
        """
        return self._p_id_token

    @p_id_token.setter
    def p_id_token(self, p_id_token: str):
        """Sets the p_id_token of this JwtDecoded.


        :param p_id_token: The p_id_token of this JwtDecoded.
        :type p_id_token: str
        """

        self._p_id_token = p_id_token

    @property
    def p_refresh_token(self) -> str:
        """Gets the p_refresh_token of this JwtDecoded.


        :return: The p_refresh_token of this JwtDecoded.
        :rtype: str
        """
        return self._p_refresh_token

    @p_refresh_token.setter
    def p_refresh_token(self, p_refresh_token: str):
        """Sets the p_refresh_token of this JwtDecoded.


        :param p_refresh_token: The p_refresh_token of this JwtDecoded.
        :type p_refresh_token: str
        """

        self._p_refresh_token = p_refresh_token

    @property
    def username(self) -> str:
        """Gets the username of this JwtDecoded.


        :return: The username of this JwtDecoded.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this JwtDecoded.


        :param username: The username of this JwtDecoded.
        :type username: str
        """

        self._username = username