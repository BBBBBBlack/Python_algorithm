import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d  # 导入 scipy 中的二维插值工具 interp2d

# 生成已知数据网格点集 (xx,yy,z)
yy, xx = np.mgrid[-2:2:20j, -3:3:30j]  # 生成网格点 30x20 = 600
z = (1 - 0.5 * xx + xx ** 5 + yy ** 3) * np.exp(-xx ** 2 - 2 * yy ** 2)  # 计算网格点的值 z
x, y = xx[0, :], yy[:, 0]  # 由数据网格点 xx,yy 转换一维数组 x, y
print("shape of original dataset:\n\txx:{},yy:{},z:{}".format(xx.shape, yy.shape, z.shape))
print("\tx:{},y:{},z:{}".format(x.shape, y.shape, z.shape))

# 由给定数据点集 (x,y,z) 求插值函数 fInterp： x,y 是一维数组，z 是 len(x)*len(y) 二维数组
f1 = interp2d(x, y, z, kind='linear')  # 线性插值
f2 = interp2d(x, y, z, kind='cubic')  # 三阶样条插值
f3 = interp2d(x, y, z, kind='quintic')  # 五阶样条插值

# 由插值函数 fInterp 计算需插值的网格点集 ynew,xnew 的函数值
xnew = np.linspace(-3, 3, 120)  # xnew 是一维数组
ynew = np.linspace(-2, 2, 80)  # ynew 是一维数组
z1 = f1(xnew, ynew)  # 根据线性插值函数 f1 计算需插值的网格点集的函数值
z2 = f2(xnew, ynew)  # 根据三阶样条插值函数 f2 计算需插值的网格点集的函数值
z3 = f3(xnew, ynew)  # 根据五阶样条插值函数 f3 计算需插值的网格点集的函数值
print("shape of interpolation dataset:\n\txnew:{},ynew:{},znew:{}".format(xnew.shape, ynew.shape, z1.shape))

# 绘图
plt.figure(figsize=(20, 16))
plt.suptitle("2-D data interpolate")  # 全局标题
plt.subplot(221)
plt.pcolor(xx, yy, z, cmap=plt.cm.hsv, shading='auto')
plt.title("original")
plt.colorbar()
plt.subplot(222)
plt.pcolor(xnew, ynew, z1, cmap=plt.cm.hsv, shading='auto')
plt.title("linear")
plt.colorbar()
plt.subplot(223)
plt.pcolor(xnew, ynew, z2, cmap=plt.cm.hsv, shading='auto')
plt.title("cubic")
plt.colorbar()
plt.subplot(224)
plt.pcolor(xnew, ynew, z3, cmap=plt.cm.hsv, shading='auto')
plt.title("quintic")
plt.colorbar()
plt.show()
