import sys
sys.path.append('../tools/')
import tools as tools
# import pandas as pd

def visualize(data):
    print(data) #######

def main():
    usage = 'Display a pair plot which highlights features useful for logistic regression'
    data = tools.parse_arg(usage)
    visualize(data)

if __name__ == '__main__':
    main()