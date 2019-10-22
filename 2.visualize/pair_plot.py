import sys
sys.path.append('../tools/')
import tools as tools
import argparse
import matplotlib.pyplot as plt
import seaborn as sb

def parse_args(usage):
    my_parser = argparse.ArgumentParser(description=usage)
    my_parser.add_argument('Dataset',
        metavar='dataset_test.csv',
        type=str,
        help='the path to dataset_test.csv')
    my_parser.add_argument('-a',
        '--all',
        action='store_true',
        help='Plot all courses.\
              Include courses with homogeneous score distribution between houses, & courses that are similar.\
              Default: only plot courses useful for logistic regression')
    args = my_parser.parse_args()
    path = args.Dataset
    plot_all = args.all
    data = tools.read_csv(path)
    return data, plot_all

def preprocess(data, plot_all):
    try:
        data = data.drop(columns=['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])
        if plot_all == False:
            data = data.drop(columns=['Arithmancy', 'Care of Magical Creatures', 'Defense Against the Dark Arts'])
        data = data.dropna()
    except Exception:
        tools.error_exit('Failed to preprocess data. Is data valid?')
    return data

def visualize(data):
    try:
        sb.pairplot(data, hue='Hogwarts House', palette=['blue', 'green', 'red', 'gold'], markers = '.', height=2)
        plt.show()
    except Exception:
        tools.error_exit('Failed to visualize data. Is data valid?')

def main():
    usage = 'Display a pair plot which highlights features useful for logistic regression'
    data, plot_all = parse_args(usage)
    data = preprocess(data, plot_all)
    visualize(data)

if __name__ == '__main__':
    main()

## TO RUN:
## python3 pair_plot.py ../data/dataset_train.csv