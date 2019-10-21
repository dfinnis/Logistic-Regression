import argparse
import os
import sys
import pandas as pd
sys.path.append('../1.analyze/')
import describe as describe
import numpy as np

def error_exit(err_msg):
    print('Error: {}' .format(err_msg))
    sys.exit()

def is_file(path):
    if not os.path.isfile(path):
        error_exit('path specified ({}) does not exist' .format(path))

def read_csv(path):
    is_file(path)
    try:
        data = pd.read_csv(path)
    except Exception:
        error_exit('Failed to read {}' .format(path))
    return data

def parse_arg(usage):
    my_parser = argparse.ArgumentParser(description=usage)
    my_parser.add_argument('Dataset',
                       metavar='dataset',
                       type=str,
                       help='the path to dataset')
    args = my_parser.parse_args()
    path = args.Dataset
    data = read_csv(path)
    return data

def normalize(data):
    features = describe.find_features(data)
    normed = data.drop(columns=['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])
    for column in normed.columns:
        if not column == 'Hogwarts House':
            mean = features[column][1]
            std = features[column][2]
            normed[column] = (normed[column] - mean) / std
    return normed

def sigmoid(z):
    return 1 / (1 + np.exp(-z))
    
def predict(X, theta):
    z = sigmoid(np.dot(X, theta))
    z[(z == 0)] += 10e-6 # takes care of bug
    z[(z == 1)] -= 10e-6
    return z