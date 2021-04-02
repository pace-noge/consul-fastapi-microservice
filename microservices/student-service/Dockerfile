FROM python:3

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install gcc \
    && apt-get clean

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/cache.pip

COPY . /app

