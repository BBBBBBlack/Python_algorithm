import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def func(x, a, b, c):
    return b * np.power(a, x) + c


if __name__ == "__main__":
    x = np.arange(1, 31, 1)
    y = np.array(
        [20, 23, 26, 29, 32, 35, 38, 45, 53, 62, 73, 86, 101, 118, 138, 161, 188, 220, 257, 300, 350, 409, 478, 558,
         651, 760, 887, 1035, 1208, 1410])

    popt, pcov = curve_fit(func, x, y)  # 曲线拟合，popt为函数的参数list
    y_pred = [func(i, popt[0], popt[1], popt[2]) for i in x]  # 直接用函数和函数参数list来进行y值的计算
    print(popt)
    print(pcov)

    plot1 = plt.plot(x, y, '*', label='original values')
    plot2 = plt.plot(x, y_pred, 'r', label='fit values')
    plt.title('')
    plt.xlabel('')
    plt.ylabel('')
    plt.legend(loc=3, borderaxespad=0., bbox_to_anchor=(0, 0))
    plt.show()
