from torch.utils.data import Dataset, DataLoader
import torch
import torch.nn as nn


class MyDataSet(Dataset):
    def __init__(self, X, y):
        self.X = None
        self.y = None
        super().__init__()
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        if X is not None:
            X = torch.tensor(X).float()
            self.X = X.to(device)
        if y is not None:
            y = torch.tensor(y).float()
            self.y = y.to(device)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        if self.y is None:
            return self.X[index]
        return self.X[index], self.y[index]
