"""
The function warehouse for jobq
"""

import logging

from jobq import Server

logging.basicConfig(format='%(process)d-%(levelname)s:%(message)s', level=logging.DEBUG)

def start_server(args):
    server = Server(args.port)
    server.set_socket()
    server.bind_to_port()
    while True:
        message = server.socket.recv()
        logging.info(f'received message: {message}')
        server.socket.send(b'f"Processed {message}"')
        
def submit(args):
    print(args.cmd)
