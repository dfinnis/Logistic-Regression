import argparse
import os
import sys

def error_exit(err_msg):
    print('Error: {}' .format(err_msg))
    sys.exit()

def parse_arg(usage):
    my_parser = argparse.ArgumentParser(description=usage)
    my_parser.add_argument('Dataset',
                       metavar='dataset',
                       type=str,
                       help='the path to dataset')
    args = my_parser.parse_args()
    path = args.Dataset
    if not os.path.isfile(path):
        error_exit('Dataset specified does not exist')
    return path