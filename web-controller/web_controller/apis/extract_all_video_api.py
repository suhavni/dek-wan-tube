from flask import request, jsonify
from flask import current_app as app
from web_controller import *
# from web_controller.model import Job
from web_controller.utils.work_queue import send_to_worker
from web_controller import MinioConnect
import mimetypes
mimetypes.init()


@app.route("/api/submit-all-videos", methods=['POST', 'GET'])
def submit_all_videos():
	# submit job to work queue
	bucket = request.json
	# serializer-like
	if (bucket is None or bucket.get("bucket_name",None) is None):
		return jsonify(error={"bucket_name": "this field is required"})

	request_bucket_name = bucket.get("bucket_name")
	minio_connector = MinioConnect.minio_client
	# check if bucket exists
	if (not minio_connector.bucket_exists(request_bucket_name)):
		return jsonify(title=f"Bucket {request_bucket_name} not found")
	# list all files in bucket
	bucket_objects = minio_connector.list_objects(request_bucket_name, recursive=True)
	job_ids = []
	for file in bucket_objects:
		file_name = file.object_name
		mimetype = mimetypes.guess_type(file_name)[0]
		if (mimetype):
			mimetype = mimetype.split('/')[0]
			if (mimetype == 'video'):
				body = {
					"input_file": file_name,
					"output_file": file_name.removesuffix(".mp4") + ".gif"
				}
				job_id = send_to_worker(body)
				job_ids.append(job_id)
	return jsonify(job_ids=job_ids)