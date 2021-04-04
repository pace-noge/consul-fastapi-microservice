FROM python:3

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install gcc \
    && apt-get clean

# RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add -

# RUN apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"

# RUN apt-get update && apt-get install consul

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/cache.pip

COPY . /app

# RUN consul connect proxy -sidecar-for school

