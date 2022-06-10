from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

db = SQLAlchemy()

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