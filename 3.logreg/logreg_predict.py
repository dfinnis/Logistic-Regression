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
    data = data.drop(columns=['Arithmancy', 'Defense Against the Dark Arts', 'Care of Magical Creatures'])
    data = data.fillna(data.mean())
    normed = normalize(data)

    X = normed.loc[:, 'Astronomy':]
    ones = np.ones([X.shape[0],1])
    X = np.concatenate((ones, X), axis=1)

    return normed, X

def predict_house(data, weights):
    houses = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
    _, X = preprocess(data)
    weights = weights.drop(weights.columns[0], axis=1)
    students = data.loc[:, 'Hogwarts House'].to_frame()

    i = 0
    for house in houses:
        theta = np.array(weights.iloc[i:i+1]).reshape(X.shape[1], 1)
        p = predict(X, theta)
        students[house] = p
        i += 1

    students = students.drop(columns=['Hogwarts House'])
    predictions = students.idxmax(axis=1)
    return predictions

def main():
    usage = 'Given dataset_test.csv and weights.csv, generate prediction file houses.csv'
    data, weights = parse_args(usage)
    predictions = predict_house(data, weights)
    predictions.to_csv('houses.csv', index_label='Index', header=['Hogwarts House'])
    # write_houses(predictions)

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