#!/usr/bin/env bash
set -euo pipefail

if [[ "${1:-}" == 'run_server' ]]; then
    # optionally rewrite the swagger.yaml server URL when API_SWAGGER_HOST is set
    if [[ -n "${API_SWAGGER_HOST:-}" ]]; then
        sed -i '/servers:/!b;n;c- url: http://'${API_SWAGGER_HOST}'/' /code/server/swagger_server/swagger/swagger.yaml
    fi

    exec uwsgi --ini server/vouch-proxy-demo-api.ini
else
    exec "$@"
fi
