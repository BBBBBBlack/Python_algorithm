import torch.nn as nn


class MyNet(nn.Module):
    def __init__(self, X_dimension):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(X_dimension, 128),
            nn.ReLU(),
            nn.Linear(128, 1),
        )

    def forward(self, X):
        return self.fc(X)
