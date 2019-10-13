import sys
sys.path.append('../tools/')
import tools as tools
# import pandas as pd

def visualize(data):
    print(data) ######

def main():
    usage='Display a histogram answering the question: Which Hogwarts course has a homogeneous score distribution between all four houses?'
    data = tools.parse_arg(usage)
    visualize(data)

if __name__ == '__main__':
    main()