# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CookieEncoded(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, cookie_name: str=None, cookie_value: str=None):  # noqa: E501
        """CookieEncoded - a model defined in Swagger

        :param cookie_name: The cookie_name of this CookieEncoded.  # noqa: E501
        :type cookie_name: str
        :param cookie_value: The cookie_value of this CookieEncoded.  # noqa: E501
        :type cookie_value: str
        """
        self.swagger_types = {
            'cookie_name': str,
            'cookie_value': str
        }

        self.attribute_map = {
            'cookie_name': 'cookie_name',
            'cookie_value': 'cookie_value'
        }
        self._cookie_name = cookie_name
        self._cookie_value = cookie_value

    @classmethod
    def from_dict(cls, dikt) -> 'CookieEncoded':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The cookie_encoded of this CookieEncoded.  # noqa: E501
        :rtype: CookieEncoded
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cookie_name(self) -> str:
        """Gets the cookie_name of this CookieEncoded.


        :return: The cookie_name of this CookieEncoded.
        :rtype: str
        """
        return self._cookie_name

    @cookie_name.setter
    def cookie_name(self, cookie_name: str):
        """Sets the cookie_name of this CookieEncoded.


        :param cookie_name: The cookie_name of this CookieEncoded.
        :type cookie_name: str
        """

        self._cookie_name = cookie_name

    @property
    def cookie_value(self) -> str:
        """Gets the cookie_value of this CookieEncoded.


        :return: The cookie_value of this CookieEncoded.
        :rtype: str
        """
        return self._cookie_value

    @cookie_value.setter
    def cookie_value(self, cookie_value: str):
        """Sets the cookie_value of this CookieEncoded.


        :param cookie_value: The cookie_value of this CookieEncoded.
        :type cookie_value: str
        """

        self._cookie_value = cookie_value
