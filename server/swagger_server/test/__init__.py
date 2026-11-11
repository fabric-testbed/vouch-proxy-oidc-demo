import base64
import gzip
import logging
import os
import unittest

import jwt

TEST_COOKIE_NAME = "vouch-test-cookie"
TEST_JWT_SECRET = "vouch-test-secret-at-least-32-bytes-long"

os.environ.setdefault("VOUCH_COOKIE_NAME", TEST_COOKIE_NAME)
os.environ.setdefault("VOUCH_JWT_SECRET", TEST_JWT_SECRET)
os.environ.setdefault("API_SERVER_URL", "https://127.0.0.1:8443")


def make_vouch_cookie(claims: dict) -> str:
    """Build a cookie value the way Vouch-Proxy does: HS256 JWT -> gzip -> urlsafe base64."""
    token = jwt.encode(claims, os.environ["VOUCH_JWT_SECRET"], algorithm="HS256")
    return base64.urlsafe_b64encode(gzip.compress(token.encode("utf-8"))).decode(
        "ascii"
    )


class BaseTestCase(unittest.TestCase):
    """Exercises the real Connexion 3 app (ASGI middleware + Flask) via its Starlette test client."""

    @classmethod
    def setUpClass(cls):
        logging.getLogger("connexion.operation").setLevel("ERROR")
        from swagger_server.__main__ import connex_app

        cls.client = connex_app.test_client()

    def get(self, path, cookie=None):
        self.client.cookies.clear()
        if cookie:
            self.client.cookies.set(os.environ["VOUCH_COOKIE_NAME"], cookie)
        return self.client.get(path)
