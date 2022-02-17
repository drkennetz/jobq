"""
Jobq package:
  creates local job queues and submits one job per queue in serial.
  might add multiprocessing later.
"""

import sys

from jobq import arguments

def main():
    """ Main entry point """
    args = arguments.get_args()
    args.func(args)

if __name__ == "__main__":
    sys.exit(main())
