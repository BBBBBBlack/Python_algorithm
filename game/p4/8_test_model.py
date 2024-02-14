# 引入所需的库
import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

total = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\all_element.csv")
performance = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\AC_momentum_trend.csv")
# 创建虚拟的特征和标签数据
x = total.to_numpy()
y = performance['mean_performance'].to_numpy()

# 导出模型
reg = joblib.load("D:\\xxx\\Python_algorithm\\game\\file\\random_forest_model.pkl")
# 使用模型进行预测
y_pred = reg.predict(x)
# 评估模型的性能
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error:", mse)
r2 = r2_score(y, y_pred)
print("R2 Score:", r2)
# 其他连续型评估指标
importance = reg.feature_importances_
importance_dict = dict(zip(total.columns, importance))
for feature, value in importance_dict.items():
    print(f"{feature}: {value}")
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

plt.show()
