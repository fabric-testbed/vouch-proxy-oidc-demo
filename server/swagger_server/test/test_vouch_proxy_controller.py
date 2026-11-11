# coding: utf-8
import base64
import gzip
import time
import unittest
from unittest import mock

import jwt
from cryptography.hazmat.primitives.asymmetric import rsa

from swagger_server.test import BaseTestCase, make_vouch_cookie

ENDPOINTS = [
    "/step1-encoded-vouch-cookie",
    "/step2-decoded-vouch-jwt",
    "/step3-decoded-cilogon-tokens",
    "/step4-fully-decoded-jwt",
]


class TestVouchProxyController(BaseTestCase):
    """VouchProxyController integration tests"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # stand-in for CILogon's RS256 signing key (avoids hitting https://cilogon.org/oauth2/certs)
        cls.rsa_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        cls.id_claims = {
            "sub": "http://cilogon.org/serverA/users/1234",
            "email": "user@example.org",
        }
        id_token = jwt.encode(cls.id_claims, cls.rsa_key, algorithm="RS256")
        cls.vouch_claims = {
            "username": "user@example.org",
            "iss": "Vouch",
            "aud": ["127.0.0.1"],
            "exp": int(time.time()) + 3600,
            "CustomClaims": {"email": "user@example.org"},
            "PAccessToken": "access-token",
            "PIdToken": id_token,
            "PRefreshToken": "refresh-token",
        }
        cls.cookie = make_vouch_cookie(cls.vouch_claims)

    def mock_jwks(self):
        signing_key = mock.Mock(key=self.rsa_key.public_key())
        patcher = mock.patch(
            "swagger_server.response_code.vouch_proxy_controller.PyJWKClient"
        )
        jwks_client = patcher.start()
        self.addCleanup(patcher.stop)
        jwks_client.return_value.get_signing_key_from_jwt.return_value = signing_key

    def test_login_required_without_cookie(self):
        for path in ENDPOINTS:
            with self.subTest(path=path):
                response = self.get(path)
                self.assertEqual(response.status_code, 401, response.text)
                self.assertIn("Login required", response.text)

    def test_step1_encoded_vouch_cookie_get(self):
        response = self.get("/step1-encoded-vouch-cookie", self.cookie)
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertEqual(body["type"], "vouch.cookie.encoded")
        self.assertEqual(body["data"][0]["cookie_value"], self.cookie)

    def test_step2_decoded_vouch_jwt_get(self):
        response = self.get("/step2-decoded-vouch-jwt", self.cookie)
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertEqual(body["type"], "vouch.jwt.decoded")
        self.assertEqual(body["data"][0]["username"], self.vouch_claims["username"])

    def test_step2_rejects_wrong_secret(self):
        bad = jwt.encode(self.vouch_claims, "not-the-vouch-secret-but-32-bytes-long", algorithm="HS256")

        cookie = base64.urlsafe_b64encode(gzip.compress(bad.encode())).decode()
        response = self.get("/step2-decoded-vouch-jwt", cookie)
        self.assertEqual(response.status_code, 500, response.text)

    def test_step3_decoded_cilogon_tokens_get(self):
        self.mock_jwks()
        response = self.get("/step3-decoded-cilogon-tokens", self.cookie)
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertEqual(body["type"], "cilogon.tokens")
        self.assertEqual(
            body["data"][0]["identity_token"]["sub"], self.id_claims["sub"]
        )

    def test_step4_fully_decoded_jwt_get(self):
        self.mock_jwks()
        response = self.get("/step4-fully-decoded-jwt", self.cookie)
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertEqual(body["type"], "vouch.jwt.fullydecoded")
        self.assertEqual(
            body["data"][0]["cilogon_identity_token"]["email"], self.id_claims["email"]
        )

    def test_swagger_ui_served(self):
        response = self.get("/ui/")
        self.assertEqual(response.status_code, 200, response.text)


if __name__ == "__main__":
    unittest.main()
