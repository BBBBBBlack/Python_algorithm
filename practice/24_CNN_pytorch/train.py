from torch.utils.data import DataLoader
from sklearn import preprocessing
from matplotlib import pyplot as plt

import MyDataSet
import MyNet
import pandas as pd
import torch.nn as nn
import torch

df = pd.read_csv("D:\\xxx\\Python_algorithm\\practice\\files\\weacher.csv")
# 数据预处理
label = df['actual'].values
# label = preprocessing.MinMaxScaler().fit_transform(label.reshape(-1, 1))
fea = df.drop('actual', axis=1)
fea_week = fea['week']
fea = fea.drop('week', axis=1)
fea = pd.concat([fea, pd.get_dummies(fea_week)], axis=1).values
fea = preprocessing.StandardScaler().fit_transform(fea)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
mynet = MyNet.MyNet(fea.shape[1]).to(device)
loss_func = nn.MSELoss()
optimizer = torch.optim.Adam(mynet.parameters(), lr=0.001)

dataset = MyDataSet.MyDataSet(fea, label)
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)
epoch = 1000
cost = []
for _ in range(epoch):
    for i, (X, y) in enumerate(dataloader):
        y = y.unsqueeze(1)
        y_pred = mynet(X)
        loss = loss_func(y_pred, y)
        # 梯度清零
        optimizer.zero_grad()
        # 反向传播
        loss.backward()
        # 更新参数
        optimizer.step()
        if i % 100 == 0:
            cost.append(loss.item())
plt.plot([i for i in range(len(cost))], cost)
plt.show()
# 保存模型
torch.save(mynet.state_dict(), 'D:\\xxx\\Python_algorithm\\practice\\files\\mynet.pth')
