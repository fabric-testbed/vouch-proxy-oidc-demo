#!/usr/bin/env bash
set -euo pipefail

if [[ "${1:-}" == 'run_server' ]]; then
    # optionally rewrite the swagger.yaml server URL when API_SWAGGER_HOST is set
    if [[ -n "${API_SWAGGER_HOST:-}" ]]; then
        sed -i '/servers:/!b;n;c- url: http://'${API_SWAGGER_HOST}'/' /code/server/swagger_server/swagger/swagger.yaml
    fi

    exec uvicorn --app-dir server swagger_server.__main__:connex_app \
        --host 0.0.0.0 --port 5000 --workers "${API_WORKERS:-8}" \
        --proxy-headers --forwarded-allow-ips '*'
else
    exec "$@"
fi
