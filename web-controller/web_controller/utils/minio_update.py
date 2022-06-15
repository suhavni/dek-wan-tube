import base64
from minio import Minio
import os

# needs to be in this file as well
class MinioConnect:
	minio_client = Minio(
		os.getenv("MINIO_ENDPOINT", "127.0.0.1:9000"),
		access_key=os.getenv("MINIO_ACCES_KEY","pkinwza"),
		secret_key=os.getenv("MINIO_SECRET_KEY","saobangpho1234"),
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

    def upload_file(self, bucket_name, file_name, job_id, content_type=None, metadata=None):
        self.minio_client.fput_object(
            bucket_name,
            f'{job_id}{file_name}',
            f'./tmp/{job_id}{file_name}',
            content_type=content_type,
            metadata=metadata
        )

    def delete_file(self, bucket_name, file_name):
        print(f'deleting {file_name} from {bucket_name}')
        
        self.minio_client.remove_object(
            bucket_name,
            file_name
        )
    
    def delete_all_files(self, bucket_name):
        try:
            [self.delete_file(bucket_name, f.object_name) for f in self.minio_client.list_objects(bucket_name, recursive=True)]
        except Exception as e:
            print(e)

    def get_binary_data(self, bucket_name, file_name, mimetype=None):
        if bucket_name == "gif": 
            content_type = "image/gif"
        elif mimetype is None:
             content_type = "video/mp4"
        else:
            content_type = mimetype
        data = self.minio_client.get_object( 
            bucket_name, 
            file_name,
        )
        return f"data:{content_type};base64,{base64.b64encode(data.read()).decode('utf-8')}"

MINIO_UPDATE = MinioUpdate()