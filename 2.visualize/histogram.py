import sys
sys.path.append('../tools/')
import tools as tools
import pandas as pd

def main():
    print('Hello world!') ######
    usage='Display a histogram answering the question: Which Hogwarts course has a homogeneous score distribution between all four houses?'
    path = tools.parse_arg(usage)
    data = pd.read_csv(path)
    print(data)
    print('Goodbye world!') ######

if __name__ == '__main__':
    main()