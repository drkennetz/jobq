from collections import deque
import logging

class NamedQueues(object):
    """ Creates or adds to a named job queue.
    Attributes:
        queues - the different queues for jobs
        pids - the process ids {pid: 'job string'}
    """

    def __init__(self):
        logging.basicConfig(format='%(process)d-%(levelname)s:%(message)s', level=logging.DEBUG)
        self.queues = {}
        self.pids = {}

    def check_for_queue(self, queuename):
        """ checks for existence of existing named queue """
        logging.info(f' Checking for existing queue: {queuename}')
        if queuename in self.queues:
            logging.info(f' Found queue in queues: {queuename}')
        else:
            logging.warning(f' Did not find queue in queues: {queuename}')

    def add_job_to_queue(self, queuename, job):
        """ Adds a job to the queue """
        logging.info(f' Adding job to the queue {queuename}: {job}')
        self.queues[queuename].append(job)

    def get_next_job_in_queue(self, queuename):
        """ gets the next job from the queue and returns it """
        job = self.queues[queuename].popleft()
        logging.info(f' Got next job {job} from queue {queuename}')
        return job

    def requeue_to_front(self, queuename, job):
        """ requeues job to front of queue """
        self.queues[queuename].appendleft(job)

    def init_queue(self, queuename):
        """ initializes a new queue """
        if queuename in self.queues:
            raise QueueExistsError(queuename)
        self.queues[queuename] = deque()

class NamedQueuesError(Exception):
    """Base class for other exceptions"""
    pass

class QueueExistsError(NamedQueuesError):
    """Exception raised for errors when queue already exists.
    Attributes:
        queuename -- the queue name that exists
        message -- explanation of the error
    """
    def __init__(self, queuename, message="NamedQueue already exists in queues."):
        self.queuename = queuename
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.queuename} -> {self.message}'
    
