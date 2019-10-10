import sys
sys.path.append('../tools/')
import tools as tools

def main():
    print("Hello world!") ######
    usage="Displays a scatter plot answering the question: What are the two features that are similar?"
    path = tools.parse_arg(usage)
    print(path)
    print("Goodbye world!") ######

if __name__ == '__main__':
    main()
