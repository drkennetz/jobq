import logging
import sys
import zmq

from jobq import NamedQueues
from jobq import utilities

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
        self.password = ""
        super().__init__()

    def set_server_password(self):
        """ Hashes a crypto password [or None]."""
        self.password = utilities.enter_password()

    def set_socket(self):
        """Creates the Reply socket"""
        self.socket = self.context.socket(zmq.REP)
        logging.info(f' created reply socket')

    def bind_to_port(self):
        """Binds the socket to a port by which to communicate"""
        self.socket.bind(f'tcp://127.0.0.1:{self.port}')
        logging.info(f' bound socket to port: {self.port}')

    def kill_server(self, password):
        """Kills a running server"""
        if self.password == "":
            self.socket.unbind(f'tcp://127.0.0.1:{self.port}')
            sys.exit("User has sent kill command... Shutting down.")
        else:
            valid = utilities.validate_password(password, self.password)
            if valid:
                self.socket.unbind(f'tcp://127.0.0.1:{self.port}')
                sys.exit("User has sent kill command with valid password... Shutting down.")
            else:
                return "Invalid password for server"

    def handle_message(self, message):
        """Does the appropriate thing with message received"""
        command = message["command"]
        print(command)
        logging.info(f' processing message: {command}')
        messages = dict({
            "check_for_queue": (self.check_for_queue, ((message["queuename"]))),
            "add_job_to_queue": (self.add_job_to_queue, ((message["queuename"], message["job"]))),
            "requeue_to_front": (self.requeue_to_front, ((message["queuename"], message["job"]))),
            "init_queue": (self.init_queue, ((message["queuename"]))),
            "list_queues": (self.list_queues,),
            "kill_server": (self.kill_server, ((message["password"])))})
        fn, args = messages.get(command)
        if args:
            fn(*args)
        else:
            fn()
                        
        
            
