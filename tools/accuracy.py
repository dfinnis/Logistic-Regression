import tools as tools
import numpy as np
from sklearn.metrics import accuracy_score
import argparse
from termcolor import colored

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
    true = tools.read_csv(true_path)
    predicted = tools.read_csv(predicted_path)
    return true['Hogwarts House'], predicted['Hogwarts House']

def find_accuracy(true, predicted):
	try:
		if not len(true) == len(predicted):
			tools.error_exit('Number of true and predicted houses different')
		decimal = accuracy_score(true, predicted)
		percent = decimal * 100
	except Exception:
		tools.error_exit('Failed to find accuracy, are you sure predictions are valid?')
	return round(percent, 2)

def print_accuracy(accuracy, length):
	if accuracy >= 98:
		color = 'green'
	else:
		color = 'red'
	print(colored('Accuracy: {}% for {} predicted houses' .format(accuracy, length), color))

def main():
    usage = 'Display accuracy of prediction, given the true answers and predicted answers as .csv'
    true, predicted = parse_args(usage)
    accuracy = find_accuracy(true, predicted)
    print_accuracy(accuracy, (len(predicted) - 1))

if __name__ == '__main__':
    main()