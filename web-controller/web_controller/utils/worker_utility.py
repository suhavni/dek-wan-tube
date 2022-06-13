from . import RedisResource
import os

host = os.getenv('WC_HOST', '0.0.0.0')
port = os.getenv('WC_PORT', 5000)

def update_status_worker(job_id, status):
    import requests
    requests.post(f'http://{host}:{port}/api/update-database', json={'id': job_id, 'status': status})