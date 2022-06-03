FROM python:3.9.13-alpine3.15 as build-stage
RUN mkdir -p /install
WORKDIR /install
RUN apk add --no-cache build-base
RUN pip install --no-cache-dir --prefix=/install ffmpeg-python imageio

FROM python:3.9.13-alpine3.15 as production-stage
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
RUN apk add --no-cache ffmpeg
COPY --from=build-stage /install /usr/local
RUN rm -rf /install
RUN mkdir -p /app
WORKDIR /app
COPY ./script/test.py .