#!/usr/bin/env bash

if [[ "$1" == 'run_server' ]]; then
    # setup virtual environment
    source .env
    pip install -U pip
    pip install virtualenv
    virtualenv -p /usr/local/bin/python .venv
    source .venv/bin/activate
    pip install -r requirements.txt

    # update swagger.yaml file
    if [[ ! -z ${API_SWAGGER_HOST} ]]; then
        sed -i '/servers:/!b;n;c- url: http://'${API_SWAGGER_HOST}'/' /code/server/swagger_server/swagger/swagger.yaml
    fi

    # run the server
    uwsgi --virtualenv ./.venv --ini server/vouch-proxy-demo-api.ini
else
    exec "$@"
fi
