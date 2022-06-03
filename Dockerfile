FROM ubuntu:20.04 as build-env
RUN apt-get update && apt-get upgrade
RUN apt-get install ffmpeg

FROM python:3.9.13-alpine3.15 as build-stage
RUN mkdir -p /install
WORKDIR /install
RUN apk add --no-cache build-base
RUN pip install --no-cache-dir --prefix=/install ffmpeg-python

FROM python:3.9.13-alpine3.15 as production-stage
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
COPY --from=build-stage /install /usr/local
RUN rm -rf /install
RUN mkdir -p /app
WORKDIR /app
COPY ./script/test.py .

