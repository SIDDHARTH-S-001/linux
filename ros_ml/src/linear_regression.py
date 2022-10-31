from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import future

MSE = []
iteration = []  
data = pd.read_csv('/home/ssiddharth/catkin_ws/src/ros_ml/results/test.csv')

X = data.iloc[:,:-1].values.flatten()
Y = data.iloc[:, 1].values.flatten()

def compute_error(b, m, X, Y):
    total_err = 0
    for i in range(0, len(X)):
        x = X
        y = Y
        total_err += (y[i] - (m*x[i]+b))**2
        mse = total_err/(total_err.size)
        return mse

m = 0
b = 0

alpha = 0.0001
epochs = 100000

n = len(X)

for i in range(epochs):
    y_pred = m*X + b
    gradient_m = (-2/n)*(X * (Y - y_pred))
    gradient_b = (-2/n)*(Y-y_pred)

    m = m - alpha*gradient_m
    b = b - alpha*gradient_b

    mse = compute_error(b, m, X, Y)
    MSE.append(mse)
    iteration.append(i)

y_pred = m*X + b
x_future = 1.4
y_future = m*x_future+b

plt.figure(figsize=(10, 10))
plt.scatter(X, Y, label = 'ground_truth')
#plt.scatter(x_future, y_future, label = 'prediction')
plt.plot(X, y_pred, color = "blue", label="prediction")
plt.xlabel("x", fontsize=16)
plt.ylabel("y", fontsize=16)
plt.title("Gradient Descent", fontsize=18)
plt.legend()
plt.show()
