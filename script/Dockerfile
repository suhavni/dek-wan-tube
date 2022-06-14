FROM python:3.9.13-alpine3.15 as build-stage
RUN mkdir -p /install
WORKDIR /install
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
# RUN apk add --no-cache build-base
RUN pip install --no-cache-dir --prefix=/install ffmpeg-python

FROM python:3.9.13-alpine3.15 as production-stage
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apk add --no-cache --update --virtual build-dependencies ffmpeg imagemagick
COPY --from=build-stage /install /usr/local
RUN rm -rf /install
RUN mkdir -p /app
WORKDIR /app
COPY ./docker-entrypoint.sh ./
RUN chmod +x docker-entrypoint.sh
COPY ./src/*.py ./
ENTRYPOINT [ "./docker-entrypoint.sh" ]