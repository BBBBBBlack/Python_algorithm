import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

import MyDataSet
import MyModel

AC_res = pd.read_csv("/file/AC_res.csv")
AC_model = MyModel.MyModel(len(AC_res), 20, 1, 1)
x = AC_res['0'].to_numpy()
y = AC_res['1'].to_numpy()

loss_func = nn.MSELoss()
optimizer = torch.optim.Adam(AC_model.parameters(), lr=0.001)
dataset = MyDataSet.MyDataSet(x, y)
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)
