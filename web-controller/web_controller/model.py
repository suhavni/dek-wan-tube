from . import db
from datetime import datetime

class Job(db. Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	job_id = db.Column(db.Integer, nullable = False)
	input_filename = db.Column(db.Text, nullable = False)
	output_filename = db.Column(db.Text, nullable = False)