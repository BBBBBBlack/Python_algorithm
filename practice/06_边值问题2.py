import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_bvp


def dh(x, h):
    dh0 = h[1]
    dh1 = (h[0] - 1) * ((1 + (h[1] ** 2)) ** 1.5)
    return np.asarray([dh0, dh1])


def bound(y_a, y_b):
    return np.array([y_a[0], y_b[0]])


res = solve_bvp(dh, bound, np.linspace(-1, 1, 20), np.zeros((2, 20)))
x = np.linspace(-1, 1, 100)
y = res.sol(x)
plt.plot(x, y[0], label="y'")
plt.plot(x, y[1], label="y")
plt.legend(loc='best')
plt.show()
