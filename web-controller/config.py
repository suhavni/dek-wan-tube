import os

class Config:
	SQLALCHEMY_DATABASE_URI = os.getenv("FLASK_DATABASE_URI", "mariadb+pymysql://saobangpho:scp1234@localhost:3306/scalable-p2-jobs")
	SQLALCHEMY_ECHO = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
