import sys
sys.path.append('../tools/')
import tools as tools
sys.path.append('../1.analyze/')
import describe as describe
import numpy as np
import pandas as pd
from Logistic_Regression import fit, cost, predict, sigmoid

import timeit
    
# np.set_printoptions(threshold=sys.maxsize, suppress=True)    

def write_weights(weights):
    try:
        file = open('../data/weights.csv', 'w')            
        file.write(weights)
        file.close
    except Exception:
    	tools.error_exit('Saving weights.csv failed')

def normalize(data):
    features = describe.find_features(data)
    normed = data.drop(columns=['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])
    for column in normed.columns:
        if not column == 'Hogwarts House':
            mean = features[column][1]
            std = features[column][2]
            normed[column] = (normed[column] - mean) / std
    return normed

def preprocess(data):
    # data = data.drop(columns=['Arithmancy', 'Defense Against the Dark Arts', 'Potions', 'Care of Magical Creatures'])
    data = data.drop(columns=['Arithmancy', 'Defense Against the Dark Arts', 'Care of Magical Creatures'])
    data = data.dropna()
    normed = normalize(data)

    courses = list(normed.columns.values)
    courses[0] = 'intercept'
    # courses.remove('Hogwarts House')

    X = normed.loc[:, 'Astronomy':]
    ones = np.ones([X.shape[0],1])
    X = np.concatenate((ones, X), axis=1)

    return normed, courses, X

# returns a numpy array of 0s and 1s (not in <housename> / is in <housename>)
def iterate_houses(normed, house):
    y = np.array(normed.loc[:,'Hogwarts House']).reshape(normed.shape[0],1) ## why use data here, rather than normed?
    housename = np.array([house])
    return (y == housename).astype(int)

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

def main():
    usage = 'Given dataset_train.csv, generate weights.csv for prediction.\
             Use gradient descent to minimize error'
    data = tools.parse_arg(usage)
    normed, courses, X = preprocess(data)
    weights = train(normed, X)
   
    weights = pd.DataFrame.from_dict(weights, columns=courses, orient='index')
    # weights.to_csv('weights.csv', header=False)
    weights.to_csv('weights.csv')


if __name__ == '__main__':
    main()





# Reasons for removal:
# 'Arithmancy' & 'Care of Magical Creatures' & 'Potions' - homogenous distribution between houses
# 'Defense Against the Dark Arts' - same as Astronomy