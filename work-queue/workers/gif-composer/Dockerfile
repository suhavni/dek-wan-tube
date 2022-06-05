# Build upon this image "alpine" is a lightweight distro
FROM python:3.7-alpine

# Install all the requirements
RUN pip install flask gunicorn redis

# Copy everthing from . to /app inside the 'box'
COPY . /app
WORKDIR /app

# How to run it when we start up the box?
ENTRYPOINT ["python", "gif_composer_worker.py"]