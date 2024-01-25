import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt


def func(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    return x1 ** 2 + x2 ** 2 + x3 ** 2 + 8


def constraint1(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    return x1 ** 2 - x2 + x3 ** 2


def constraint2(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    return -(x1 + x2 ** 2 + x3 ** 3 - 20)


def constraint3(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    return -x1 - x2 ** 2 + 2


def constraint4(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    return x2 + 2 * x3 ** 2 - 3


# 约束
cons1 = {'type': 'ineq', 'fun': constraint1}
cons2 = {'type': 'ineq', 'fun': constraint2}
cons3 = {'type': 'eq', 'fun': constraint3}
cons4 = {'type': 'eq', 'fun': constraint4}
cons = (cons1, cons2, cons3, cons4)
# 边界
b = (0.0, None)
bound = (b, b, b)
res = minimize(fun=func, x0=np.zeros(3), method='SLSQP', constraints=cons, bounds=bound)
print(res.x)
