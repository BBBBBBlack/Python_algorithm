import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''模拟退火算法'''


def get_distance_table(location):
    dist_table = np.zeros((len(location), len(location)))
    for i in range(len(location)):
        for j in range(len(location)):
            dist_table[i, j] = np.sqrt(np.sum(np.square(location[i] - location[j])))
    return dist_table


def cal_cost(x, dist_table):
    cost = 0
    for i in range(len(x)):
        cost += dist_table[x[i - 1], x[i]]
    return cost


# 读取Excel文件
df = pd.read_excel('files/citys.xlsx')
location = np.asarray(df[['经度', '纬度']].values)
location = np.append(location, location[0].reshape(1, 2), axis=0)
dist_table = get_distance_table(location)
# 1.初始化
t_0 = 100  # 设定初始退火温度
t_f = 1  # 设定最低温度
inter_iter = 1000  # 设定每个温度下的迭代次数
initial_x = np.arange(location.shape[0])  # 设定初始解
x = initial_x
t = t_0
recordBest = []
# 温度迭代
while t > t_f:
    temp = None
    for i in range(inter_iter):
        # 2.随机生成新解
        new_x = x.copy()
        # 生成两个随机数
        rand1 = np.random.randint(1, len(x) - 1)
        rand2 = np.random.randint(1, len(x) - 1)
        # 交换两个随机数的位置
        new_x[rand1], new_x[rand2] = new_x[rand2], new_x[rand1]
        # 3.计算新解的目标函数值
        old_cost = cal_cost(x, dist_table)
        new_cost = cal_cost(new_x, dist_table)
        # 4.判断是否接受新解
        if new_cost < old_cost:
            x = new_x
        else:
            p = np.exp(-(new_cost - old_cost) / t)
            if np.random.rand() < p:
                x = new_x
        temp = new_cost
    recordBest.append(temp)
    # 5.降温
    t = 0.99 * t
# 6.输出结果
print(x)
f1 = plt.figure()
plt.plot(recordBest)
f2 = plt.figure()
plt.plot(location[x, 0], location[x, 1])
plt.scatter(location[:, 0], location[:, 1], color='red')
print(cal_cost(x, dist_table))
plt.show()
# print(df[df.columns.array])
