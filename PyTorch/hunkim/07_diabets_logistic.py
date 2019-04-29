import torch
import torch.nn as nn
import numpy as np
from torch.autograd import Variable

xy = np.loadtxt('./data/diabetes.csv.gz', delimiter=',', dtype=np.float32)
x_data = Variable(torch.from_numpy(xy[:, 0:-1]))
y_data = Variable(torch.from_numpy(xy[:, [-1]]))    #索引操作

print(x_data.data.shape)    #torch.Size([759.8])
print(y_data.data.shape)    #torch.Size([759,1])

class Model(nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.l1 = nn.Linear(8,6)
        self.l2 = nn.Linear(6,4)
        self.l3 = nn.Linear(4,1)

        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        out1 = self.sigmoid(self.l1(x))
        out2 = self.sigmoid(self.l2(out1))
        y_pred = self.sigmoid(self.l3(out2))
        return y_pred

model = Model()

criterion = nn.BCELoss(size_average=True)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

for epoch in range(1000):
    y_pred = model(x_data)
    loss = criterion(y_pred, y_data)
    print(epoch, loss.data)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    


