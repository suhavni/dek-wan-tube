from rq import Connection, Worker, Queue

from utility import RedisResource

QUEUES = ['extract', 'composer']

if __name__ == '__main__':
    with Connection(RedisResource.conn):
        w = Worker(map(Queue, QUEUES))
        w.work()