import sys
sys.path.append('../tools/')
import tools as tools
sys.path.append('../1.analyze/')
import describe as describe

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from Logistic_Regression import fit, cost, predict, sigmoid

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

def filter_House(housename, y):
    house = np.array([housename])
    return y == house

def preprocess(data):
    data = data.drop(columns=['Arithmancy', 'Defense Against the Dark Arts', 'Care of Magical Creatures'])
    data = data.dropna()
    normed = normalize(data)

    X = normed.loc[:, 'History of Magic':'Transfiguration']
    ones = np.ones([X.shape[0],1])
    X = np.concatenate((ones, X), axis=1)
    y = np.array(data.loc[:,'Hogwarts House']).reshape(1333,1)

    housename = 'Gryffindor'
    y = filter_House(housename, y).astype(int)

    return normed, X, y
    # return data, normed

def train(data):
    # data, normed = preprocess(data)
    normed, X, y = preprocess(data)

    alpha = 0.02
    num_iters = 100000
    theta = np.zeros(3).reshape(3, 1)
    theta, J_history = fit(X, y, theta, alpha, num_iters)
    
    # plt.figure()
    # ax = plt.axes()
    # ax.plot(J_history)
    # plt.show()

    p = predict(X, theta)
    # np.set_printoptions(threshold=sys.maxsize)    
    print(p)

    # accuracy = y - p
    # score = np.where(accuracy == 0)[1].size
    # print(score)


    ### pump some iron ###
    weights = 'Thanks for stopping by!' ###
    return weights

def main():
    usage = 'Given dataset_train.csv, generate weights.csv for prediction.\
             Use gradient descent to minimize error'
    data = tools.parse_arg(usage)
    weights = train(data)
    write_weights(weights)

if __name__ == '__main__':
    main()

# Reasons for removal:
# 'Arithmancy' & 'Care of Magical Creatures' - homogenous distribution between houses
# 'Defense Against the Dark Arts' - same as Astronomy