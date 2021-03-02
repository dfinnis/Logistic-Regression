# Logistic-Regression

A sorting hat for Hogwart's Houses.

A multi-class classifer, using logistic regression coded from scratch.

#### Final Score 125/100

## Getting Started

First clone this repo.

```git clone https://github.com/anyashuka/Logistic-Regression.git; cd Logistic-Regression```

Move into the Logistic-Regression folder and download dependencies.

```pip install -r requirements.txt```

Then simply run the ```run_all.sh``` script to follow the following steps in each folder.

```./run_all.sh```

<img src="https://github.com/anyashuka/Logistic-Regression/blob/master/img/run_all.png">

## 1.analyze

```describe.py``` is Pandas describe() recoded from scratch, using Numpy.

Run with dataset_train.csv as argument, ```describe.py``` displays info on numerical feaures for dataset_train.csv.

```python3 describe.py ../data/dataset_train.csv```

The output can be compared with the output of Pandas describe() for dataset_train.csv by running:

```python3 pandas_describe.py```

## 2.visualize

### Histogram

Which Hogwarts course has a homogeneous score distribution between all four houses?
Arithmancy & Care of Magical Creatures

```python3 histogram.py ../data/dataset_train.csv```

<img src="https://github.com/anyashuka/Logistic-Regression/blob/master/img/histogram_arithmancy.png" width="400">

<img src="https://github.com/anyashuka/Logistic-Regression/blob/master/img/histogram_care.png" width="400">

### Scatter_plot

What are the two features that are similar?
Astronomy & Defense Against the Dark Arts

```python3 scatter_plot.py ../data/dataset_train.csv```

<img src="https://github.com/anyashuka/Logistic-Regression/blob/master/img/scatter_plot.png" width="400">

### Pair_plot

What features are you going to use for your logistic regression?

```python3 pair_plot.py ../data/dataset_train.csv```

<img src="https://github.com/anyashuka/Logistic-Regression/blob/master/img/pair_plot.png">

## 3.logreg

### Train

Train model to predict Hogwart's House using logistic regression and dataset_train.csv.
Save model to weights.csv.

```python3 logreg_train.py ../data/dataset_train.csv -t -c```

#### Flag -t, --timer

Display time taken to train. Takes nearly a minute on my system for 100000 epochs.

#### Flag -c, --cost

Display cost graph, prediction error over training period.

<img src="https://github.com/anyashuka/Logistic-Regression/blob/master/img/training.png" width="400">

### Predict

Predict houses for dataset_test.csv, using the model saved as weights.csv. Saves predicted houses to ```houses.csv```.

```python3 logreg_predict.py ../data/dataset_test.csv ../data/weights.csv```

## Test Accuracy

Test accuracy of predicted houses against dataset_truth.csv. In ```tools/``` run:

```python3 accuracy.py ../data/dataset_truth.csv ../data/houses.csv```

<img src="https://github.com/anyashuka/Logistic-Regression/blob/master/img/accuracy.png" width="800">

## Dependencies

Thankfully running the following command should take care of dependencies for you.

```pip install -r requirements.txt```

Python 3.9.1
* pandas
* numpy
* seaborn
* termcolor
* matplotlib
* scikit_learn

## References


