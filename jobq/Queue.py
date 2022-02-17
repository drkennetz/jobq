from collections import deque
import logging

class JobQueue(object):
    """ Creates or adds to a named job queue.
    Args:
        queuename (str): The name of the queue to initiate
    """

    def __init__(self, queuename):
        self.logger = logging.basicConfig(format='%(levelname)s:$(message)s', level=logging.DEBUG)
        self.queuename = queuename

    def check_for_queue(self):
        """ checks for existence of existing named queue """
        return 

    def add_job(self, job):
        """ Adds a job to the queue """
        self.logger.info(f'Adding job to the queue: {job}')
        self.queue.append(job)

    def get_next_job(self):
        """ gets the next job from the queue and returns it """
        job = self.queue.popleft()
        self.logger.info(f'got next job {job} from queue')

    def requeue_to_front(self, job):
        """ requeues job to front of queue """
        self.queue.appendleft(job)