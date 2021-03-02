#### -- Run DSLR -- ####
printf "\E[H\E[2J"
echo "\x1b[1mLaunching Datascience Logistic Regression...\x1B[0m\n"

#### -- 1.analyze -- ####
cd 1.analyze
echo "\x1b[1m1. Analyze\x1B[0m"
echo
echo "Pandas describe() recoded from scratch, using Numpy"
echo
echo "Numerical feaures for dataset_train.csv:"
echo
python3 describe.py ../data/dataset_train.csv
echo
cd ..

#### -- 2.visualize -- ####
cd 2.visualize
echo "\n\x1b[1m2. Visualize\x1B[0m"
echo
echo "Histogram:"
echo "Which Hogwarts course has a homogeneous score distribution between all four houses?"
echo "Arithmancy & Care of Magical Creatures"
python3 histogram.py ../data/dataset_train.csv
echo

echo "Scatter_plot:"
echo "What are the two features that are similar?"
echo "Astronomy & Defense Against the Dark Arts"
python3 scatter_plot.py ../data/dataset_train.csv
echo

echo "Pair_plot:"
echo "What features are you going to use for your logistic regression?"
python3 pair_plot.py ../data/dataset_train.csv
echo
cd ..

#### -- 3.logreg -- ####
cd 3.logreg
echo "\n\x1b[1m3. Logreg\x1B[0m\n"
echo "Training model..."
python3 logreg_train.py ../data/dataset_train.csv -c -t
echo

echo "Predicting houses for dataset_test.csv..."
python3 logreg_predict.py ../data/dataset_test.csv ../data/weights.csv
echo
cd ..

#### -- test accuracy -- ####
cd tools
echo "Testing accuracy of predicted houses against dataset_truth.csv..."
python3 accuracy.py ../data/dataset_truth.csv ../data/houses.csv
echo
echo
cd ..

#### -- cleanup -- ####
# rm data/weights.csv
# rm data/houses.csv
