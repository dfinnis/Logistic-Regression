import sys
sys.path.append('../tools/')
import tools as tools
sys.path.append('../1.analyze/')
import describe as describe
import matplotlib.pyplot as plt
import warnings

def plot_house(data, normed, house, column, color):
    grades = normed[data['Hogwarts House'] == house][column]
    plt.hist(grades, bins=25, alpha=0.5, label = house, color = color)

def histogram(data, normed, column):
    plt.figure()
    plot_house(data, normed, 'Ravenclaw', column, 'b')
    plot_house(data, normed, 'Slytherin', column, 'g')
    plot_house(data, normed, 'Gryffindor', column, 'r')
    plot_house(data, normed, 'Hufflepuff', column, 'y')
    plt.legend(loc = 'upper right')
    plt.title(column)
    plt.xlabel('Normalized Score')
    plt.ylabel('Number of Students')
    plt.show()

def visualize(data, normed):
    warnings.simplefilter(action = 'ignore', category = RuntimeWarning)
    histogram(data, normed, 'Arithmancy')                ## homogeneous
    histogram(data, normed, 'Care of Magical Creatures') ## homogeneous
    histogram(data, normed, 'Potions')                   ## mostly homogenous

def main():
    usage = 'Display a histogram answering the question:\
    		 Which Hogwarts course has a homogeneous score distribution between all four houses?'
    data = tools.parse_arg(usage)
    normed = tools.normalize(data)
    visualize(data, normed)

if __name__ == '__main__':
    main()
