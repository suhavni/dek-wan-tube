from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_minio import Minio
import os

db = SQLAlchemy()
minio = Minio(
	os.getenv("MINIO_ENDPOINT", "localhost"),
	access_key=os.getenv("MINIO_ACCES_KEY", "pkinwza"),
	secret_key=os.getenv("MINIO_SECRET_KEY", "saobangpho1234")
)

def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object("config.Config")

	db.init_app(app)
	with app.app_context():
		from .model import Job
		from . import apis

		db.create_all()

	return app
if __name__ == '__main__':
	app = create_app()
	app.run(host='0.0.0.0')