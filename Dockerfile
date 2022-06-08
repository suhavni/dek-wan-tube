# Build upon this image "alpine" is a lightweight distro
FROM python:3.9.13-alpine3.15 as build-stage

WORKDIR /install
# Install all the requirements
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1
RUN pip install --prefix=/install redis rq ffmpeg-python

# Stage 2
FROM python:3.9.12-alpine3.15 as production-stage

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk add --no-cache ffmpeg imagemagick
COPY --from=build-stage /install /usr/local
RUN rm -rf /install

# Copy everthing from . to /app inside the 'box'

COPY work-queue/src/worker.py /app/worker.py
COPY work-queue/src/utility.py /app/utility.py
COPY script/src/ /resources/
WORKDIR /app

# How to run it when we start up the box?
ENTRYPOINT ["python", "worker.py"]

# ENV FLASK_APP=main
# CMD ["flask", "run", "--host", "0.0.0.0"]