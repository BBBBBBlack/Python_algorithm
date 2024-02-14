import numpy
import pandas as pd
import torch
from matplotlib import pyplot as plt
from sklearn import preprocessing
from torch.utils.data import DataLoader

import MyDataSet
import MyNet

# 数据预处理
df = pd.read_csv("D:\\xxx\\Python_algorithm\\practice\\files\\weacher.csv")
label = df['actual'].values
fea = df.drop('actual', axis=1)
fea_week = fea['week']
fea = fea.drop('week', axis=1)
fea = pd.concat([fea, pd.get_dummies(fea_week)], axis=1).values
fea = preprocessing.StandardScaler().fit_transform(fea)
# 加载模型
device = 'cuda' if torch.cuda.is_available() else 'cpu'
# 使用与训练时相同的代码创建一个空模型
mynet = MyNet.MyNet(fea.shape[1]).to(device)
mynet.load_state_dict(torch.load('D:\\xxx\\Python_algorithm\\practice\\files\\mynet.pth'))
mynet.to(device)
# 预测
dataset = MyDataSet.MyDataSet(fea, label)
dataloader = DataLoader(dataset, batch_size=1, shuffle=True)
y_pred = []
for i, (X, y) in enumerate(dataloader):
    y_pred.append([y.cpu().detach().numpy()[0], mynet(X).cpu().detach().numpy()[0][0]])
y_pred = numpy.asarray(y_pred)
plt.plot([i for i in range(len(label))], y_pred[:, 0], color='blue')
plt.plot([i for i in range(len(y_pred))], y_pred[:, 1], color='red')
plt.show()
