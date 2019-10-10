import sys
sys.path.append('../tools/')
import tools as tools
import pandas as pd

def write_weights():
    try:
        file = open('../data/weights.csv', 'w')            
        file.write('Oh hi there')
        file.close
    except Exception:
    	tools.error_exit("Saving weights.csv failed")


def main():
    usage="Given dataset_train.csv, generate weights.csv for prediction. Use gradient descent to minimize error"
    path = tools.parse_arg(usage)
    data = pd.read_csv(path)
    print(data)
    ## train
    write_weights()
    print("Goodbye world!") ######

if __name__ == '__main__':
    main()
