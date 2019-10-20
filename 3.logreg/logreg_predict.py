import sys
sys.path.append('../tools/')
import tools as tools
import argparse
import numpy as np
import pandas as pd
from logreg_train import normalize
from Logistic_Regression import predict

np.set_printoptions(suppress=True)  

def write_houses(predictions):
    try:
        file = open('../data/houses.csv', 'w')            
        file.write(predictions)
        file.close
    except Exception:
    	tools.error_exit('Saving houses.csv failed')

def parse_args(usage):
    my_parser = argparse.ArgumentParser(description=usage)
    my_parser.add_argument('Dataset',
                       metavar='dataset_test.csv',
                       type=str,
                       help='the path to dataset_test.csv')
    my_parser.add_argument('Weights',
                       metavar='weights.csv',
                       type=str,
                       help='the path to weights.csv')
    args = my_parser.parse_args()
    data_path = args.Dataset
    weights_path = args.Weights
    data = tools.read_csv(data_path)
    weights = tools.read_csv(weights_path)
    return data, weights

def preprocess(data):
    data = data.drop(columns=['Arithmancy', 'Defense Against the Dark Arts', 'Potions', 'Care of Magical Creatures'])
    data = data.fillna(data.mean())
    normed = normalize(data)

    courses = list(normed.columns.values)
    courses[0] = 'intercept'
    # courses.remove('Hogwarts House')

    X = normed.loc[:, 'Astronomy':]
    ones = np.ones([X.shape[0],1])
    X = np.concatenate((ones, X), axis=1)

    return normed, courses, X

def predict_house(data, weights):
    ### Look into the magic orb ###
    # print(data) ###
    # print(weights) ###

    houses = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
    _, _, X = preprocess(data)
    predictions = data.iloc[:, 1]  # index + house len(X)
    # print(predictions)
    weights = weights.drop(weights.columns[0], axis=1)
    # theta = weights.iloc[0:1].reshape(scores.shape[1], 1)

    theta = np.array(weights.iloc[0:1]).reshape(X.shape[1], 1)

    p = predict(X, theta)

    for student in data:
        for house in houses:
            p = predict(X, theta)
            print(house, p)
            # p = np.where(p > 0.5)
            # if p > 0.5:
                # student['housename'] = house
            # print(house)

    # print(p)


    # predictions = 'You stay classy San Diego!' ####
    return predictions

def main():
    usage = 'Given dataset_test.csv and weights.csv, generate prediction file houses.csv'
    data, weights = parse_args(usage)
    predictions = predict_house(data, weights)
    write_houses(predictions)

if __name__ == '__main__':
    main()

## correct format:
## $> cat houses.csv
## Index,Hogwarts House
## 0,Gryffindor
## 1,Hufflepuff
## 2,Ravenclaw
## 3,Hufflepuff
## 4,Slytherin
## 5,Ravenclaw
## 6,Hufflepuff
##        [...]