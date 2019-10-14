import sys
sys.path.append('../tools/')
import tools as tools
sys.path.append('../1.analyze/')
import describe as describe

def write_weights(weights):
    try:
        file = open('../data/weights.csv', 'w')            
        file.write(weights)
        file.close
    except Exception:
    	tools.error_exit('Saving weights.csv failed')

def normalize(data):
    features = describe.find_features(data)
    normed = data.drop(columns=['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])
    for column in normed.columns:
        if not column == 'Hogwarts House':
            mean = features[column][1]
            std = features[column][2]
            normed[column] = (normed[column] - mean) / std
    return normed

def train(data):
    ### pump some iron ###
    # print(data) ###
    normed = normalize(data)
    # print(normed) #######
    weights = 'Thanks for stopping by!' ###
    return weights

def main():
    usage = 'Given dataset_train.csv, generate weights.csv for prediction.\
             Use gradient descent to minimize error'
    data = tools.parse_arg(usage)
    weights = train(data)
    write_weights(weights)

if __name__ == '__main__':
    main()
