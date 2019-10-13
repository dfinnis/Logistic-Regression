import sys
sys.path.append('../tools/')
import tools as tools
import pandas as pd

def write_weights(weights):
    try:
        file = open('../data/weights.csv', 'w')            
        file.write(weights)
        file.close
    except Exception:
    	tools.error_exit('Saving weights.csv failed')

def train(data):
	### pump some iron ###
	# print(data) ###
	weights = 'Thanks for stopping by!' ###
	return weights

def main():
    usage = 'Given dataset_train.csv, generate weights.csv for prediction. Use gradient descent to minimize error'
    data = tools.parse_arg(usage)
    weights = train(data)
    write_weights(weights)

if __name__ == '__main__':
    main()
