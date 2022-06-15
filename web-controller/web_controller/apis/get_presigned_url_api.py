from re import I
from flask import request, jsonify
from flask import current_app as app
from ..utils.minio_update import MINIO_UPDATE


@app.route("/api/get-binary-data", methods=['GET', 'POST'])
def get_presigned_url():
    body = request.json
    if (body is None or body.get("bucket_name", None) is None or body.get("file_name", None) is None):
        return jsonify(error={"bucket_name": "this field is required", "file_name": "this field is required"})
    bucket_name = body.get("bucket_name")
    file_name = body.get("file_name")
    try:
        binary = MINIO_UPDATE.get_binary_data(bucket_name, file_name)
        return jsonify(binary_data=binary)
    except Exception as e:
        return jsonify(error=str(e))