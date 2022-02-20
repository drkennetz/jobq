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

    ######################################################
    # Parent parser for ports - Everything requires port #
    ######################################################
    parent_parser = argparse.ArgumentParser(add_help=False)
    parsent_parser.add_argument("-p", "--port", type=str, required=True,
                                help="The server port")

    ######################
    # Start a new server #
    ######################
    parser_start_server = subparsers.add_parser('start_server', parents=[parent_parser], description="Start a new server")
    parser_start_server.set_defaults(func=core.start_server)

    #########################
    # Stop a running server #
    #########################
    parser_stop_server = subparsers.add_parser('stop_server', parents=[parent_parser], description="Stop a running server")
    parser_stop_server.set_defaults(func=core.stop_server)

    ###############################
    # Client subparser entrypoint #
    ###############################
    parser_client = subparsers.add_parser('client', parents=[parent_parser], description="send a message from the client to the server")

    ##########################
    # Client check for queue #
    ##########################
    check_for_queue = parser_client.add_parser('check_for_queue', description="See if a queue has been initiated")
    check_for_queue.add_argument("-q", "--queue", type=str, required=True,
                                 help="the queue to check for.")
    check_for_queue.set_defaults(func=core.check_for_queue)

    ##########################
    # Client list all queues #
    ##########################
    list_all_queues = parser_client.add_parser('list_all_queues', description="list all queues initiated in server")
    list_all_queues.set_defaults(func=core.list_all_queues)

    ##################################
    # Client check all jobs in queue #
    ##################################
    list_jobs_in_queue = parser_client.add_parser('list_jobs_in_queue', description="Lists all jobs in queue")
    list_jobs_in_queue.add_argument("-q", "--queue", type=str, required=True,
                                    help="Lists all pending jobs in queue")
    
    parser_client.add_argument("-m", "--message", required=True,
                               choices=["check_for_queue",
                                        "add_job_to_queue",
                                        "requeue_to_front",
                                        "init_queue",
                                        "list_queues"],
                               help="The message to send to the server.")
    parser_client.set_defaults(func=core.client_message)
    args = parser.parse_args()
    return args
