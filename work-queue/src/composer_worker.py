from rq import Connection, Worker

from utility import RedisResource

if __name__ == '__main__':
    with Connection(RedisResource.conn):
        w = Worker(['composer'])
        w.work()