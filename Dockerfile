FROM nikolaik/python-nodejs:python3.5-nodejs12-alpine
MAINTAINER Joshua Coales <joshua@coales.co.uk>

RUN mkdir /usr/cf_bypass
WORKDIR /usr/cf_bypass

COPY . /usr/cf_bypass
RUN pip install -r requirements.txt

EXPOSE 4999/tcp

CMD python ./run.py
