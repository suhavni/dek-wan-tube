import os
from redis import Redis
from rq import Queue
from .. import MinioConnect

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
    update_status_queue = Queue('update_status', connection=conn, is_async=False)

class MinioUpdate:
    minio_client = MinioConnect.minio_client

    def download_file(self, bucket_name, file_name, job_id):
        self.minio_client.fget_object(
            bucket_name,
            file_name,
            f'/tmp/{job_id}/{file_name}'
        )

    def add_folder(self, bucket_name, folder_name):
        self.minio_client.make_bucket(bucket_name)
        self.minio_client.make_bucket(f'{bucket_name}/{folder_name}')

    def upload_file(self, bucket_name, file_name, job_id):
        self.minio_client.fput_object(
            bucket_name,
            file_name,
            f'/tmp/{job_id}/{file_name}'
        )

    def delete_file(self, bucket_name, file_name):
        self.minio_client.remove_object(
            bucket_name,
            file_name
        )
    
    def delete_folder(self, bucket_name, folder_name):
        self.minio_client.remove_bucket(f'{bucket_name}/{folder_name}')