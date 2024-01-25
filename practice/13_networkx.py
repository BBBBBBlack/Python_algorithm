import networkx as nx
import matplotlib.pyplot as plt

g1 = nx.DiGraph()
# 节点
g1.add_node("A1")
# 一次多个
g1.add_nodes_from([("B1", dict(size=11)), ("B2", {"color": "blue"}), "B3"])
g1.add_node("C1", color="red", size=12)
print(g1.nodes)
# 各节点属性
print(g1._node)
# 边
g1.add_edge("A1", "B1", weight=0.5)
g1.add_edges_from([("A1", "B1", {'weight': 1}), ("A1", "B3", {'color': 'blue'})])
g1.add_weighted_edges_from([("B2", "C1", 2)])
print(g1.edges)
print(g1.get_edge_data("A1", "B3"))
# pos:
# nx.circular_layout：将节点围绕中心以圆形布局
# nx.random_layout：将节点随机分布在平面上
# nx.shell_layout：使用多个同心圆来布局节点
# nx.spring_layout：使用力导向算法来布局节点，使得连接的节点之间的距离尽可能相等
# nx.spectral_layout：使用图的特征向量来布局节点
nx.draw(g1, pos=nx.shell_layout(g1), with_labels=True)
nx.draw_networkx_edges(g1, pos=nx.shell_layout(g1), edgelist=[("A1", "B1")], width=2.0)
plt.show()
