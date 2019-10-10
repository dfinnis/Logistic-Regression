import sys
sys.path.append('../tools/')
import tools as tools
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt 
import pandas as pd

def main():
    usage='Display a scatter plot answering the question: What are the two features that are similar?'
    path = tools.parse_arg(usage)
    data = pd.read_csv(path)
    # pd.set_option('display.max_rows', -1)
    print(data)
    # print(data['Best Hand'])

    print('Goodbye world!') ######

if __name__ == '__main__':
    main()




