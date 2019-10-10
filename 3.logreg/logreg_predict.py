import sys
sys.path.append('../tools/')
import tools as tools

def main():
    print("Hello world!") ######
    usage="Displays a pair plot which highlights features useful for logistic regression"
    path = tools.parse_arg(usage)
    data = pd.read_csv(path)
    print(data)
    print("Goodbye world!") ######

if __name__ == '__main__':
    main()

## takes as a parameter dataset_test.csv
## and a file containing the weights trained by previous program
## generates a prediction file houses.csv in format:

## $> cat houses.csv
## Index,Hogwarts House
## 0,Gryffindor
## 1,Hufflepuff
## 2,Ravenclaw
## 3,Hufflepuff
## 4,Slytherin
## 5,Ravenclaw
## 6,Hufflepuff
##        [...]