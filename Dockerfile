FROM python:3.11-slim-bookworm
LABEL maintainer="Michael J. Stealey <michael.j.stealey@gmail.com>"

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY ./server /code/server
COPY ./docker-entrypoint.sh /code/docker-entrypoint.sh
RUN chmod +x /code/docker-entrypoint.sh

ENTRYPOINT ["/code/docker-entrypoint.sh"]
EXPOSE 5000
CMD ["run_server"]
