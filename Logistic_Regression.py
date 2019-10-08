import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("ex2data1.csv")

X = data.values[:,:2] # converts dataframe to numpy array
ones = np.ones([X.shape[0],1])
X = np.concatenate((ones,X),axis=1)

y = np.array(data.admission).reshape(100,1)

print(X.shape)
print(y.shape)

theta = np.zeros(3).reshape(3, 1)

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

print(cost(X, y, theta))

def fit(X, y, theta, alpha, num_iters):
    m = X.shape[0]
    J_history = []
    for i in range(num_iters):
        hyp = predict(X, theta)
        theta = theta - (alpha/m) * np.dot(X.T, (hyp - y))
        J_history.append(float(cost(X, y, theta))) # float returns a float (if you do just cost() it appends an array to an array)
    return theta, J_history

alpha = 0.000002
num_iters = 100000
theta = np.zeros(3).reshape(3,1)
theta, J_history = fit(X, y, theta, alpha, num_iters)

#print(theta, J_history[-1])

cost(X, y, theta)

print(J_history)

fig = plt.figure()
ax = plt.axes()
ax.plot(J_history)

p = predict(X, theta)
print(p)

accuracy = y - p
score = np.where(accuracy == 0)[1].size
print(score)







