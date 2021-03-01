import pandas as pd

## Pandas describe dataset_train.csv
## for reference against describe.py
data = pd.read_csv("../data/dataset_train.csv")
data = data.drop(columns=['Index'])
desc = data.describe()
print(desc)
