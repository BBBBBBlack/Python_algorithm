from itertools import cycle  # python自带的迭代器模块
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering, KMeans, MiniBatchKMeans, DBSCAN
from sklearn.datasets import make_blobs

# 产生随机数据的中心
centers = [[1, 1], [-1, -1], [1, -1]]
# 产生的数据个数
n_samples = 3000
# 生产数据，cluster_std是分散度，即数据点分布的分散程度，数值越大越分散
X, lables_true = make_blobs(n_samples=n_samples, centers=centers, cluster_std=0.6,
                            random_state=0)

# 设置分层聚类函数
linkages = ['ward', 'average', 'complete']
n_clusters_ = 3
ac = AgglomerativeClustering(linkage=linkages[0], n_clusters=n_clusters_)
# ac = KMeans(n_clusters=n_clusters_)
# ac = MiniBatchKMeans(n_clusters=n_clusters_)
# eps:区域半径，min_samples:簇的样本数目阈值
# ac = DBSCAN(eps=2.0, min_samples=10)
# 训练数据
ac.fit(X)

# 每个数据的分类
lables = ac.labels_

# 绘图
plt.figure(1)
plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    # 根据lables中的值是否等于k，重新组成一个True、False的数组
    my_members = lables == k
    # X[my_members, 0] 取出my_members对应位置为True的值的横坐标
    plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
plt.title('Estimated number of clusters: %d' % n_clusters_)

plt.figure(2)
plt.clf()
for k, col in zip(range(n_clusters_), colors):
    # 根据lables中的值是否等于k，重新组成一个True、False的数组
    my_members = lables_true == k
    # X[my_members, 0] 取出my_members对应位置为True的值的横坐标
    plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
plt.title('True number of clusters: %d' % n_clusters_)
plt.show()
