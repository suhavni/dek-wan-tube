import os
import logging
from redis import Redis
from rq import Queue
import subprocess
import sys

LOG = logging

class RedisResource:
    REDIS_QUEUE_LOCATION = os.getenv('REDIS_QUEUE', 'localhost')
    host, *port_info = REDIS_QUEUE_LOCATION.split(':')
    port = tuple()
    if port_info:
        port, *_ = port_info
        port = (int(port),)

    conn = Redis(host=host, *port)
    extract_queue = Queue('extract', connection=conn)
    composer_queue = Queue('composer', connection=conn)

def extract_worker(in_filename, out_filename):
    # FIXME: make the file work such that it takes input from MinIO and outputs into MinIO
    process = subprocess.Popen(f'python ../resources/main.py extract {in_filename} {out_filename}', shell=True)

    # TODO: update status in database -> started process extract images from video

    return_code = process.wait()

    if return_code == os.EX_OK:
        # TODO: update status in database -> extracted images from video successful
        RedisResource.composer_queue.enqueue_call(compose_worker, args=[in_filename, out_filename])
    else:
        err = err.decode(sys.stdin.encoding)
        # TODO: update status in database -> error occured when extracting image (err, return_code)
    
def compose_worker(in_filename, out_filename):
    # FIXME: make the file work such that it takes input from MinIO and outputs into MinIO
    process = subprocess.Popen(f'python ../resources/main.py gif_composer {in_filename} {out_filename}', shell=True)

    # TODO: update status in database -> started process composing images to gif

    return_code = process.wait()

    if return_code == os.EX_OK:
        # TODO: update status in database -> composed images to gif successful
        pass
    else:
        err = err.decode(sys.stdin.encoding)
        # TODO: update status in database -> error occured when composing gif (err, return_code)
    

def worker(function, body):
    in_filename = body.get('input_file', 'input.mp4')
    out_filename = body.get('output_file', 'output.mp4')

    process = subprocess.Popen(f'python ../resources/main.py {function} {in_filename} {out_filename}', shell=True)

    return_code = process.wait()


    if return_code == os.EX_OK and function == 'extract':
        RedisResource.composer_queue.enqueue_call(worker, args=['gif_composer', body])
    elif return_code == os.EX_OK:
        pass
    else:
        err = err.decode(sys.stdin.encoding)
        return return_code, err
    return return_code, 'OK'
