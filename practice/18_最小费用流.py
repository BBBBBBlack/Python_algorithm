import matplotlib.pyplot as plt
import networkx as nx

g = nx.DiGraph()  # 创建一个有向图 DiGraph
g.add_edges_from([('s', 'v1', {'capacity': 13, 'weight': 7}),
                  ('s', 'v2', {'capacity': 9, 'weight': 9}),
                  ('v1', 'v3', {'capacity': 6, 'weight': 6}),
                  ('v1', 'v4', {'capacity': 5, 'weight': 5}),
                  ('v2', 'v1', {'capacity': 4, 'weight': 4}),
                  ('v2', 'v3', {'capacity': 5, 'weight': 2}),
                  ('v2', 'v5', {'capacity': 5, 'weight': 5}),
                  ('v3', 'v4', {'capacity': 5, 'weight': 2}),
                  ('v3', 'v5', {'capacity': 4, 'weight': 1}),
                  ('v3', 't', {'capacity': 4, 'weight': 4}),
                  ('v4', 't', {'capacity': 9, 'weight': 7}),
                  ('v5', 't', {'capacity': 9, 'weight': 5})])

# 求最小费用最大流
# flowDict (dict)：字典类型，最小费用最大流的流经路径及各路径的分配流量
flowDict = nx.max_flow_min_cost(g, "s", "t")
# 由流经路径及各路径的分配流量 flowDict 计算可行流的成本
min_val = nx.cost_of_flow(g, flowDict)
print("最小费用最大流" + str(flowDict))
print("最小费用" + str(min_val))

# 输出标签(最大流量,所需费用)
cap = nx.get_edge_attributes(g, "capacity")
wei = nx.get_edge_attributes(g, "weight")
labels = {}
for label in cap.keys():
    labels[label] = "(" + str(cap[label]) + "," + str(wei[label]) + ")"

# 输出最小费用最大流real=xxx
for i in flowDict.keys():
    for j in flowDict[i].keys():
        if flowDict[i][j] > 0:
            labels[(i, j)] += ",real=" + str(flowDict[i][j])
nx.draw(g, pos=nx.shell_layout(g), with_labels=True, node_color='c', node_size=300, font_size=10)  # 绘制有向图，显示顶点标签
nx.draw_networkx_edge_labels(g, pos=nx.shell_layout(g), edge_labels=labels,
                             font_color='navy')  # 显示边的标签：'capacity' + maxFlow
plt.show()
