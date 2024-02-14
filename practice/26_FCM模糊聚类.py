from sklearn import datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 萼片长度、萼片宽度、花瓣长度、花瓣宽度
iris = datasets.load_iris()
iris_data = iris.data  # ndarray(150, 4)
# 归一化
iris_data = iris_data / np.max(iris_data, axis=0)  # ndarray(150, 4)，[0,1]之间
# Setosa、Versicolour、Virginica
n_clusters = 3
# 隶属度矩阵u_ij，第i个样本属于第j个簇的隶属度
u = np.random.rand(iris_data.shape[0], n_clusters)  # ndarray(150, 3)
u = u / np.sum(u, axis=1)[:, None]
# 设置迭代次数
max_iter = 1000
# 聚类中心数组
centers = np.random.rand(n_clusters, iris_data.shape[1])  # ndarray(3, 4)
for i in range(max_iter):

    for j in range(n_clusters):
        # 计算聚类中心
        # centers[j] = np.sum(np.power(u[:, j], 3) * iris_data) / np.sum(np.power(u[:, j], 3))
        # 计算隶属度
        temp = 0
        for k in range(n_clusters):
            temp += np.power(np.sqrt(np.sum(np.power(iris_data - centers[j], 2), axis=1)
                                     / np.sum(np.power(iris_data - centers[k], 2), axis=1)), 2)
        # print(temp)
        u[:, j] = 1 / temp
        centers[j] = np.sum(np.power(u[:, j], 2)[:, None] * iris_data, axis=0) / np.sum(np.power(u[:, j], 2))

print(np.argmax(u, axis=1))
# print(iris.target)
