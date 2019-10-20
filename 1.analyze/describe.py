import numpy as np
import pandas as pd
import math
import sys
sys.path.append('../tools/')
import tools as tools

def std_dev(feature, mean, count):
    total = 0.0
    for value in feature:
        if str(value) != 'nan':
            total += ((value - mean) ** 2)
    mean_sq = total / (count - 1)
    std_dev = math.sqrt(mean_sq)
    return std_dev

def find_quart(feature, count, quart = 1):
    index = (count - 1) * (quart * 0.25)
    floor = math.floor(index)
    if floor == index:
        return feature[int(index)]
    return (feature[floor] + (feature[floor + 1] - feature[floor]) * (index - floor))

def find_features(data):
    try:
        features = pd.DataFrame({'': ['Count', 'Mean ', 'Std  ', 'Min  ', '25%  ', '50%  ', '75%  ', 'Max  ']})
        col = 0
        for column in data.columns:
            if col > 5:
                count = 0
                total = 0
                feature = np.array(data[column], dtype='float64')
                feature = np.sort(feature)
                min_set = 0
                for value in feature:
                    if str(value) != 'nan':
                        count += 1
                        total += value
                        if min_set == 0:
                            minimum = value
                            maximum = value
                            min_set = 1
                        else:
                            maximum = value
                mean = total / count
                std = std_dev(feature, mean, count)
                quarter = find_quart(feature, count, 1)
                half = find_quart(feature, count, 2)
                three_quarter = find_quart(feature, count, 3)

                features[column] = np.array([count, mean, std, minimum, quarter, half, three_quarter, maximum])
            col += 1
    except Exception:
        tools.error_exit('Failed to read file')
    return features

def main():
    usage = 'Display numerical features for given dataset'
    data = tools.parse_arg(usage)
    features = find_features(data)
    print(features.to_string(index=False))

if __name__ == '__main__':
    main()
