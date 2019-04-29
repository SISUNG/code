import torch
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader

class DiabetesDataset(Dataset):
    def __init__(self):
        xy = np.loadtxt('./data/diabetes.csv.gz',
                             delimiter=',',
                             dtype=np.float32)
        self.len = xy.shape[0]
        self.x_data = torch.from_numpy(xy[:,0:-1])
        self.y_data = torch.from_numpy(xy[:, [-1]])

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len

dataset = DiabetesDataset()
train_loader = DataLoader(dataset=dataset,
                          batch_size=32,
                          shuffle=True,
                          num_workers=0)

class Model(nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.l1 = nn.Linear(8,6)
        self.l2 = nn.Linear(6,4)
        self.l3 = nn.Linear(4,1)

        self.sigmoid = nn.Sigmoid()
    def forward(self,x):
        out1 = self.sigmoid(self.l1(x))
        out2 = self.sigmoid(self.l2(out1))
        y_pred = self.sigmoid(self.l3(out2))
        return y_pred

model = Model()

criterion = nn.BCELoss(size_average=True)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

#training loop
for epoch in range(10):
    for i, data in enumerate(train_loader,0):
        inputs, labels = data
        inputs, labels = Variable(inputs), Variable(labels)

        y_pred = model(inputs)

        loss = criterion(y_pred,labels)
        print(epoch, i, loss.data)

        optimizer.zero_grad()   #zero gradients
        loss.backward() #perform a backward pass
        optimizer.step()    #update the weights

