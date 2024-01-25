# 1. 一维插值使用示例
import numpy as np
import matplotlib.pyplot as plt  # 导入 Matplotlib 工具包
from scipy.interpolate import interp1d  # 导入 scipy 中的一维插值工具 interp1d

# 已知数据点集 (x,y)
x = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0]  # 已知数据 x
y = [3.1, 2.7, 1.5, 0.1, 1.0, 3.9]  # 已知数据 y
# 由给定数据点集 (x,y) 求插值函数 fx
fx = interp1d(x, y, kind='linear')  # 由已知数据 (x,y) 求出插值函数 fx
# 由插值函数 fx 计算插值点的函数值
xInterp = np.linspace(0, 10, 100)  # 指定需插值的数据点集 xInterp
yInterp = fx(xInterp)  # 调用插值函数 fx，计算 xInterp 的函数值
# 绘图
plt.plot(xInterp, yInterp, label="linear interpolate")
plt.show()
