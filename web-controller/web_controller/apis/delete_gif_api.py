from flask import request, jsonify
from flask import current_app as app
from ..utils.minio_update import MINIO_UPDATE

REQUIRED = "this field is required"

@app.route("/api/delete-gif", methods=['POST'])
def delete_gif():
    body = request.json
    if (body is None or body.get("bucket_name", None) is None or body.get("file_name", None) is None):
        return jsonify(error={"bucket_name": REQUIRED, "file_name": REQUIRED})
    bucket_name = body.get("bucket_name")
    file_name = body.get("file_name")
    try:
        MINIO_UPDATE.delete_file(bucket_name, file_name)
        return jsonify(success=True)
    except Exception as e:
        return jsonify(error=str(e))


@app.route("/api/delete-all-gifs", methods=['POST'])
def delete_all_gifs():
    body = request.json
    if (body is None or body.get("bucket_name", None) is None):
        return jsonify(error={"bucket_name": REQUIRED})
    bucket_name = body.get("bucket_name")
    try:
        MINIO_UPDATE.delete_all_files(bucket_name)
        return jsonify(success=True)
    except Exception as e:
        return jsonify(error=str(e))