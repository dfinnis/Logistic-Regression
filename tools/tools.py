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

def generic_preprocess(data, fill):
    data = data.drop(columns=['Arithmancy', 'Defense Against the Dark Arts', 'Care of Magical Creatures'])
    if fill == 'mean':
        data = data.fillna(data.mean())
    else:
        data = data.dropna()
    normed = normalize(data)
    X = normed.loc[:, 'Astronomy':]
    ones = np.ones([X.shape[0],1])
    X = np.concatenate((ones, X), axis=1)
    return normed, X
