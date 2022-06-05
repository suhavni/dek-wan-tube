import os
import json
import redis
from flask import Flask, jsonify, request


app = Flask(__name__)

class RedisResource:
    REDIS_QUEUE_LOCATION = os.getenv('REDIS_QUEUE', 'localhost')
    EXTRACT_AND_RESIZE = 'queue:extract'
    GIF_COMPOSER = 'queue:gif_composer'

    host, *port_info = REDIS_QUEUE_LOCATION.split(':')
    port = tuple()
    if port_info:
        port, *_ = port_info
        port = (int(port),)

    conn = redis.Redis(host=host, *port)

def add_to_wq(body, redis_resource):
    json_packed = json.dumps(body)
    print('packed:', json_packed)
    RedisResource.conn.rpush(
        redis_resource,
        json_packed)

@app.route('/wq/extract', methods=['POST'])
def extract_and_resize():
    body = request.json
    add_to_wq(body, RedisResource.EXTRACT_AND_RESIZE)
    
    return jsonify({'status': 'OK'})

@app.route('/wq/gif-composer', methods=['POST'])
def gif_composer():
    body = request.json
    add_to_wq(body, RedisResource.GIF_COMPOSER)
    
    return jsonify({'status': 'OK'})