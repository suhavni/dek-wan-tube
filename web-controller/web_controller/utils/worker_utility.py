import os
import logging
# from redis import Redis
# from rq import Queue
import subprocess
import sys
import web_controller

LOG = logging


def extract_worker(in_filename, out_filename):
    # FIXME: make the file work such that it takes input from MinIO and outputs into MinIO
    process = subprocess.Popen(f'python ../resources/main.py extract {in_filename} {out_filename}', shell=True)

    # TODO: update status in database -> started process extract images from video

    return_code = process.wait()

    if return_code == os.EX_OK:
        # TODO: update status in database -> extracted images from video successful
        web_controller.RedisResource.composer_queue.enqueue_call(compose_worker, args=[in_filename, out_filename])
    else:
        _, err = process.communicate()
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
        _, err = process.communicate()
        err = err.decode(sys.stdin.encoding)
        # TODO: update status in database -> error occured when composing gif (err, return_code)