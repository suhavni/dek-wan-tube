from flask import request, jsonify
from flask import current_app as app
from web_controller import *
from web_controller import MinioConnect
import mimetypes
mimetypes.init()


@app.route("/api/gif-list", methods=['GET'])
def list_gif_files():
	minio_connector = MinioConnect.minio_client
	# list all files in bucket
	bucket_objects = minio_connector.list_objects("gif", recursive=True)
	gif_files = []
	for file in bucket_objects:
		file_name = file.object_name
		mimetype = mimetypes.guess_type(file_name)[0]
		if (mimetype):
			if (mimetype == 'image/gif'):
				gif_files.append(file_name)
	return jsonify(file_names=gif_files)