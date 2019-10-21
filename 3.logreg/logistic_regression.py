import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))
    
def predict(X, theta):
    z = sigmoid(np.dot(X, theta))
    z[(z == 0)] += 10e-6    # takes care of bug
    z[(z == 1)] -= 10e-6
    return z

def cost(X, y, theta):
    m = X.shape[0]
    hyp = predict(X, theta)
    part1 = np.dot(-y.T, np.log(hyp))
    part2 = np.dot((1 - y).T, np.log(1 - hyp))
    return (part1 - part2) / m

def fit(X, y, theta, alpha, num_iters):
    m = X.shape[0]
    J_history = []
    for i in range(num_iters):
        hyp = predict(X, theta)
        theta = theta - (alpha/m) * np.dot(X.T, (hyp - y))
        J_history.append(float(cost(X, y, theta))) # float returns a float (if you do just cost() it appends an array to an array)
    return theta, J_history
