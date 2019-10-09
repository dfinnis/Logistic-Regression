## take a dataset as a parameter
## display info for numerical features in format:

## $> describe.[extension] dataset_train.csv
## 		 Feature 1       Feature 2       Feature 3       Feature 4
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

def parse_arg():
    my_parser = argparse.ArgumentParser(description='Display numerical features for given dataset')
    my_parser.add_argument('Dataset',
                       metavar='dataset',
                       type=str,
                       help='the path to dataset')
    args = my_parser.parse_args()

    dataset = args.Dataset
    if not os.path.isfile(dataset):
        print('The dataset specified does not exist')
        sys.exit()
    return dataset

def main():
    print("Hello world!") ####
    dataset = parse_arg()
    print("Goodbye world!") ####

if __name__ == '__main__':
    main()
