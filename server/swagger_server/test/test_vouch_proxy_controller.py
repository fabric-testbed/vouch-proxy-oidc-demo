# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_cilogon_tokens import ApiCilogonTokens  # noqa: E501
from swagger_server.models.api_cookie_encoded import ApiCookieEncoded  # noqa: E501
from swagger_server.models.api_jwt_decoded import ApiJwtDecoded  # noqa: E501
from swagger_server.models.api_jwt_fully_decoded import ApiJwtFullyDecoded  # noqa: E501
from swagger_server.models.status401_unauthorized import Status401Unauthorized  # noqa: E501
from swagger_server.models.status500_internal_server_error import Status500InternalServerError  # noqa: E501
from swagger_server.test import BaseTestCase


class TestVouchProxyController(BaseTestCase):
    """VouchProxyController integration test stubs"""

    def test_step1_encoded_vouch_cookie_get(self):
        """Test case for step1_encoded_vouch_cookie_get

        Encoded JWT as Vouch-Proxy cookie
        """
        response = self.client.open(
            '/step1-encoded-vouch-cookie',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_step2_decoded_vouch_jwt_get(self):
        """Test case for step2_decoded_vouch_jwt_get

        Decoded JWT from Vouch-Proxy cookie
        """
        response = self.client.open(
            '/step2-decoded-vouch-jwt',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_step3_decoded_cilogon_tokens_get(self):
        """Test case for step3_decoded_cilogon_tokens_get

        CILogon Tokens
        """
        response = self.client.open(
            '/step3-decoded-cilogon-tokens',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_step4_fully_decoded_jwt_get(self):
        """Test case for step4_fully_decoded_jwt_get

        Fully decoded JWT
        """
        response = self.client.open(
            '/step4-fully-decoded-jwt',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
