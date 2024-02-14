import scipy.cluster.hierarchy as hierarchy  # 导入层次聚类算法
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt


centers = [[1, 1], [-1, -1], [1, -1]]
# 产生的数据个数
n_samples = 30
# 生产数据，cluster_std是分散度，即数据点分布的分散程度，数值越大越分散
X, lables_true = make_blobs(n_samples=n_samples, centers=centers, cluster_std=0.6,
                            random_state=0)
plt.figure(1)
hierarchy.dendrogram(hierarchy.ward(X))
(plt.figure(2))
hierarchy.dendrogram(hierarchy.average(X))
plt.figure(3)
hierarchy.dendrogram(hierarchy.complete(X))
plt.show()
# 画图，ax.get_xbound()是x轴范围，[7.25, 7.25]是y轴的范围，在y=7.25的地方画一条虚线
# ax = plt.gca()
# ax.plot(ax.get_xbound(), [7.25, 7.25], '--', c='k')
