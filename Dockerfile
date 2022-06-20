FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV TZ EST

RUN apt-get update \
    && apt-get -y install \
    python2 python3-pip python3 \
    && apt-get clean

COPY . /src/
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -e /src/
ADD conf/gunicorn_conf.py /conf/gunicorn_conf.py

RUN useradd -m -d /lw -s /bin/bash -u 99 lw \
    && mkdir /lw/w \
    && chown lw:lw /lw/w

USER lw
WORKDIR /lw/w
EXPOSE 7654

CMD gunicorn -k uvicorn.workers.UvicornWorker -c /conf/gunicorn_conf.py lw.app:app
