import sys
sys.path.append('../tools/')
import tools as tools
import numpy as np
import pandas as pd
import argparse
import time

# np.set_printoptions(threshold=sys.maxsize, suppress=True)    

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
    args = my_parser.parse_args()
    path = args.Dataset
    data = tools.read_csv(path)
    timer = args.timer
    return data, timer

def preprocess(data):
    data = data.drop(columns=['Arithmancy', 'Defense Against the Dark Arts', 'Care of Magical Creatures'])
    data = data.dropna()
    normed = tools.normalize(data)
    
    courses = list(normed.columns.values)
    courses[0] = 'intercept'
    
    X = normed.loc[:, 'Astronomy':]
    ones = np.ones([X.shape[0],1])
    X = np.concatenate((ones, X), axis=1)
    return normed, courses, X

def iterate_houses(normed, house):
    y = np.array(normed.loc[:,'Hogwarts House']).reshape(normed.shape[0],1)
    housename = np.array([house])
    return (y == housename).astype(int) # returns a numpy array of 0s and 1s (not in <housename> / is in <housename>)

def cost(X, y, theta):
    m = X.shape[0]
    hyp = tools.predict(X, theta)
    part1 = np.dot(-y.T, np.log(hyp))
    part2 = np.dot((1 - y).T, np.log(1 - hyp))
    return (part1 - part2) / m

def fit(X, y, theta, alpha, num_iters):
    m = X.shape[0]
    J_history = []
    for i in range(num_iters):
        hyp = tools.predict(X, theta)
        theta = theta - (alpha/m) * np.dot(X.T, (hyp - y))
        J_history.append(float(cost(X, y, theta)))
    return theta, J_history

def train(normed, X):
    alpha = 0.02
    num_iters = 100000
    weights = {}
    houses = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
    for house in houses:
        y = iterate_houses(normed, house)
        theta = np.zeros(X.shape[1]).reshape(X.shape[1],1)
        theta, J_history = fit(X, y, theta, alpha, num_iters)
        flatten = [item for array in theta for item in array] ## flattens a 2D array into 1D
        weights[house] = flatten
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
    data, timer = parse_args(usage)
    start_time = time.time()
    normed, courses, X = preprocess(data)
    weights = train(normed, X)
    write_weights(weights, courses)
    if timer == True:
        print("--- Training took %s seconds ---" % round((time.time() - start_time), 2))

if __name__ == '__main__':
    main()

## TO RUN:
## python3 logreg_train.py ../data/dataset_train.csv