import sys
sys.path.append('../tools/')
import tools as tools
import pandas as pd

def main():
    print('Hello world!') ######
    usage='Display a pair plot which highlights features useful for logistic regression'
    path = tools.parse_arg(usage)
    data = pd.read_csv(path)
    print(data)
    print('Goodbye world!') ######

if __name__ == '__main__':
    main()