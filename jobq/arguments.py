"""
Argument warehouse for jobq
"""

import argparse

from jobq import core

def get_args():
    """ Parses the command line arguments for the program """
    parser = argparse.ArgumentParser(prog="jobq", description="local job queueing service")
    subparsers = parser.add_subparsers(title="actions", dest="action",
                                       help="call a specific subparser with its help message to display args")
    subparsers.required = True

    #########################################################################
    # Add parent parser for arguments that will be used by other subparsers #
    #########################################################################
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument("-q", "--queue", type=str, required=True,
                               help="the queue you'd like to use")


    ######################
    # Start a new server #
    ######################
    parser_start_server = subparsers.add_parser('start_server', description="Start a new server")
    parser_start_server.add_argument("-p", "--port", required=True, help="The port to start the server on.")

    #####################
    # Start a new queue #
    #####################
    parser_start_queue = subparsers.add_parser('start_queue', parents=[parent_parser], description="Start a new queue")
    #parser_start.set_defaults(func=core.start)

    ###########################
    # Submit a job to a queue #
    ###########################
    parser_submit = subparsers.add_parser('submit', parents=[parent_parser], description="Submit a job to a queue")
    parser_submit.add_argument("-c", "--cmd", nargs="*", required=True, help="The full command line as a string to submit as a job.")
    parser_submit.set_defaults(func=core.submit)

    parser_list = subparsers.add_parser('list', description="List all active queues")
    args = parser.parse_args()
    return args
