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
    parent_parser.add_argument("-p", "--port", type=str, required=True,
                                help="The server port")

    ######################
    # Start a new server #
    ######################
    parser_start_server = subparsers.add_parser('start_server', parents=[parent_parser], description="Start a new server")
    parser_start_server.add_argument("--with_password",
                                     action="store_true",
                                     help="the password to init the server with.")
    parser_start_server.set_defaults(func=core.start_server)


    ###############################
    # Client subparser entrypoint #
    ###############################
    parser_client = subparsers.add_parser('client', parents=[parent_parser], description="send a message from the client to the server")
    client_subparser = parser_client.add_subparsers()

    #########################
    # Kill a running server #
    #########################
    kill_server = client_subparser.add_parser('kill_server', description="Stop a running server")
    kill_server.add_argument("--with_password",
                             action="store_true",
                             help="prompt to kill server with password associated.")
    kill_server.set_defaults(func=core.kill_server)
    ##########################
    # Client check for queue #
    ##########################
    queueexists = client_subparser.add_parser('queueexists', description="See if a queue has been initiated")
    queueexists.add_argument("-q", "--queue", type=str, required=True,
                             help="the queue to check for.")
    queueexists.set_defaults(func=core.queueexists)

    ##########################
    # Client list all queues #
    ##########################
    showqueues = client_subparser.add_parser('showqueues', description="list all queues initiated in server")
    showqueues.set_defaults(func=core.showqueues)

    ##################################
    # Client check all jobs in queue #
    ##################################
    showjobs = client_subparser.add_parser('showjobs', description="Lists all jobs in queue")
    showjobs.add_argument("-q", "--queue", type=str, required=True,
                          help="Lists all jobs in queue")
    showjobs.set_defaults(func=core.showjobs)
    args = parser.parse_args()
    return args
