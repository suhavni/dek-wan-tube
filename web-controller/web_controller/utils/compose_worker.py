from .worker_utility import RedisResource, update_status_worker
import subprocess
import os
from .minio_update import MINIO_UPDATE

def compose_complete(out_filename, job_id, started_log):
    composed_log = RedisResource.update_status_queue.enqueue_call(
        update_status_worker, 
        args=[job_id, "Finished composing GIF. Uploading to MinIO."],
        depends_on=started_log
    )

    MINIO_UPDATE.upload_file('gif', f'{job_id}/{out_filename}', '', content_type='image/gif', metadata={'ContentType': 'image/gif', 'Content-Type': 'image/gif'})

    RedisResource.update_status_queue.enqueue_call(
        update_status_worker,
        args=[job_id, "Uploaded GIF to MinIO."],
        depends_on=composed_log
    )

    subprocess.run(f'rm -rf ./tmp/{job_id}', shell=True)

def download_and_compose(in_filename, out_filename, job_id, dependency):
    downloading_log = RedisResource.update_status_queue.enqueue_call(
        update_status_worker, 
        args=[job_id, "Downloading extracted frames from MinIO"],
        depends_on=dependency
    )

    [MINIO_UPDATE.download_file('frames', f'{job_id}/Image{i:02d}.jpg', '') for i in range(60)]

    process = subprocess.Popen(f'python ../script/src/main.py gif_composer tmp/{job_id}/{in_filename} tmp/{job_id}/{out_filename}', shell=True)

    started_log = RedisResource.update_status_queue.enqueue_call(
        update_status_worker, 
        args=[job_id, "Started composing GIF"],
        depends_on=downloading_log
    )

    return_code = process.wait()
    return return_code, started_log.id

def compose_worker(in_filename, out_filename, job_id, dependency):
    return_code, started_log = download_and_compose(in_filename, out_filename, job_id, dependency)

    if return_code == os.EX_OK:
        compose_complete(out_filename, job_id, started_log)
    else:
        RedisResource.update_status_queue.enqueue_call(
            update_status_worker, 
            args=[job_id, f"There was an error while composing GIF. Exit code: {return_code}"],
            depends_on=started_log
        )