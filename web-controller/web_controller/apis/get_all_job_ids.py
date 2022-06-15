from flask import request, jsonify
from flask import current_app as app
from web_controller.model import Job


@app.route("/api/get-job-ids", methods=['GET', 'POST'])
def get_all_job_ids():
	request_job = request.json
	if (request_job is None or request_job.get("input_filename") == None):
		return jsonify(input_filename="This field is required")
	input_filename = request_job.get("input_filename")
	jobs = Job.query.filter_by(input_filename=input_filename).all()
	return jsonify(all_jobs=[job.id for job in jobs])