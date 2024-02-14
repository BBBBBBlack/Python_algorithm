import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

AC = pd.read_csv('D:\\xxx\\Python_algorithm\\game\\file2\\AC_momentum_trend.csv')
ND = pd.read_csv('D:\\xxx\\Python_algorithm\\game\\file2\\DM_momentum_trend.csv')
momentum_diff = AC['momentum'].to_numpy() - ND['momentum'].to_numpy()
momentum_diff = momentum_diff.reshape([1, -1])
# 设置分层聚类函数
linkages = ['ward', 'average', 'complete']
n_clusters_ = 4
ac = KMeans(n_clusters=n_clusters_, random_state=0)
# 训练数据
ac.fit(momentum_diff.T)

# 定义映射关系
mapping = {0: 1, 1: 3, 2: 2, 3: 0}

# 进行映射
label = [mapping[val] for val in ac.labels_]
# 定义状态空间和状态转移矩阵的大小
states = [0, 1, 2, 3]
n_states = len(states)
transition_matrix = np.zeros((n_states, n_states))

# 统计序列中的状态转移
sequence = label[:38]

for i in range(len(sequence) - 1):
    current_state = states.index(sequence[i])
    next_state = states.index(sequence[i + 1])
    transition_matrix[current_state, next_state] += 1

# 概率归一化
for i in range(n_states):
    transition_matrix[i, :] /= transition_matrix[i, :].sum()

# 预测后续值
num_predictions = 20
current_state = sequence[-1]
predicted_sequence = []

for _ in range(num_predictions):
    next_state = np.random.choice(states, p=transition_matrix[current_state])
    predicted_sequence.append(next_state)
    current_state = next_state
# 打印聚类中心
print("聚类中心：", sorted(ac.cluster_centers_, key=lambda x: x[0]))
# 打印聚类分析结果
print("原始动量差序列聚类结果：", label)
# 打印预测序列
print("预测序列（38-58）：", predicted_sequence)
# 打印状态转移矩阵
print("状态转移矩阵：", transition_matrix)
plt.figure(figsize=(8, 4), dpi=300)
plt.axhspan(-0.5, 0.5, color='#EFFFD0', alpha=0.2)
plt.axhspan(0.5, 1.5, color='#BAE3C3', alpha=0.2)
plt.axhspan(1.5, 2.5, color='#75D9B5', alpha=0.2)
plt.axhspan(2.5, 3.5, color='#31ACBA', alpha=0.2)
plt.scatter(range(1, len(label) + 1), label, label='actual sequence', s=10)
plt.scatter(range(len(sequence) + 1, len(sequence) + num_predictions + 1), predicted_sequence,
            s=10, color='#f3515f', label='predicted sequence')
plt.plot(range(1, len(label) + 1), label, label='actual sequence',
         linewidth=1)
plt.plot(range(len(sequence) + 1, len(sequence) + num_predictions + 1), predicted_sequence,
         color='#f3515f', label='predicted sequence', linewidth=1)
plt.yticks(range(5))
plt.ylim(-0.5, 3.5)
plt.xlabel('game no')
plt.ylabel('class')
plt.legend(prop={'size': 7}, loc='upper left')
plt.show()
