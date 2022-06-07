import os
import json
from redis import Redis
from rq import Queue, Connection, Worker
from flask import Flask, jsonify, request


app = Flask(__name__)

class RedisResource:
    # REDIS_QUEUE_LOCATION = os.getenv('REDIS_QUEUE', 'localhost')
    REDIS_QUEUE_LOCATION = 'localhost'
    host, *port_info = REDIS_QUEUE_LOCATION.split(':')
    port = tuple()
    if port_info:
        port, *_ = port_info
        port = (int(port),)

    conn = Redis(host=host, *port)
    queue = Queue(connection=conn)
    
def extract(body):
    print("this is extract and resize worker")

def gif_composer(body):
    print("this is gif composer worker")

def spawn_process(body):
    pid = os.fork()
    if pid < 0:
        os._exit(-1)
    elif not pid:
        try:
            print('enqueueing task')
            worker = RedisResource.queue.enqueue(extract, body)
            RedisResource.queue.enqueue(gif_composer, body, depends_on=worker)
            os._exit(0)
        except:
            print("bad command\n")
            os._exit(-1)
    else:
        pid = os.waitpid(pid, 0)


@app.route('/wq/extract', methods=['POST'])
def extract_and_resize():
    body = request.json
    spawn_process(body)
    # new_pid = os.fork()
    # if new_pid == 0:
    #     RedisResource.queue.enqueue(dummy_func, body)
    
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    with Connection(RedisResource.conn):
        print('connected')
        w = Worker(['default'])
        w.work()

# @app.route('/wq/gif-composer', methods=['POST'])
# def gif_composer():
#     body = request.json
#     add_to_wq(body, RedisResource.GIF_COMPOSER)
    
#     return jsonify({'status': 'OK'})