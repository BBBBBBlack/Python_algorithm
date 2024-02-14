from torch.utils.data import DataLoader
from sklearn import preprocessing
from matplotlib import pyplot as plt

import MyDataSet
import MyNet
import pandas as pd
import torch.nn as nn
import torch

df = pd.read_excel("D:\\xxx\\Python_algorithm\\practice\\files\\NNs.xlsx")
# 数据预处理
df = df.loc[0:df.shape[0] - 2, '年龄（岁）':'体脂率']
label = df['体脂率'].values
# label = preprocessing.MinMaxScaler().fit_transform(label.reshape(-1, 1))
fea = df.loc[:, :'腕围 (cm)'].values
fea = preprocessing.StandardScaler().fit_transform(fea)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
mynet = MyNet.MyNet(fea.shape[1]).to(device)
loss_func = nn.MSELoss()
optimizer = torch.optim.Adam(mynet.parameters(), lr=0.001)

dataset = MyDataSet.MyDataSet(fea, label)
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)
epoch = 2000
cost = []
for _ in range(epoch):
    for i, (X, y) in enumerate(dataloader):
        y = y.unsqueeze(1)
        y_pred = mynet(X)
        loss = loss_func(y_pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if i % 100 == 0:
            print("loss:" + str(loss.item()))
            cost.append(loss.item())
plt.plot([i for i in range(len(cost))], cost)
plt.show()
# 保存模型
torch.save(mynet.state_dict(), 'D:\\xxx\\Python_algorithm\\practice\\files\\mynet.pth')