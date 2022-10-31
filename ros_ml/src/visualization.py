import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('/home/ssiddharth/catkin_ws/src/ros_ml/results/test.csv')

x = np.array(data.iloc[:,:-1])
y = np.array(data.iloc[:, -1])

plt.figure(figsize=(10, 10))
plt.scatter(x,y)
plt.xlabel("x", fontsize=16)
plt.ylabel("y", fontsize=16)
plt.title("Robot Position", fontsize=18)
plt.show()
