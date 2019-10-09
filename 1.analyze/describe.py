## take a dataset as a parameter
## display info for numerical features in format:

## $> describe.[extension] dataset_train.csv
##               Feature 1       Feature 2       Feature 3       Feature 4
## Count        149.000000      149.000000      149.000000      149.000000
## Mean           5.848322        3.051007        3.774497        1.205369
## Std            5.906338        3.081445        4.162021        1.424286
## Min            4.300000        2.000000        1.000000        0.100000
## 25%            5.100000        2.800000        1.600000        0.300000
## 50%            5.800000        3.000000        4.400000        1.300000
## 75%            6.400000        3.300000        5.100000        1.800000
## Max            7.900000        4.400000        6.900000        2.500000

import argparse
import os
import sys
import numpy as np
import pandas as pd
import math

def error_exit(err_msg):
    print("Error: {}" .format(err_msg))
    sys.exit()    

def parse_arg():
    my_parser = argparse.ArgumentParser(description='Display numerical features for given dataset')
    my_parser.add_argument('Dataset',
                       metavar='dataset',
                       type=str,
                       help='the path to dataset')
    args = my_parser.parse_args()

    path = args.Dataset
    if not os.path.isfile(path):
        error_exit("Dataset specified does not exist")
    return path

def std_dev(feature, mean, count):
    total = 0
    for value in feature:
        if str(value) != "nan":
            diff = value - mean
            square = diff * diff
            total += square
    mean_sq = total / count
    std_dev = math.sqrt(mean_sq)
    return std_dev

def parse_file(path):
    try:
        data = pd.read_csv(path)
        df = pd.DataFrame({'': ['Count', 'Mean ', 'Std  ', 'Min  ', '25%  ', '50%  ', '75%  ', 'Max  ']})
        col = 0
        for column in data.columns:
            # if col == 4:
            #     ### deal with age
            # if col == 5:
            #     ### deal with left/right handed
            if col > 5:
                count = 0
                total = 0
                feature = np.array(data[column], dtype='float64')
                feature = np.sort(feature)
                set = 0
                for value in feature:
                    if str(value) != "nan":
                        count += 1
                        total += value
                        if set == 0:
                            minimum = value
                            maximum = value
                            set = 1
                        else:
                            maximum = value
                mean = total / count
                std = std_dev(feature, mean, count)
                quarter = feature[round(count/4)]
                half = feature[round(count/2)]
                three_quarter = feature[round((count/4)*3)]

                df[column] = np.array([count, mean, std, minimum, quarter, half, three_quarter, maximum])
            col += 1
    except Exception:
        error_exit("Failed to read file")
    return df.to_string(index=False)

def main():
    path = parse_arg()
    dataset = parse_file(path)
    print(dataset)

if __name__ == '__main__':
    main()
