from . import MinioUpdate, RedisResource

MINIO_UPDATE = MinioUpdate()
     

def update_status_worker(job_id, status):
    import requests
    requests.post(f'http://localhost:5000/api/update-database', json={'id': job_id, 'status': status})