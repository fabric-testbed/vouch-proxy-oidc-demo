#!/usr/bin/env python3

import connexion

from swagger_server import encoder

connex_app = connexion.FlaskApp(__name__, specification_dir="./swagger/")
connex_app.app.json = encoder.JSONProvider(connex_app.app)
connex_app.add_api(
    "swagger.yaml", arguments={"title": "Vouch-Proxy OIDC Demo"}, pythonic_params=True
)

app = connex_app.app

logger = app.logger

if __name__ == "__main__":
    logger.info("Starting Vouch-Proxy OIDC Demo")
    connex_app.run(port=5000)
