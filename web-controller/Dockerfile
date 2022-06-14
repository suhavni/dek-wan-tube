# Build upon this image "alpine" is a lightweight distro
FROM python:3.9.13-alpine3.15 as build-stage

WORKDIR /install
# Install all the requirements
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1
COPY ./web_controller/requirements.txt ./

RUN apk add build-base
RUN pip install --prefix=/install -r requirements.txt


# Stage 2
FROM python:3.9.13-alpine3.15 as production-stage

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=build-stage /install /usr/local
RUN rm -rf /install

# Copy everthing from . to /app inside the 'box'

COPY ./config.py /app/config.py
COPY ./web_controller /app/web_controller
WORKDIR /app

# How to run it when we start up the box?
ENTRYPOINT ["gunicorn", "-b 0.0.0.0:5000", "-w 2", "web_controller.wsgi:app"]