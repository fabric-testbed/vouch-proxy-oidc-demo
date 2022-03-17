# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Vouch-Proxy OIDC JWT Demo",
    author_email="stealey@unc.edu",
    url="",
    keywords=["Swagger", "Vouch-Proxy OIDC JWT Demo"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    Explore how Vouch-Proxy encapsulates OIDC JWT information as a cookie object 1. Vouch-Proxy JWT stored as base64 encoded gzipped cookie 2. Vouch-Proxy JWT base64 decoded and unzipped (signature alg: HS256) 3. CILogon tokens (access, identity, refresh) - unpacked from JWT (signature alg: RS256) 4. Fully decoded/unpacked JWT with CILogon tokens  Login:  https://{server_URL}/login \\ Logout: https://{server_URL}/logout 
    """
)
