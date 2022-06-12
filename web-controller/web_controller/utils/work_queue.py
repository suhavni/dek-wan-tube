from flask import request
from .worker_utility import extract_worker, RedisResource
# from worker_utility import RedisResource
from web_controller.model import Job
from web_controller import db

def send_to_worker(body):
    # body = request.json
    in_filename = body.get('input_file', 'input.mp4')
    out_filename = body.get('output_file', 'output.mp4')
    RedisResource.extract_queue.enqueue_call(extract_worker, args=[in_filename, out_filename])

    # connect to database
    job = Job(
        status = "Sent to Extract Worker", 
        input_filename = in_filename,
        output_filename = out_filename
    )
    db.session.add(job)
    db.session.commit()
    return job.id

