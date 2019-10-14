import sys
sys.path.append('../tools/')
import tools as tools
sys.path.append('../1.analyze/')
import describe as describe
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

def normalize(data):
	features = describe.find_features(data)
	print(features) ######
	normed = 'I am a normal human' #####
	return normed

def visualize(data):
    # pd.set_option('display.max_rows', -1) #######
    normed = normalize(data)
    print(normed) #######
    # print(data) #######
    # print(data['Best Hand']) ########

def main():
	usage = 'Display a scatter plot answering the question:\
			 What are the two features that are similar?'
	data = tools.parse_arg(usage)
	visualize(data)

if __name__ == '__main__':
	main()




