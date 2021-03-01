#### -- Run DSLR -- ####
printf "\E[H\E[2J"
echo "\x1b[1mLaunching Datascience Logistic Regression...\x1B[0m\n"

#### -- 1.analyze -- ####
echo "\x1b[1m1.analyze\x1B[0m\n"
cd 1.analyze
python3 describe.py ../data/dataset_train.csv
echo
#### Pandas describe commands ####
# python3
# import pandas as pd
# data = pd.read_csv("./data/dataset_train.csv")
# desc = data.describe()
# desc
cd ..

#### -- 2.visualize -- ####
cd 2.visualize
echo "\n\x1b[1m2.visualize\x1B[0m\n"

echo "histogram:"
echo "Which Hogwarts course has a homogeneous score distribution between all four houses?\n"
python3 histogram.py ../data/dataset_train.csv

echo "scatter_plot:"
echo "What are the two features that are similar?\n"
python3 scatter_plot.py ../data/dataset_train.csv

echo "pair_plot:"
echo "what features are you going to use for your logistic regression?\n"
python3 pair_plot.py ../data/dataset_train.csv

cd ..

#### -- 3.logreg -- ####
cd 3.logreg
echo "\n\x1b[1m3.logreg\x1B[0m\n"
echo "Training model..."
python3 logreg_train.py ../data/dataset_train.csv -c -t
echo
echo "Predicting houses for dataset_test.csv..."
python3 logreg_predict.py ../data/dataset_test.csv ../data/weights.csv
echo

cd ..
#### -- test accuracy -- ####
# cd tools
# python3 accuracy.py ../data/houses.csv
# cd ..
