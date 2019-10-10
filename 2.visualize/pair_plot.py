import sys
sys.path.append('../tools/')
import tools as tools

def main():
    print("Hello world!") ######
    usage="Displays a pair plot which highlights features useful for logistic regression"
    path = tools.parse_arg(usage)
    print(path)
    print("Goodbye world!") ######

if __name__ == '__main__':
    main()