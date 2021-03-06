# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.cookie_encoded import CookieEncoded  # noqa: F401,E501
from swagger_server.models.status200_ok_single import Status200OkSingle  # noqa: F401,E501
from swagger_server import util


class ApiCookieEncoded(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data: List[CookieEncoded]=None, size: int=1, status: int=200, type: str=None):  # noqa: E501
        """ApiCookieEncoded - a model defined in Swagger

        :param data: The data of this ApiCookieEncoded.  # noqa: E501
        :type data: List[CookieEncoded]
        :param size: The size of this ApiCookieEncoded.  # noqa: E501
        :type size: int
        :param status: The status of this ApiCookieEncoded.  # noqa: E501
        :type status: int
        :param type: The type of this ApiCookieEncoded.  # noqa: E501
        :type type: str
        """
        self.swagger_types = {
            'data': List[CookieEncoded],
            'size': int,
            'status': int,
            'type': str
        }

        self.attribute_map = {
            'data': 'data',
            'size': 'size',
            'status': 'status',
            'type': 'type'
        }
        self._data = data
        self._size = size
        self._status = status
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'ApiCookieEncoded':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The api_cookie_encoded of this ApiCookieEncoded.  # noqa: E501
        :rtype: ApiCookieEncoded
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[CookieEncoded]:
        """Gets the data of this ApiCookieEncoded.


        :return: The data of this ApiCookieEncoded.
        :rtype: List[CookieEncoded]
        """
        return self._data

    @data.setter
    def data(self, data: List[CookieEncoded]):
        """Sets the data of this ApiCookieEncoded.


        :param data: The data of this ApiCookieEncoded.
        :type data: List[CookieEncoded]
        """

        self._data = data

    @property
    def size(self) -> int:
        """Gets the size of this ApiCookieEncoded.


        :return: The size of this ApiCookieEncoded.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size: int):
        """Sets the size of this ApiCookieEncoded.


        :param size: The size of this ApiCookieEncoded.
        :type size: int
        """

        self._size = size

    @property
    def status(self) -> int:
        """Gets the status of this ApiCookieEncoded.


        :return: The status of this ApiCookieEncoded.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this ApiCookieEncoded.


        :param status: The status of this ApiCookieEncoded.
        :type status: int
        """

        self._status = status

    @property
    def type(self) -> str:
        """Gets the type of this ApiCookieEncoded.


        :return: The type of this ApiCookieEncoded.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ApiCookieEncoded.


        :param type: The type of this ApiCookieEncoded.
        :type type: str
        """

        self._type = type
