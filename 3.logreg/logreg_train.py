import sys
sys.path.append('../tools/')
import tools as tools
sys.path.append('../1.analyze/')
import describe as describe
import numpy as np
import pandas as pd
from Logistic_Regression import fit, cost, predict, sigmoid

import timeit
    
np.set_printoptions(threshold=sys.maxsize, suppress=True)    

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
    data = data.drop(columns=['Arithmancy', 'Defense Against the Dark Arts', 'Potions', 'Care of Magical Creatures'])
    data = data.dropna()
    normed = normalize(data)

    # houses = {'Gryffindor': ['History of Magic','Transfiguration', 'Flying'], 
    #         'Ravenclaw': ['Muggle Studies', 'Charms'], 
    #         'Slytherin': ['Divination'], 'Hufflepuff': ['Astronomy', 'Herbology', 'Ancient Runes']}

    # courses = list(normed.columns.values)
    # courses.remove('Hogwarts House')

    # return X, y
    return normed

# returns a numpy array of 0s and 1s (not in <housename> / is in <housename>)
def filter_House(housename, y):
    house = np.array([housename])
    return y == house

def iterate_houses(data, normed, house):
    X = normed.loc[:, 'Astronomy':]
    # X = normed[[course1,course2]]
    ones = np.ones([X.shape[0],1])
    X = np.concatenate((ones, X), axis=1)

    y = np.array(normed.loc[:,'Hogwarts House']).reshape(1359,1) ## why use data here, rather than normed?
    y = filter_House(house, y).astype(int)

    return X, y

def train(data, normed):

    alpha = 0.02
    num_iters = 100000
    weights = {}

    # theta = np.zeros(3).reshape(3, 1)

    houses = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
    for house in houses:
        X, y = iterate_houses(data, normed, house)
        theta = np.zeros(X.shape[1]).reshape(X.shape[1],1)
        theta, J_history = fit(X, y, theta, alpha, num_iters)
        flatten = [item for array in theta for item in array]
        p = predict(X, theta)
        print(p)
        weights[house] = flatten


    # start = timeit.timeit()
    # for house, noted_courses in houses.items():
    #     for noted_course in noted_courses:
    #         for course in courses:
    #             theta = np.zeros(3).reshape(3, 1)
    #             X, y = iterate_courses(data, normed, house, noted_course, course)
    #             theta, J_history = fit(X, y, theta, alpha, num_iters)


    #             weight = [house, noted_course, course, flatten]
    #             print(weight)
    #             weights.append(weight) ## instead: no weights[], use generator and write to csv one line at a time?        

    # p = predict(X, theta)
    # np.set_printoptions(threshold=sys.maxsize, suppress=True)    

    ### pump some iron ###
    # end = timeit.timeit()
    # print(end - start)
    # weights = 'Thanks for stopping by!' ###
    # print(weights)
    return weights

def main():
    usage = 'Given dataset_train.csv, generate weights.csv for prediction.\
             Use gradient descent to minimize error'
    data = tools.parse_arg(usage)
    normed = preprocess(data)

    weights = train(data, normed)

    weights = pd.DataFrame.from_dict(weights, orient='index')
    print(weights)
    weights.to_csv('weights.csv', header=False)

    # write_weights(weights)

if __name__ == '__main__':
    main()





# Reasons for removal:
# 'Arithmancy' & 'Care of Magical Creatures' & 'Potions' - homogenous distribution between houses
# 'Defense Against the Dark Arts' - same as Astronomy