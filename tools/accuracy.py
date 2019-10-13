import tools as tools
import numpy as np
from sklearn.metrics import accuracy_score
import argparse
import os
import sys
import pandas as pd

def parse_args(usage):
    my_parser = argparse.ArgumentParser(description=usage)
    my_parser.add_argument('Truth',
                       metavar='true answers',
                       type=str,
                       help='the path to the true answers')
    my_parser.add_argument('Predicted',
                       metavar='predicted answers',
                       type=str,
                       help='the path to the predicted answers')
    args = my_parser.parse_args()
    true_path = args.Truth
    predicted_path = args.Predicted
    tools.is_file(true_path)
    tools.is_file(predicted_path)
    true = tools.read_csv(true_path)
    predicted = tools.read_csv(predicted_path)
    return true, predicted


def find_accuracy(true, predicted):
	print(true['Hogwarts House']) ########
	print(predicted['Hogwarts House']) ####
	y_pred = [0, 2, 2, 'grifindor'] ######
	y_true = [0, 1, 2, 'grifindor'] #######
	score = accuracy_score(y_true, y_pred)
	percent = score * 100
	return percent

def main():
    usage='Display accuracy of prediction, given the true answers and predicted answers as .csv'
    true, predicted = parse_args(usage)
    accuracy = find_accuracy(true, predicted)
    print("accuracy: {}%" .format(accuracy))

if __name__ == '__main__':
    main()