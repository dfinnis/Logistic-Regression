import sys
sys.path.append('../tools/')
import tools as tools
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt 
# import pandas as pd

def visualize(data):
    # pd.set_option('display.max_rows', -1) #######
    print(data) #######
    # print(data['Best Hand']) ########

def main():
	usage='Display a scatter plot answering the question: What are the two features that are similar?'
	data = tools.parse_arg(usage)
	visualize(data)

if __name__ == '__main__':
	main()




