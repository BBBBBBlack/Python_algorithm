import numpy as np
from scipy.optimize import brent
import matplotlib.pyplot as plt


# 1. Demo1：单变量无约束优化问题(Scipy.optimize.brent)
def func(x):  # 目标函数
    fx = x ** 2 - 8 * np.sin(2 * x + np.pi)
    return fx


xmin, fval, iter, funcalls = brent(func, brack=(-5.0, 2.0), full_output=True)
x = np.linspace(-10, 10, 100)
y = func(x)
plt.plot(x, y)
plt.scatter(xmin, fval, color="red")
plt.show()
