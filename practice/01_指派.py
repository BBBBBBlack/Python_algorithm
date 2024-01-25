# 一些指派问题例子
from pulp import *
import numpy

prob = LpProblem('指派', sense=LpMinimize)
# 决策变量
rows = cols = range(0, 4)
x = LpVariable.dicts("x", (rows, cols), cat="Binary")
param = [[56, 74, 61, 63],
         [63, 69, 65, 71],
         [57, 77, 63, 67],
         [55, 76, 62, 62]]
# 目标函数
prob += lpSum([param[row][col] * x[row][col] for col in cols] for row in rows)
# 约束条件
for row in rows:
    prob += lpSum([x[row][col] for col in cols]) == 1
for col in cols:
    prob += lpSum([x[row][col] for row in rows]) == 1
status = prob.solve()
var_res = [v.varValue for v in prob.variables()]
var_res = numpy.array(var_res).reshape(4, 4)
print(var_res)
# print(f"目标函数的最小值z={value(prob.objective)}，此时目标函数的决策变量为:",
#       {v.name: v.varValue for v in prob.variables()})
