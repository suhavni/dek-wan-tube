from minio import Minio
import os

# needs to be in this file as well
class MinioConnect:
	minio_client = Minio(
		os.getenv("MINIO_ENDPOINT", "127.0.0.1:9000"),
		access_key="pkinwza",
		secret_key="saobangpho1234",
		secure=False
	)

class MinioUpdate:
    minio_client = MinioConnect.minio_client

    def download_file(self, bucket_name, file_name, job_id):
        self.minio_client.fget_object(
            bucket_name,
            file_name,
            f'./tmp/{job_id}{file_name}',
        )

    def add_folder(self, bucket_name, folder_name):
        self.minio_client.make_bucket(bucket_name)
        self.minio_client.make_bucket(f'{bucket_name}/{folder_name}')

    def upload_file(self, bucket_name, file_name, job_id):
        print(f'Uploading {file_name} to {bucket_name}')
        print(f'Job id: {job_id}')
        print(f'File path: ./tmp/{job_id}/{file_name}')
        print(f'File name: {job_id}{file_name}')
        self.minio_client.fput_object(
            bucket_name,
            f'{job_id}{file_name}',
            f'./tmp/{job_id}{file_name}'
        )

    def delete_file(self, bucket_name, file_name):
        self.minio_client.remove_object(
            bucket_name,
            file_name
        )
    
    def delete_folder(self, bucket_name, folder_name):
        self.minio_client.remove_bucket(f'{bucket_name}/{folder_name}')

MINIO_UPDATE = MinioUpdate()