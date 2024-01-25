from pulp import *
import numpy

prob = LpProblem("集合覆盖", sense=LpMinimize)
l = list(range(8))
# 决策变量
x = LpVariable.dicts("x", l, cat="Binary")
# 目标函数
prob += lpSum(x[i] for i in l)
# 约束条件
origin = [[7, 12, 18, 20, 24, 26, 25, 28],
          [14, 5, 8, 15, 16, 18, 18, 18],
          [19, 9, 4, 14, 10, 22, 16, 13],
          [14, 15, 15, 10, 18, 15, 14, 18],
          [20, 18, 12, 20, 9, 25, 14, 12],
          [18, 21, 20, 16, 20, 6, 10, 15],
          [22, 18, 20, 15, 16, 15, 5, 9],
          [30, 22, 15, 20, 14, 18, 8, 6]]
origin = numpy.array(origin)
r = numpy.where(origin <= 10, 1, 0)
for i in l:
    prob += lpSum([r[i][j] * x[j] for j in l]) >= 1
prob.solve()
var_res = [v.varValue for v in prob.variables()]
print(var_res)
