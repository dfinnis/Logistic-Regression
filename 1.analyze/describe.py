import numpy as np
import pandas as pd
import math
import sys
sys.path.append('../tools/')
import tools as tools

def std_dev(feature, mean, count):
    total = 0
    for value in feature:
        if str(value) != 'nan':
            diff = value - mean
            square = diff * diff
            total += square
    mean_sq = total / count
    std_dev = math.sqrt(mean_sq)
    return std_dev

def find_features(data):
    try:
        features = pd.DataFrame({'': ['Count', 'Mean ', 'Std  ', 'Min  ', '25%  ', '50%  ', '75%  ', 'Max  ']})
        col = 0
        for column in data.columns:
            # if col == 4:
            #     ### deal with age
            # if col == 5:
            #     ### deal with left/right handed
            if col > 5:
                count = 0
                total = 0
                feature = np.array(data[column], dtype='float64')
                feature = np.sort(feature)
                set = 0
                for value in feature:
                    if str(value) != 'nan':
                        count += 1
                        total += value
                        if set == 0:
                            minimum = value
                            maximum = value
                            set = 1
                        else:
                            maximum = value
                mean = total / count
                std = std_dev(feature, mean, count)
                quarter = feature[round(count/4)]
                half = feature[round(count/2)]
                three_quarter = feature[round((count/4)*3)]

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
