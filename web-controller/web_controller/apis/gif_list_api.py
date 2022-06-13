from flask import request, jsonify
from flask import current_app as app
from web_controller import *
from web_controller import MinioConnect
import mimetypes
mimetypes.init()


@app.route("/api/gif-list", methods=['GET'])
def list_gif_files():
	request_bucket = request.json
	if (request_bucket is None or request_bucket.get("bucket_name", None) is None):
		return jsonify(bucket_name="This field is required")
	request_bucket_name = request_bucket.get("bucket_name")
	minio_connector = MinioConnect.minio_client
	if (not minio_connector.bucket_exists(request_bucket_name)):
		return jsonify(title=f"Bucket {request_bucket_name} not found")
	# list all files in bucket
	bucket_objects = minio_connector.list_objects(request_bucket_name, recursive=True)
	gif_files = []
	for file in bucket_objects:
		file_name = file.object_name
		mimetype = mimetypes.guess_type(file_name)[0]
		if (mimetype):
			if (mimetype == 'image/gif'):
				gif_files.append(file_name)
	return jsonify(file_names=gif_files)