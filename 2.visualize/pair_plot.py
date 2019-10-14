import sys
sys.path.append('../tools/')
import tools as tools
import matplotlib.pyplot as plt
import seaborn as sb

def visualize(data):
    data = data.drop(columns=['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand', 'Arithmancy', 'Defense Against the Dark Arts', 'Care of Magical Creatures'])
    data = data.dropna()
    sb.pairplot(data, hue='Hogwarts House', markers = '.', height=2)
    plt.show()

def main():
    usage = 'Display a pair plot which highlights features useful for logistic regression'
    data = tools.parse_arg(usage)
    visualize(data)

if __name__ == '__main__':
    main()

# Reasons for removal:
# 'Arithmancy' & 'Care of Magical Creatures' - homogenous distribution between houses
# 'Defense Against the Dark Arts' - same as Astronomy