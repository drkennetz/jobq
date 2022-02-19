"""
The function warehouse for jobq
"""

import logging
import zmq

from jobq import Server

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(process)d-%(levelname)s:%(message)s', level=logging.DEBUG)

def start_server(args):
    server = Server.Server(args.port)
    server.set_socket()
    server.bind_to_port()
    while True:
        logging.info(f' listening on port: {args.port}')
        message = server.socket.recv()
        message = message.decode('utf-8')
        logging.info(f' received message: {message}')
        server.socket.send_string(f' Processed {message}')

def client_message(args):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    logging.info(' Pid should be different, starting client')
    socket.connect(f"tcp://localhost:{args.port}")
    logging.info(f' Sending message {args.message}')
    socket.send(args.message.encode('utf-8'))
    message = socket.recv()
    message = message.decode('utf-8')
    logging.info(f" Received reply {message}")
                
def submit(args):
    print(args.cmd)
