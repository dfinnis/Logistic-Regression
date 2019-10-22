import sys
sys.path.append('../tools/')
import tools as tools
import numpy as np
import pandas as pd
import argparse
import time
import logistic_regression as logreg

# np.set_printoptions(threshold=sys.maxsize, suppress=True) ## Print non-truncated output

def parse_args(usage):
    my_parser = argparse.ArgumentParser(description=usage)
    my_parser.add_argument('Dataset',
        metavar='dataset',
        type=str,
        help='the path to dataset')
    my_parser.add_argument('-t',
        '--timer',
        action='store_true',
        help='Display time taken. Default false')
    my_parser.add_argument('-c',
        '--cost',
        action='store_true',
        help='Display cost graph, prediction error over training period. Default false')
    args = my_parser.parse_args()
    path = args.Dataset
    data = tools.read_csv(path)
    timer = args.timer
    cost = args.cost
    return data, timer, cost

def preprocess(data):
    try:
        normed, X = tools.generic_preprocess(data, 'drop')
        courses = list(normed.columns.values)
        courses[0] = 'intercept'
    except Exception:
        tools.error_exit('Failed to preprocess data. Is data valid?')
    return normed, courses, X

def iterate_houses(normed, house):
    y = np.array(normed.loc[:,'Hogwarts House']).reshape(normed.shape[0],1)
    housename = np.array([house])
    return (y == housename).astype(int) # returns a numpy array of 0s and 1s (not in <housename> / is in <housename>)

def train(normed, X, cost):
    try:
        alpha = 0.02
        num_iters = 100000
        weights = {}
        houses = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
        if cost == True:
            ax = tools.plot_set_up()
        for house in houses:
            y = iterate_houses(normed, house)
            theta = np.zeros(X.shape[1]).reshape(X.shape[1],1)
            theta, J_history = logreg.fit(X, y, theta, alpha, num_iters)
            if cost == True:
                tools.plot_house(J_history, house, ax)
            flatten = [item for array in theta for item in array] ## flattens a 2D array into 1D
            weights[house] = flatten
        if cost == True:
            tools.plot_show()
    except Exception:
        tools.error_exit('Failed to train weights.')
    return weights

def write_weights(weights, courses):
    try:
        weights = pd.DataFrame.from_dict(weights, columns=courses, orient='index')
        weights.to_csv('../data/weights.csv')
        print('Successfully saved weights to ../data/weights.csv')
    except Exception:
    	tools.error_exit('Saving weights.csv failed')

def main():
    usage = 'Given dataset_train.csv, generate weights.csv for prediction.\
             Use gradient descent to minimize error'
    data, timer, cost = parse_args(usage)
    start_time = time.time()
    normed, courses, X = preprocess(data)
    weights = train(normed, X, cost)
    write_weights(weights, courses)
    if timer == True:
        print("--- Training took %s seconds ---" % round((time.time() - start_time), 2))

if __name__ == '__main__':
    main()

## TO RUN:
## python3 logreg_train.py ../data/dataset_train.csv