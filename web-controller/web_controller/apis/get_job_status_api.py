from flask import request, jsonify
from flask import current_app as app
from web_controller.model import Job
import mimetypes
mimetypes.init()


@app.route("/api/get-job-status", methods=['GET'])
def get_job_status():
	request_job = request.json
	if (request_job is None or request_job.get("job_id") == None):
		return jsonify(job_id="This field is required")
	job_id = int(request_job.get("job_id"))
	job = Job.query.get(job_id)
	if (job == None):
		return jsonify(status=f"Job {job_id} does not exist")
	return jsonify(status=job.status)