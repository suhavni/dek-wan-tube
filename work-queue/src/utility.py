import os
import logging
from redis import Redis
from rq import Queue

LOG = logging

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

def worker(function, body):
    in_filename = body.get('input_file', 'input.mp4')
    out_filename = body.get('output_file', 'output.mp4')

    os.system(f'python ..resources/main.py {function} {in_filename} {out_filename}')
    if function == 'extract': 
        RedisResource.composer_queue.enqueue_call(worker, args=['gif_composer', body])
    
    
    # It already forks anyway
    # ------------------------
    # python_cmd = ['python', '../resources/main.py', function, in_filename, out_filename]
    # pid = os.fork()
    #     os._exit(-1)
    # elif not pid:
    #     os.execvp(python_cmd[0], python_cmd)
    #     LOG.exception("bad command")
    #     os._exit(-1)
    # else:
    #     pid = os.waitpid(pid, 0)