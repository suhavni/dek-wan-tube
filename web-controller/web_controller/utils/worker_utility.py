import os
import subprocess
import sys
from . import RedisResource, MinioUpdate

MINIO_UPDATE = MinioUpdate()

def extract_worker(in_filename, out_filename, job_id):
    RedisResource.update_status_queue.enqueue_call(update_status_worker, args=[job_id, "Downloading video"])
    MINIO_UPDATE.download_file('video', in_filename, job_id)
    
    process = subprocess.Popen(f'python ../resources/main.py extract tmp/{job_id}/{in_filename} tmp/{job_id}/{out_filename}', shell=True)
    RedisResource.update_status_queue.enqueue_call(update_status_worker, args=[job_id, "Started extracting frames"])

    return_code = process.wait()

    if return_code == os.EX_OK:
        RedisResource.update_status_queue.enqueue_call(update_status_worker, args=[job_id, "Finished extracting frames. Sending to GIF composer worker"])
        RedisResource.composer_queue.enqueue_call(compose_worker, args=[in_filename, out_filename, job_id])
    else:
        RedisResource.update_status_queue.enqueue_call(update_status_worker, args=[job_id, f"There was an error while extracting frames. Exit code: {return_code}"])
    
def compose_worker(in_filename, out_filename, job_id):
    process = subprocess.Popen(f'python ../resources/main.py gif_composer tmp/{job_id}/{in_filename} tmp/{job_id}/{out_filename}', shell=True)
    RedisResource.update_status_queue.enqueue_call(update_status_worker, args=[job_id, "Started composing GIF"])

    return_code = process.wait()

    if return_code == os.EX_OK:
        RedisResource.update_status_queue.enqueue_call(update_status_worker, args=[job_id, "Finished composing GIF."])
    else:
        RedisResource.update_status_queue.enqueue_call(update_status_worker, args=[job_id, f"There was an error while composing GIF. Exit code: {return_code}"])
     
def update_status_worker(job_id, status):
    import requests
    requests.post(f'http://localhost:5000/api/update-database', json={'id': job_id, 'status': status})