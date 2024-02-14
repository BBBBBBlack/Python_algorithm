import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt


def dx1_dt(x1, t, a, b):
    return b - a * x1


x0 = np.asarray([71.1, 72.4, 72.4, 72.1, 71.4, 72.0, 71.6])
# 级比检验
temp = x0[:-1] / x0[1:]
n = len(x0)
if np.exp(-2 / (n + 1)) < np.all(temp) < np.exp(2 / (n + 1)):
    print('级比检验通过')
else:
    exit('级比检验未通过')
# 累加生成
x1 = np.cumsum(x0)
# 累加平均生成
z1 = 0.5 * x1[1:] + 0.5 * x1[:-1]
Y = x0[1:].reshape(n - 1, 1)
B = np.c_[-z1.reshape(n - 1, 1), np.ones(n - 1).reshape(n - 1, 1)]
u = np.dot(np.dot(np.linalg.inv(np.dot(B.T, B)), B.T), Y)
# 预测值
# 方法1
y = odeint(dx1_dt, x1[1], np.linspace(1, 10, 10), args=(u[0], u[1]))
# 方法2
y2 = (x0[0] - u[1] / u[0]) * np.exp(-u[0] * np.linspace(1, 10, 10)) + u[1] / u[0]
plt.plot(np.linspace(1, 10, 10), y)
plt.plot(np.linspace(1, 10, 10), y2)
plt.show()
res = y[7] - y[6]
res2 = y2[7] - y2[6]
print(res)
print(res2)
# print(odeint(dx1_dt, x1[2], np.linspace(2, 10, 20), args=(u[0], u[1])))
