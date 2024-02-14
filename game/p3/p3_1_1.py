# 引入所需的库
import joblib
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import random

total = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file\\Wimbledon_featured_matches.csv")
performance = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file\\1.csv")
# 创建虚拟的特征和标签数据
x = total.to_numpy()
y = performance['1'].to_numpy()

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 创建随机森林回归器并进行训练
reg = RandomForestRegressor(n_estimators=90, random_state=42)  # 创建随机森林分类器
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

plt.figure(figsize=(6, 4), dpi=300)
plt.plot(range(1, len(y) + 1), y, label='actual performance score difference')
plt.plot(range(len(y) - len(y_pred) + 1, len(y) + 1), y_pred, color='#f3515f',
         label='predict performance score difference')
plt.xlabel('game no')
plt.ylabel('score difference')
plt.ylim(-0.25, 0.3)
plt.legend(loc='upper left')

plt.figure(figsize=(6, 4), dpi=300)
plt.plot(range(1,len(y)+1), y, label='before')
random_list = [random.uniform(0, 2) for _ in range(len(x))]
x[:, total.columns.get_loc('serve')] *= random_list
y = reg.predict(x)
plt.plot(range(1, len(y) + 1), y, label='after', color='#f3515f')
plt.xlabel('game no')
plt.ylabel('score difference')
plt.ylim(-0.25, 0.3)
plt.legend(loc='upper left')
plt.show()

# 保存模型
joblib.dump(reg, "D:\\xxx\\Python_algorithm\\game\\file\\random_forest_model.pkl")
