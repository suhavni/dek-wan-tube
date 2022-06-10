from flask import request
from worker_utility import RedisResource, worker

def send_to_worker():
    body = request.json
    in_filename = body.get('input_file', 'input.mp4')
    out_filename = body.get('output_file', 'output.mp4')

    RedisResource.extract_queue.enqueue_call(worker, args=[in_filename, out_filename])