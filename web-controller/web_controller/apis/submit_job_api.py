from flask import request, jsonify
from flask import current_app as app
from web_controller import *
# from web_controller.model import Job
from web_controller.utils.work_queue import send_to_worker


@app.route("/submit-job", methods=['POST'])
def submit_job():
	job_detail = request.json
	# serializer-like
	if (job_detail is None):
		return jsonify(error={"title": "Json body is required"})
	elif (job_detail.get("input_file", None) is None):
		return jsonify(error={"input_file": "this field is required"})
	elif (job_detail.get("output_file", None) is None):
		return jsonify(error={"output_file": "this field is required"})
	# submit job to work queue
	job_id = send_to_worker(job_detail)

	return jsonify(job_id=job_id)