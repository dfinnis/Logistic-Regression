import sys
sys.path.append('../tools/')
import tools as tools
sys.path.append('../1.analyze/')
import describe as describe
# import pandas as pd

def normalize(data):
	features = describe.find_features(data)
	print(features) ######
	normed = 'I am a normal human' #####
	return normed

def visualize(data):
    # pd.set_option('display.max_rows', -1) #######
    normed = normalize(data)
    print(normed) #######
    print(data) #######

def main():
    usage = 'Display a pair plot which highlights features useful for logistic regression'
    data = tools.parse_arg(usage)
    visualize(data)

if __name__ == '__main__':
    main()