import logging
import zmq

from jobq import NamedQueues

class Server(NamedQueues.NamedQueues):
    """ A Server object manage Queue requests
    Attributes:
        context: a ZeroMQ context  
        port: The port by which to communicate over tcp
    """
    def __init__(self, port, context=zmq.Context()):
        self.context = context
        self.port = port
        self.socket = None
        NamedQueues.__init__(self)

    def set_socket(self):
        """Creates the Reply socket"""
        self.socket = self.context.socket(zmq.REP)
        logging.info(f' created reply socket')

    def bind_to_port(self, port):
        """Binds the socket to a port by which to communicate"""
        self.socket.bind(f'tcp://*:{self.port}')
        logging.info(f' bound socket to port: {port}')

    def handle_message(self, message, queuename='', job=''):
        """Does the appropriate thing with message received"""
        messages = {
            'check_for_queue': self.check_for_queue(queuename),
            'add_job_to_queue': self.add_job_to_queue(queuename, job),
            'requeue_to_front': self.requeue_to_front(queuename, job),
            'init_queue': self.init_queue(queuename),
            'list_queues': self.list_queues()
            },
        messages[message]
    
