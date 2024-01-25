import matplotlib.pyplot as plt
import networkx as nx

G1 = nx.Graph()
G1.add_weighted_edges_from([(1, 2, 5), (1, 3, 6), (2, 4, 2), (2, 5, 12), (3, 4, 6),
                            (3, 6, 7), (4, 5, 8), (4, 7, 4), (5, 8, 1), (6, 7, 5),
                            (7, 8, 10)])
T = nx.minimum_spanning_tree(G1)  # 返回包括最小生成树的图
print(T.edges(data=True))  # 最小生成树的边,data=True 表示返回值包括边的权重

mst1 = nx.tree.minimum_spanning_edges(G1, algorithm="kruskal")  # 返回最小生成树的边
print(list(mst1))  # 最小生成树的边
mst2 = nx.tree.minimum_spanning_edges(G1, algorithm="prim", data=False)  # data=False 表示返回值不带权
print(list(mst2))

# 绘图
pos = {1: (1, 5), 2: (3, 1), 3: (3, 9), 4: (5, 5), 5: (7, 1), 6: (6, 9), 7: (8, 7), 8: (9, 4)}  # 指定顶点位置
nx.draw(G1, pos=nx.shell_layout(G1), with_labels=True, node_color='c', alpha=0.8)  # 绘制无向图
labels = nx.get_edge_attributes(G1, 'weight')
nx.draw_networkx_edges(G1, pos=nx.shell_layout(G1), edgelist=T.edges, edge_color='b', width=4)  # 设置指定边的颜色
nx.draw_networkx_edge_labels(G1, pos=nx.shell_layout(G1), edge_labels=labels, font_color='m')  # 显示边的权值
plt.show()
