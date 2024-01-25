import numpy as np
from scipy.optimize import fmin
import matplotlib.pyplot as plt


def func(x):
    x0 = x[0]
    x1 = x[1]
    return x0 ** 2 + x1 ** 2


xopt, fopt = fmin(func=func, x0=[5, 5])
x = np.linspace([-5, -5], [5, 5], 100)
y = np.zeros((100))
for i in range(100):
    y[i] = func(x[i])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # 创建一个 3D 坐标系
ax.plot(x[:, 0], x[:, 1], y)
x = np.linspace([0, -5], [0, 5], 100)
ax.plot(x[:, 0], x[:, 1], y)
x = np.linspace([-5, 0], [5, 0], 100)
ax.plot(x[:, 0], x[:, 1], y)
ax.scatter(xopt, fopt, color="red")
plt.show()
