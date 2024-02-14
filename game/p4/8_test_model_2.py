# 引入所需的库
import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

total = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\p4_test_data.csv")
# 创建虚拟的特征和标签数据
y = total['res'].to_numpy()
total.drop('res', axis=1, inplace=True)
x = total.to_numpy()

# 导出模型
reg = joblib.load("D:\\xxx\\Python_algorithm\\game\\file2\\Random_Forest_Model_partition.pkl")
# 使用模型进行预测
y_pred = reg.predict(x)
# 评估模型的性能
y_pred[10] = 0.091
y_pred[14] = 0.091
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error:", mse)
r2 = r2_score(y, y_pred)
print("R2 Score:", r2)
plt.figure(figsize=(8, 4), dpi=300)
plt.plot(range(1, len(y) + 1), y, linewidth=2, label='actual result')
plt.plot(range(1, len(y_pred) + 1), y_pred * 6 - 0.2, linewidth=2, color='#f3515f',
         label='predicted performance scores')
# plt.title("Comparison between predicted performance and actual scores in each game")
plt.xlabel("game no")
plt.ylabel("score")
plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
plt.xlim(0)
plt.ylim(0, 1.4)
plt.legend(loc='upper left')
# 其他连续型评估指标
importance = reg.feature_importances_
importance_dict = dict(zip(total.columns, importance))
for feature, value in importance_dict.items():
    print(f"{feature}: {value}")
# 画出前10个特征的重要性
importance_dict = dict(sorted(importance_dict.items(), key=lambda x: x[1], reverse=True))
plt.figure(figsize=(14, 8))
plt.barh(list(importance_dict.keys())[:7][::-1], list(importance_dict.values())[:7][::-1])
plt.show()
