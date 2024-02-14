# 计算动量
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 标准化
def standardization(array):
    array = array.to_numpy()
    return (array - array.min()) / (array.max() - array.min())


# 变异系数法
def weight_cv(array):
    # 变异系数
    cv = np.std(array, axis=0) / np.mean(array, axis=0)
    return cv / cv.sum()


AC = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file\\AC_p2_1.csv")
ND = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file\\ND_p2_1.csv")
AC_perform = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file\\AC_p2_perform_mean.csv")
ND_perform = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file\\ND_p2_perform_mean.csv")

# 标准化
AC = standardization(AC)
ND = standardization(ND)
AC_weight = weight_cv(AC)
ND_weight = weight_cv(ND)
print(AC_weight)
print(ND_weight)
# 变异系数
AC_val = np.dot(AC, AC_weight)
ND_val = np.dot(ND, ND_weight)
plt.figure()
plt.title('Two players\' momentum')
plt.plot(AC_perform['0'].to_numpy(), AC_val, label='Carlos Alcaraz\'s momentum')
plt.plot(ND_perform['0'].to_numpy(), ND_val, label='Novak Djokovic\'s momentum')
plt.legend()

plt.figure()
plt.title('Carlos Alcaraz\'s momentum and mean performance')
plt.plot(AC_perform['0'].to_numpy(), AC_val, label='momentum')
plt.plot(AC_perform['0'].to_numpy(), AC_perform['1'].to_numpy(), label='mean performance')
plt.plot(AC_perform['0'].to_numpy(), AC_perform['con_pro_win'].to_numpy(), label='consecutive point win')
plt.legend()

plt.figure()
plt.title('Novak Djokovic\'s momentum and mean performance')
plt.plot(ND_perform['0'].to_numpy(), ND_val, label='momentum')
plt.plot(ND_perform['0'].to_numpy(), ND_perform['1'].to_numpy(), label='mean performance')
plt.plot(ND_perform['0'].to_numpy(), ND_perform['con_pro_win'].to_numpy(), label='consecutive point win')
plt.legend()

plt.figure()
plt.title('Carlos Alcaraz\'s momentum and mean performance difference')
plt.plot(AC_perform['0'].to_numpy(), AC_val, label='momentum')
plt.plot(AC_perform['0'].to_numpy(), AC_perform['1'].to_numpy() - ND_perform['1'].to_numpy(),
         label='mean performance difference')
plt.legend()

plt.figure()
plt.title('Novak Djokovic\'s momentum and mean performance difference')
plt.plot(ND_perform['0'].to_numpy(), ND_val, label='momentum')
plt.plot(ND_perform['0'].to_numpy(), ND_perform['1'].to_numpy() - AC_perform['1'].to_numpy(),
         label='mean performance difference')
plt.legend()
plt.show()

pd.concat([pd.DataFrame(AC_val, columns=['momentum']), AC_perform['1'] - ND_perform['1'], AC_perform['con_pro_win']],
          axis=1).to_csv("D:\\xxx\\Python_algorithm\\game\\file\\1.csv", index=False)

pd.concat([pd.DataFrame(ND_val, columns=['momentum']), ND_perform['1'] - AC_perform['1'], ND_perform['con_pro_win']],
          axis=1).to_csv("D:\\xxx\\Python_algorithm\\game\\file\\2.csv", index=False)