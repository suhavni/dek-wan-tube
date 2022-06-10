from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_minio import Minio
import os
from redis import Redis
from rq import Queue


# Connect job database, minio server, redis server
db = SQLAlchemy()
minio_client = Minio()

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

def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object("config.Config")

	minio_client = Minio(
		os.getenv("MINIO_ENDPOINT", "localhost"),
		access_key=os.getenv("MINIO_ACCES_KEY", "pkinwza"),
		secret_key=os.getenv("MINIO_SECRET_KEY", "saobangpho1234")
	)

	db.init_app(app)
	with app.app_context():
		from .model import Job
		from . import apis

		db.create_all()

	return app
if __name__ == '__main__':
	app = create_app()
	app.run(host='0.0.0.0')