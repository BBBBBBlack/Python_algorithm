import numpy
import pandas as pd
import torch
from matplotlib import pyplot as plt
from sklearn import preprocessing
from torch.utils.data import DataLoader

import MyDataSet
import MyNet

# 数据预处理
df = pd.read_excel("D:\\xxx\\Python_algorithm\\practice\\files\\NNs.xlsx")
fea = df.loc[df.shape[0] - 1, '年龄（岁）':'腕围 (cm)'].values
fea = fea.reshape(1, -1)
fea = preprocessing.StandardScaler().fit_transform(fea)
# 加载模型
device = 'cuda' if torch.cuda.is_available() else 'cpu'
# 使用与训练时相同的代码创建一个空模型
mynet = MyNet.MyNet(fea.shape[1]).to(device)
mynet.load_state_dict(torch.load('D:\\xxx\\Python_algorithm\\practice\\files\\mynet.pth'))
mynet.to(device)
# 预测
dataset = MyDataSet.MyDataSet(fea, None)
dataloader = DataLoader(dataset, batch_size=1, shuffle=True)
y_pred = []
for i, X in enumerate(dataloader):
    print(mynet(X).cpu().detach().numpy()[0][0])
