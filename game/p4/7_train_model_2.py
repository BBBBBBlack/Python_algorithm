# 仅适用于网络数据
# 引入所需的库
from itertools import islice

import joblib
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import random

total = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\p4_train_data.csv")
performance = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\AC_momentum_trend.csv")
# 创建虚拟的特征和标签数据
x = total.to_numpy()
y = performance['mean_performance'].to_numpy()

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 创建随机森林回归器并进行训练
reg = RandomForestRegressor(n_estimators=46, random_state=32)  # 创建随机森林分类器
reg.fit(X_train, y_train)  # 使用训练集进行训练

# 使用训练好的模型进行预测
# 使用训练好的模型进行预测
y_pred = reg.predict(X_test)

# 评估模型的性能（使用均方误差作为评估指标）
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
# 其他连续型评估指标
r2 = r2_score(y_test, y_pred)
print("R2 Score:", r2)
importance = reg.feature_importances_
importance_dict = dict(zip(total.columns, importance))
for feature, value in importance_dict.items():
    print(f"{feature}: {value}")

# 柱状图
# plt.figure(figsize=(10, 8))
# sorted_dict = dict(sorted(importance_dict.items(), key=lambda x: x[1],reverse=True))
# top_8 = dict(islice(sorted_dict.items(), 8))
# keys = list(top_8.keys())
# values = list(top_8.values())
# plt.barh(keys[::-1], values[::-1])
# 画出前10个特征的重要性
importance_dict = dict(sorted(importance_dict.items(), key=lambda x: x[1], reverse=True))
plt.figure(figsize=(14, 8),dpi=300)
plt.gca().set_aspect(0.06)
plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)
plt.xlabel('importance', fontsize=16)
colors = ['#263d71', '#3b63a1', '#80abd6', '#a6c9e5', '#5b9abb', '#46a7ae', '#81cfd1']
plt.barh(list(importance_dict.keys())[:7][::-1], list(importance_dict.values())[:7][::-1],
         color=colors)
for i, v in enumerate(list(importance_dict.values())[:7][::-1]):
    plt.text(v, i, '{:.2f}'.format(v), color='black', va='center', fontsize=14)

# plt.show()

# 画出真实值和预测值的对比图
plt.figure()
plt.plot(range(1, len(y) + 1), y, label='True')
plt.plot(range(len(y) - len(y_pred) + 1, len(y) + 1), y_pred, label='Predict')
plt.legend()
plt.figure()
plt.plot(range(len(y)), y, label='before')
random_list = [random.uniform(0, 10) for _ in range(len(x))]
x[:, total.columns.get_loc('speed_mph')] *= random_list
y = reg.predict(x)
plt.plot(range(len(y)), y, label='after')
plt.legend()
plt.show()

# 保存模型
joblib.dump(reg, "D:\\xxx\\Python_algorithm\\game\\file2\\Random_Forest_Model_partition.pkl")
