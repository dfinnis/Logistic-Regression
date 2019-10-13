import sys
sys.path.append('../tools/')
import tools as tools
import argparse
import os
import pandas as pd

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
    tools.is_file(data_path)
    tools.is_file(weights_path)
    data = tools.read_csv(data_path)
    weights = tools.read_csv(weights_path)
    return data, weights

def predict(data, weights):
	### Look into the magic orb ###
	# print(data) ###
	# print(weights) ###
	predictions = 'You stay classy San Diego!' ####
	return predictions

def main():
    usage='Given dataset_test.csv and weights.csv, generate prediction file houses.csv'
    data, weights = parse_args(usage)
    predictions = predict(data, weights)
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