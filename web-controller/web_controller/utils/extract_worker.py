from .worker_utility import RedisResource, update_status_worker
from .compose_worker import compose_worker
from .minio_update import MINIO_UPDATE
import subprocess
import os

def get_output(in_filename: str) -> str:
    try:
        return "/".join(in_filename.split('/')[:-1]) + 'Image'
    except:
        return 'Image'


def extract_complete(in_filename, out_filename, job_id, started_log):
    extracted_log = RedisResource.update_status_queue.enqueue_call(
        update_status_worker, 
        args=[job_id, "Finished extracting frames. Uploading to MinIO."],
        depends_on=started_log
    )
    
    [MINIO_UPDATE.upload_file('frames', f'{get_output(in_filename)}{i:02d}.jpg', f'{job_id}/') for i in range(60)]

    uploaded_log = RedisResource.update_status_queue.enqueue_call(
        update_status_worker, 
        args=[job_id, "Uploaded frames to MinIO. Sending to GIF Composer."],
        depends_on=extracted_log
    )

    RedisResource.composer_queue.enqueue_call(
        compose_worker, 
        args=[in_filename, out_filename, job_id, uploaded_log.id]
    )

    subprocess.run(f'rm -rf ./tmp/{job_id}', shell=True)


def download_and_extract(in_filename, out_filename, job_id):
    print('submitting status update: Downloading video')
    downloading_log = RedisResource.update_status_queue.enqueue_call(
        update_status_worker, 
        args=[job_id, "Downloading video from MinIO"]
    )
    MINIO_UPDATE.download_file('video', in_filename, f'{job_id}/')
    
    process = subprocess.Popen(f'python ../script/src/main.py extract ./tmp/{job_id}/{in_filename} ./tmp/{job_id}/{out_filename}', shell=True)
    
    started_log = RedisResource.update_status_queue.enqueue_call(
        update_status_worker, 
        args=[job_id, "Started extracting frames"],
        depends_on=downloading_log
    )

    return_code = process.wait()
    return return_code, started_log.id
    

def extract_worker(in_filename, out_filename, job_id):
    return_code, started_log = download_and_extract(in_filename, out_filename, job_id)
    if return_code == os.EX_OK:
        extract_complete(in_filename, out_filename, job_id, started_log)
    else:
        RedisResource.update_status_queue.enqueue_call(
            update_status_worker, 
            args=[job_id, f"There was an error while extracting frames. Exit code: {return_code}"],
            depends_on=started_log)