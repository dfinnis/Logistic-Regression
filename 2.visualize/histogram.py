import sys
sys.path.append('../tools/')
import tools as tools
sys.path.append('../1.analyze/')
import describe as describe
import matplotlib.pyplot as plt
import warnings

def normalize(data):
    features = describe.find_features(data)
    normed = data.drop(columns=['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])
    for column in normed.columns:
        if not column == 'Hogwarts House':
            mean = features[column][1]
            std = features[column][2]
            normed[column] = (normed[column] - mean) / std
    return normed

def get_grades(data, normed, house, course):
    df = normed[data['Hogwarts House'] == house][course]
    return df

def visualize(data, normed):
    warnings.simplefilter(action = "ignore", category = RuntimeWarning)
    for column in normed.columns:
        if not column == 'Hogwarts House':
            plt.figure()
            plt.hist(get_grades(data, normed, "Ravenclaw", column), bins=25, alpha=0.5, label = 'Ravenclaw', color = 'b')
            plt.hist(get_grades(data, normed, "Slytherin", column), bins=25, alpha=0.5, label = 'Slytherin', color = 'y')
            plt.hist(get_grades(data, normed, "Gryffindor", column), bins=25, alpha=0.5, label = 'Gryffindor', color = 'g')
            plt.hist(get_grades(data, normed, "Hufflepuff", column), bins=25, alpha=0.5, label = 'Hufflepuff', color = 'r')
            plt.legend(loc = 'upper right')
            plt.title(column)
            plt.xlabel('Normalized Score')
            plt.ylabel('Number of Students')
            plt.show()

def main():
    usage = 'Display a histogram answering the question:\
    		 Which Hogwarts course has a homogeneous score distribution between all four houses?'
    data = tools.parse_arg(usage)
    normed = normalize(data)
    visualize(data, normed)

if __name__ == '__main__':
    main()