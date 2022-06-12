from flask import request, jsonify
from flask import current_app as app
from web_controller import *
from web_controller.model import Job


@app.route("/api/update-database", methods=['POST'])
def update_database():
	job_detail = request.json
	# serializer-like
	if (job_detail is None):
		return jsonify(error={"title": "Json body is required"})
	elif (job_detail.get("id", None) is None):
		return jsonify(error={"id": "this field is required"})
	elif (job_detail.get("status", None) is None):
		return jsonify(error={"status": "this field is required"})
	# submit job to work queue
	job = Job.query.get(int(job_detail.get("id")))
	job.status = job_detail.get("status")

	db.session.commit()
	return jsonify(status="Updated", id=int(job_detail.get("id")))