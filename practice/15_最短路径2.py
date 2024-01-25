import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

g = pd.DataFrame([[0, 50, 0, 40, 25, 10],  # 0 表示不邻接，
                  [50, 0, 15, 20, 0, 25],
                  [0, 15, 0, 10, 20, 0],
                  [40, 20, 10, 0, 10, 25],
                  [25, 0, 20, 10, 0, 55],
                  [10, 25, 0, 25, 55, 0]])
g = nx.from_pandas_adjacency(g)

'''bellman_ford'''
path = nx.bellman_ford_path(g, source=0, target=3)
path_len = nx.bellman_ford_path_length(g, source=0, target=3)
print("最短路径：" + str(path))
print("最短路径长度:" + str(path_len))

nx.draw(g, pos=nx.shell_layout(g), with_labels=True, font_color='w')  # 绘制无向图
labels = nx.get_edge_attributes(g, 'weight')  # 设置边的 labels 为 ‘weight'
nx.draw_networkx_edge_labels(g, pos=nx.shell_layout(g), edge_labels=labels, font_color='c')  # 显示边的权值
plt.show()
