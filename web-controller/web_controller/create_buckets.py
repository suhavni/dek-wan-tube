from . import MinioConnect

minio_client = MinioConnect.minio_client

def create_bucket(bucket_name):
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)

buckets = ['video', 'frames', 'gif']

[create_bucket(bucket_name) for bucket_name in buckets]

import subprocess
try:
    output = subprocess.check_output("\ls --hide='t_*' resources/", shell=True)
    files = output.decode('utf-8').split('\n')
except Exception as err:
    files = []
    print(err)

for f in files:
    if f:
        minio_client.fput_object('video', f, f'resources/{f}')
