from rq import Connection, Worker

from web_controller.utils.worker_utility import RedisResource

if __name__ == '__main__':
    with Connection(RedisResource.conn):
        w = Worker(['composer'])
        w.work()