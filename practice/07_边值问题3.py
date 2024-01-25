import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_bvp


def dy(x, y, p):
    lambda_ = p[0]
    q = 10
    dy0 = y[1]
    dy1 = (2 * q * np.cos(2 * x) - lambda_) * y[0]
    return np.asarray([dy0, dy1])


def bound(ya, yb, p):
    return np.asarray([ya[0] - 1, ya[0], yb[0]])


x = np.linspace(0, np.pi, 20)
y0 = np.cos(8 * x)
y1 = -3 * np.sin(8 * x)
y = np.asarray([y0, y1])
res = solve_bvp(dy, bound, x=x, y=y, p=[10])
x = np.linspace(0, np.pi, 100)
y = res.sol(x)
plt.plot(x, y[1], label="y'")
plt.plot(x, y[0], label="y")
plt.legend(loc='best')
plt.show()
