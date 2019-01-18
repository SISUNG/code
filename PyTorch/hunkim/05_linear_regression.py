import torch
import torch.nn as nn
from torch.autograd import Variable

x_data = Variable(torch.Tensor([[1.0],
                                [2.0],
                                [3.0]]))
y_data = Variable(torch.Tensor([[4.0],
                                [5.0],
                                [6.0]]))

class Model(nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.linear = nn.Linear(1,1)

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred

model = Model() #our model

criterion = nn.MSELoss(size_average=False)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

#training loop
for epoch in range(5000):
    y_pred = model(x_data)

    loss = criterion(y_pred, y_data)
    print(epoch, loss.data) #原来为loss.data[0]运行错误

    optimizer.zero_grad()
    loss.backward() #三个样本一起更新
    optimizer.step()

#after training
hour_var = Variable(torch.Tensor([[4.0]]))
y_pred = model(hour_var)
print('predict(after training)',4, model(hour_var).data[0][0])