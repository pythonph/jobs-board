FROM ubuntu:16.04

RUN mkdir -p /_build/
WORKDIR /_build/
ADD . /_build/

RUN apt-get update && apt-get install -y \
       build-essential \
       libpq-dev \
       libssl-dev \
       libffi-dev \
       libxml2-dev \
       libxslt1-dev \
       zlib1g-dev \
       liblcms2-dev \
       libpng12-dev \
       libjpeg-dev \
       libfreetype6-dev \
       python3-dev \
       python3-pip \
       nodejs \
       npm \
    && pip3 install -U pip \
    && pip3 install -r requirements.txt \
    && npm install

# Clean up
RUN apt-get autoclean \
    && apt-get autoremove \
    && apt-get purge \
    && rm -Rf /_build/
