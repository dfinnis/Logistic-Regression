import sys
sys.path.append('../tools/')
import tools as tools

def main():
    print("Hello world!") ######
    usage="Displays a histogram answering the question: Which Hogwarts course has a homogeneous score distribution between all four houses?"
    path = tools.parse_arg(usage)
    print(path)
    print("Goodbye world!") ######

if __name__ == '__main__':
    main()