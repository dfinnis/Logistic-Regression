import sys
sys.path.append('../tools/')
import tools as tools
import argparse
import numpy as np
import pandas as pd

np.set_printoptions(suppress=True)

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
    fill = 'mean'
    normed, X = tools.generic_preprocess(data, fill)
    return X

def predict_house(data, weights):
    houses = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
    X = preprocess(data)
    weights = weights.drop(weights.columns[0], axis=1)
    students = data.loc[:, 'Hogwarts House'].to_frame()

    i = 0
    for house in houses:
        theta = np.array(weights.iloc[i:i+1]).reshape(X.shape[1], 1)
        p = tools.predict(X, theta)
        students[house] = p
        i += 1

    students = students.drop(columns=['Hogwarts House'])
    predictions = students.idxmax(axis=1)
    return predictions

def write_houses(predictions):
    try:
        predictions.to_csv('../data/houses.csv', index_label='Index', header=['Hogwarts House'])
        print('Successfully saved predicted houses to ../data/houses.csv')
    except Exception:
    	tools.error_exit('Saving houses.csv failed')

def main():
    usage = 'Given dataset_test.csv and weights.csv, generate prediction file houses.csv'
    data, weights = parse_args(usage)
    predictions = predict_house(data, weights)
    write_houses(predictions)

if __name__ == '__main__':
    main()

## TO RUN:
## python3 logreg_predict.py ../data/dataset_train.csv ../data/weights.csv