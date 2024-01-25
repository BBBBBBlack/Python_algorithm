import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()
g.add_weighted_edges_from([(1, 2, 2), (1, 3, 8), (1, 4, 1),
                           (2, 3, 6), (2, 5, 1),
                           (3, 4, 7), (3, 5, 5), (3, 6, 1), (3, 7, 2),
                           (4, 7, 9),
                           (5, 6, 3), (5, 8, 2), (5, 9, 9),
                           (6, 7, 4), (6, 9, 6),
                           (7, 9, 3), (7, 10, 1),
                           (8, 9, 7), (8, 11, 9),
                           (9, 10, 1), (9, 11, 2),
                           (10, 11, 4)])
'''dijkstra'''
path = nx.dijkstra_path(g, 1, 11, "weight")
path_len = nx.dijkstra_path_length(g, 1, 11, "weight")
print("最短路径：" + str(path))
print("最短路径长度:" + str(path_len))

pos = {1: (0, 4), 2: (5, 7), 3: (5, 4), 4: (5, 1), 5: (10, 7), 6: (10, 4), 7: (10, 1),
       8: (15, 7), 9: (15, 4), 10: (15, 1), 11: (20, 4)}  # 指定顶点位置
labels = nx.get_edge_attributes(g, 'weight')  # 设置边的 labels 为 ‘weight'
nx.draw(g, pos, with_labels=True, font_color='w')  # 绘制无向图
nx.draw_networkx_edge_labels(g, pos, edge_labels=labels, font_color='c')  # 显示边的权值
plt.show()
