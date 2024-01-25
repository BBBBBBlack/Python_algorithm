import numpy as np

origin = np.asarray([[24, 180, 60, 90, 5000.0],
                     [23, 175, 90, 85, 10000],
                     [23, 170, 95, 92, 8000],
                     [24, 185, 81, 100, 5500],
                     [25, 190, 79, 60, 2000]])
# 正向化
# 年龄：极小-极大
origin[:, 0] = np.max(origin[:, 0]) - origin[:, 0]
# 身高：中间-极大
M = np.max(np.abs(origin[:, 1] - 180))
origin[:, 1] = 1 - (np.abs(origin[:, 1] - 180) * 1.0 / M * 1.0)
# 长相：区间（80-90）-极大
M = max(80 - np.min(origin[:, 2]), np.max(origin[:, 2] - 90))
temp = origin[:, 2]
temp[temp < 80] = 1 - (80 - temp[temp < 80]) / M
mask = np.logical_and(temp >= 80, temp <= 90)
temp[mask] = 1
temp[temp > 90] = 1 - (temp[temp > 90] - 90) / M
origin[:, 2] = temp
# 标准化
origin = origin / np.sqrt(np.sum(np.power(origin, 2), axis=0))
# 计算比重
origin = origin / np.sum(origin, axis=0)
# 计算信息熵
origin[origin == 0] = 0.00001
ej = -1 / np.log(5) * np.sum(origin * np.log(origin), axis=0)
dj = 1 - ej
# 计算权值
Wj = dj / np.sum(dj)
print(Wj)
