import matplotlib.pyplot as plt
import pandas as pd
import torch
import torch.nn as nn


class RegLSTM(nn.Module):
    def __init__(self, inp_dim, out_dim, mid_dim, mid_layers):
        super(RegLSTM, self).__init__()

        self.rnn = nn.LSTM(inp_dim, mid_dim, mid_layers)  # rnn
        self.reg = nn.Sequential(
            nn.Linear(mid_dim, mid_dim),
            nn.Tanh(),
            nn.Linear(mid_dim, out_dim),
        )  # regression

    def forward(self, x):
        y = self.rnn(x)[0]  # y, (h, c) = self.rnn(x)
        seq_len, batch_size, hid_dim = y.shape
        y = y.view(-1, hid_dim)
        y = self.reg(y)
        y = y.view(seq_len, batch_size, -1)
        return y

    def output_y_hc(self, x, hc):
        y, hc = self.rnn(x, hc)  # y, (h, c) = self.rnn(x)

        seq_len, batch_size, hid_dim = y.size()
        y = y.view(-1, hid_dim)
        y = self.reg(y)
        y = y.view(seq_len, batch_size, -1)
        return y, hc


AC = pd.read_csv("D:\\xxx\\Python_algorithm\\game\\file2\\AC_perform.csv")
AC = AC.iloc[:, 1:].to_numpy()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ND = ND.iloc[:, 1:]
# pre = pd.concat([AC, ND])
# 时间序列预测
train_x = AC[:len(AC) - 10, 0].reshape(len(AC) - 10, 1, 1)
train_y = AC[10:len(AC), 0].reshape(len(AC) - 10, 1, 1)
batch_x = torch.tensor(train_x, dtype=torch.float32, device=device)
batch_y = torch.tensor(train_y, dtype=torch.float32, device=device)
# 加载模型
model = RegLSTM(1, 1, 32, 2).to(device)
loss = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-2)

# 开始训练
print("Training......")
loss_=[]
for e in range(1000):
    out = model(batch_x)

    Loss = loss(out, batch_y)

    optimizer.zero_grad()
    Loss.backward()
    optimizer.step()

    if e % 10 == 0:
        print('Epoch: {:4}, Loss: {:.5f}'.format(e, Loss.item()))
        loss_.append(Loss.item())
torch.save(model.state_dict(), 'D:\\xxx\\Python_algorithm\\game\\file2\\net.pth')
plt.figure(figsize=(10, 6), dpi=300)
plt.plot(range(len(loss_)), loss_)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()
# 预测
# model = RegLSTM(1, 1, 32, 2).to(device)
# model.load_state_dict(torch.load('D:\\xxx\\Python_algorithm\\game\\file2\\net.pth'))
# model.eval()
# temp = AC.reshape([len(AC), 1, 1])
# temp = torch.tensor(temp, dtype=torch.float32, device=device)
# y_pred = model(temp)
# y_pred = y_pred.cpu()
# y_pred = y_pred.view(-1).detach().numpy()
# plt.figure(figsize=(10, 6), dpi=300)
# plt.plot(range(len(AC)), AC, label='Carlos Alcaraz\'s actual performance score')
# plt.plot(range(10, len(y_pred) + 10), y_pred, color='#f3515f',
#          label='Carlos Alcaraz\'s predict performance score')
# # plt.title('Performance Predict By LSTM')
# plt.xlabel('point no')
# plt.ylabel('performance score')
# plt.legend(loc='upper left')
# plt.show()
