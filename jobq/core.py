"""
The function warehouse for jobq
"""

import logging
import zmq
from getpass import getpass

from jobq import Server, utilities

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(process)d-%(levelname)s:%(message)s', level=logging.DEBUG)

def start_server(args):
    server = Server.Server(args.port)
    if args.with_password:
        server.set_server_password()
    server.set_socket()
    server.bind_to_port()
    while True:
        logging.info(f' listening on port: {args.port}')
        message = server.socket.recv_json()
        logging.info(f' received message: {message["command"]}')
        server.socket.send_string(f' Response: {server.handle_message(message)}')

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
                
def kill_server(args):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://localhost:{args.port}")
    if args.with_password:
        password = getpass()
    else:
        password = ""
    logging.info(f' Sending message kill_server')
    send = {"command": "kill_server", "password": password, "queuename": "", "job": ""}
    socket.send_json(send)
    socket.disconnect(f"tcp://localhost:{args.port}")
    logging.info(f' Server on port {args.port} has been shutdown.')

def queueexists(args):
    pass

def showqueues(args):
    pass

def showjobs(args):
    pass

def submitjob(args):
    pass

