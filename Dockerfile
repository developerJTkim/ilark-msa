# 
FROM python:3.8 as requirements-stage

WORKDIR /app
COPY . /app/

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install gcc vim -y \
    && apt-get clean

# install dependencies
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
RUN pip install python-dotenv
RUN pip install --upgrade 'sentry-sdk[fastapi]'