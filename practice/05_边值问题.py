import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_bvp  # 导入 scipy.integrate 模块


def dy(x, y):
    dy0 = y[1]
    dy1 = -abs(y[0])
    # print(np.vstack((dy0, dy1)).shape)
    return np.asarray([dy0, dy1])


def bound(y_a, y_b):
    ya = 0.5
    yb = -1.5
    return np.array([y_a[0] - ya, y_b[0] - yb])


res = solve_bvp(dy, bound, x=np.linspace(0, 4, 20), y=np.zeros((2, 20)))
x = np.linspace(0, 4, 100)
y = res.sol(x)
plt.plot(x, y[1], label="y'")
plt.plot(x, y[0], label="y")
plt.legend(loc='best')
plt.show()
