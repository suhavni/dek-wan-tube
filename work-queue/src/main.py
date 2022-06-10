from flask import Flask, jsonify, request
from utility import RedisResource, worker

app = Flask(__name__)


# FIXME: this is actually part of the web controller, 
# fix the file structure so this is with web controller
@app.route('/wq/extract', methods=['POST'])
def extract_and_resize():
    body = request.json
    in_filename = body.get('input_file', 'input.mp4')
    out_filename = body.get('output_file', 'output.mp4')

    RedisResource.extract_queue.enqueue_call(worker, args=[in_filename, out_filename])
    return jsonify({'status': 'OK'})