from flask import request
from .worker_utility import extract_worker, RedisResource
# from worker_utility import RedisResource

def send_to_worker(body):
    # body = request.json
    in_filename = body.get('input_file', 'input.mp4')
    out_filename = body.get('output_file', 'output.mp4')

    RedisResource.extract_queue.enqueue_call(extract_worker, args=[in_filename, out_filename])