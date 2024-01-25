from scipy.integrate import odeint  # 导入 scipy.integrate 模块
import numpy as np
import matplotlib.pyplot as plt


def RLC(y, t, a, w):
    u, v = y
    du_dt = v
    dv_dt = -2 * a * v - (w ** 2) * u
    return [du_dt, dv_dt]


# y0初值
u0 = 1.0
v0 = 0.0
y = [u0, v0]
# t
t = np.arange(0, 30, 0.01)
# args
param = (1, 0.6)
track = odeint(RLC, y0=y, t=t, args=param)
plt.plot(t, track[:, 0], label="u1", color="blue")
param = (1, 1)
track = odeint(RLC, y0=y, t=t, args=param)
plt.plot(t, track[:, 0], label="u2", color="red")
param = (0.3, 1)
track = odeint(RLC, y0=y, t=t, args=param)
plt.plot(t, track[:, 0], label="u3", color="green")
plt.legend(loc='best')
plt.show()
