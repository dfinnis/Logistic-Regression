import argparse
import os
import sys
import pandas as pd

def error_exit(err_msg):
    print('Error: {}' .format(err_msg))
    sys.exit()

def is_file(path):
    if not os.path.isfile(path):
        error_exit('path specified ({}) does not exist' .format(path))

def parse_arg(usage):
    my_parser = argparse.ArgumentParser(description=usage)
    my_parser.add_argument('Dataset',
                       metavar='dataset',
                       type=str,
                       help='the path to dataset')
    args = my_parser.parse_args()
    path = args.Dataset
    is_file(path)
    return path

def read_csv(path):
    try:
        data = pd.read_csv(path)
    except Exception:
        error_exit('Failed to read {}' .format(path))
    return data