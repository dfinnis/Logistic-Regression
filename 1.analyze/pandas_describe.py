import pandas
import tools as tools

def main():
	usage = 'Display pandas descibe output for given data set.\
			 Provides reference for describe.py.'
	df = tools.parse_arg(usage)
	df = df.drop(columns=['Index'])
	print(df.describe())

if __name__ == '__main__':
    main()
