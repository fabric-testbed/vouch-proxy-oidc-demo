#!/usr/bin/env python3

import connexion

from swagger_server import encoder

connex_app = connexion.App(__name__, specification_dir='./swagger/')
connex_app.app.json_encoder = encoder.JSONEncoder
connex_app.add_api('swagger.yaml', arguments={'title': 'Vouch-Proxy OIDC Demo'}, pythonic_params=True)

app = connex_app.app

logger = app.logger

if __name__ == '__main__':
    logger.info("Starting Vouch-Proxy OIDC Demo")
    app.run(port=5000, debug=True)
