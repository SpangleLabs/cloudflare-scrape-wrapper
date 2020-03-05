FROM nikolaik/python-nodejs:python3.7-nodejs12-alpine
FROM tiangolo/meinheld-gunicorn-flask:python3.7-alpine3.8
MAINTAINER Joshua Coales <joshua@coales.co.uk>

COPY . /app
RUN pip install -r requirements.txt -U

EXPOSE 4999/tcp

ENV MODULE_NAME "run"
ENV VARIABLE_NAME "app"