FROM python:3.11-slim-bookworm
LABEL maintainer="Michael J. Stealey <michael.j.stealey@gmail.com>"

WORKDIR /code

# uwsgi needs libpcre at runtime and a C toolchain + headers to build its wheel
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpcre3 \
        libpcre3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code/requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# drop the build toolchain; keep libpcre3 for uwsgi at runtime
RUN apt-get purge -y --auto-remove build-essential libpcre3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ./server /code/server
COPY ./docker-entrypoint.sh /code/docker-entrypoint.sh
RUN chmod +x /code/docker-entrypoint.sh

ENTRYPOINT ["/code/docker-entrypoint.sh"]
EXPOSE 5000
CMD ["run_server"]
