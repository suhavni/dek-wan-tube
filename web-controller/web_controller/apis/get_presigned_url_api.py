from re import I
from flask import request, jsonify
from flask import current_app as app
from ..utils.minio_update import MINIO_UPDATE


@app.route("/api/get-presigned-url", methods=['GET', 'POST'])
def get_presigned_url():
    body = request.json
    if (body is None or body.get("bucket_name", None) is None or body.get("file_name", None) is None):
        return jsonify(error={"bucket_name": "this field is required", "file_name": "this field is required"})
    bucket_name = body.get("bucket_name")
    file_name = body.get("file_name")
    try:
        presigned_url = MINIO_UPDATE.get_presigned_url(bucket_name, file_name)
        response = _http.urlopen('GET', presigned_url)
        return jsonify(resp=response, presigned_url=presigned_url)
    except Exception as e:
        return jsonify(error=str(e))