from flask import Flask, jsonify, request
from utility import RedisResource, worker

app = Flask(__name__)

@app.route('/wq/extract', methods=['POST'])
def extract_and_resize():
    body = request.json
    RedisResource.extract_queue.enqueue_call(worker, args=['extract', body])
    return jsonify({'status': 'OK'})