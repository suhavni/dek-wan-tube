from flask import Flask, jsonify, request
from utility import RedisResource, worker

app = Flask(__name__)

@app.route('/wq/extract', methods=['POST'])
def extract_and_resize():
    body = request.json
    extract_worker = RedisResource.queue.enqueue_call(worker, args=['extract', body])
    RedisResource.queue.enqueue(worker, args=['gif_composer', body], depends_on=extract_worker)
    return jsonify({'status': 'OK'})