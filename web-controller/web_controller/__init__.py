from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from minio import Minio
import os
from redis import Redis
from rq import Queue
# from .apis import submit_job_api

db = SQLAlchemy()

class RedisResource:
    REDIS_QUEUE_LOCATION = os.getenv('REDIS_QUEUE', 'localhost')
    host, *port_info = REDIS_QUEUE_LOCATION.split(':')
    port = tuple()
    if port_info:
        port, *_ = port_info
        port = (int(port),)

    conn = Redis(host=host, *port)
    extract_queue = Queue('extract', connection=conn)
    composer_queue = Queue('composer', connection=conn)

class MinioConnect:
	minio_client = Minio(
		os.getenv("MINIO_ENDPOINT", "127.0.0.1:9000"),
		access_key="pkinwza",
		secret_key="saobangpho1234",
		secure=False
	)


def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object("config.Config")

	# print(MinioConnect.minio_client.list_buckets())

	db.init_app(app)
	with app.app_context():
		from .model import Job
		# from . import apis

		db.create_all()

	return app
if __name__ == '__main__':
	app = create_app()
	app.run(host='0.0.0.0')