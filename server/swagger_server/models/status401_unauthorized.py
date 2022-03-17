# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.status401_unauthorized_errors import Status401UnauthorizedErrors  # noqa: F401,E501
from swagger_server import util


class Status401Unauthorized(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, errors: List[Status401UnauthorizedErrors]=None, type: str='error', size: int=1, status: int=401):  # noqa: E501
        """Status401Unauthorized - a model defined in Swagger

        :param errors: The errors of this Status401Unauthorized.  # noqa: E501
        :type errors: List[Status401UnauthorizedErrors]
        :param type: The type of this Status401Unauthorized.  # noqa: E501
        :type type: str
        :param size: The size of this Status401Unauthorized.  # noqa: E501
        :type size: int
        :param status: The status of this Status401Unauthorized.  # noqa: E501
        :type status: int
        """
        self.swagger_types = {
            'errors': List[Status401UnauthorizedErrors],
            'type': str,
            'size': int,
            'status': int
        }

        self.attribute_map = {
            'errors': 'errors',
            'type': 'type',
            'size': 'size',
            'status': 'status'
        }
        self._errors = errors
        self._type = type
        self._size = size
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'Status401Unauthorized':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The status_401_unauthorized of this Status401Unauthorized.  # noqa: E501
        :rtype: Status401Unauthorized
        """
        return util.deserialize_model(dikt, cls)

    @property
    def errors(self) -> List[Status401UnauthorizedErrors]:
        """Gets the errors of this Status401Unauthorized.


        :return: The errors of this Status401Unauthorized.
        :rtype: List[Status401UnauthorizedErrors]
        """
        return self._errors

    @errors.setter
    def errors(self, errors: List[Status401UnauthorizedErrors]):
        """Sets the errors of this Status401Unauthorized.


        :param errors: The errors of this Status401Unauthorized.
        :type errors: List[Status401UnauthorizedErrors]
        """

        self._errors = errors

    @property
    def type(self) -> str:
        """Gets the type of this Status401Unauthorized.


        :return: The type of this Status401Unauthorized.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Status401Unauthorized.


        :param type: The type of this Status401Unauthorized.
        :type type: str
        """

        self._type = type

    @property
    def size(self) -> int:
        """Gets the size of this Status401Unauthorized.


        :return: The size of this Status401Unauthorized.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size: int):
        """Sets the size of this Status401Unauthorized.


        :param size: The size of this Status401Unauthorized.
        :type size: int
        """

        self._size = size

    @property
    def status(self) -> int:
        """Gets the status of this Status401Unauthorized.


        :return: The status of this Status401Unauthorized.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this Status401Unauthorized.


        :param status: The status of this Status401Unauthorized.
        :type status: int
        """

        self._status = status
