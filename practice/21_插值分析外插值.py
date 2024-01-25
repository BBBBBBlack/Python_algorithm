# 3. 一维插值方法(外插)
import numpy as np
import matplotlib.pyplot as plt  # 导入 Matplotlib 工具包
from scipy.interpolate import UnivariateSpline  # 导入 scipy 中的一维插值工具 UnivariateSpline

# 生成已知数据点集 (x,y)，需插值的数据点集 xnew
x = np.linspace(0, 10, 11)  # 生成已知数据点集的 x
y = np.cos((x) ** 2 / 30) * 2 + 2  # 生成已知数据点集的 y
xnew = np.linspace(-0.5, 10.5, 110)  # 指定需插值的数据点集 xnew

# 使用 UnivariateSpline 插值工具，由给定数据点集 (x,y) 求插值函数 fSpl
fSpl1 = UnivariateSpline(x, y, s=0)  # 三次样条插值，s=0：插值函数经过所有数据点
y1 = fSpl1(xnew)  # 由插值函数 fSpl1 计算插值点的函数值 y1

fSpl2 = UnivariateSpline(x, y)  # 三次样条插值，默认 s= len(w)
y2 = fSpl2(xnew + 10)  # 由插值函数 fSpl2 计算插值点的函数值 y2

fSpl2.set_smoothing_factor(0.1)  # 设置光滑因子 sf
y3 = fSpl2(xnew + 10)  # 由插值函数 fSpl2(sf=0.1) 计算插值点的函数值 y3

# 绘图
fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(x, y, 'ro', ms=5, label="data")
plt.plot(xnew, y1, 'm', label="3rd spline interpolate")
plt.plot(xnew + 10, y2, 'g', label="3rd spline fitting")
plt.plot(xnew + 10, y3, 'b--', label="smoothing factor")
ax.set_title("Data interpolate with extrapolation")
plt.legend(loc="best")
plt.show()
