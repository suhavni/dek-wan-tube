from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from minio import Minio
import os
from redis import Redis
from rq import Queue
# from .apis import submit_job_api

db = SQLAlchemy()

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
		# from .model import Job
		from .apis import submit_job_api, update_database_api, extract_all_video_api, gif_list_api

		db.create_all()

	return app
if __name__ == '__main__':
	app = create_app()
	app.run(host='0.0.0.0')