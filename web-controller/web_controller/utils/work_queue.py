from .extract_worker import extract_worker, RedisResource
from web_controller.model import Job
from web_controller import db

def send_to_worker(body):
    in_filename = body.get('input_file', 'input.mp4')
    out_filename = body.get('output_file', 'output.mp4')

    # connect to database
    job = Job(
        status = "Sent to Extract Worker", 
        input_filename = in_filename,
        output_filename = out_filename
    )
    db.session.add(job)
    db.session.commit()

    RedisResource.extract_queue.enqueue_call(extract_worker, args=[in_filename, out_filename, job.id])
    return job.id

