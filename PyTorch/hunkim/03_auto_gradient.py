import torch
from torch.autograd import Variable

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = Variable(torch.Tensor([1.0]), requires_grad=True)
# print(w.size()) #torch.Size([1])
# print(w.data)   #tensor([1.])
# print(w.data[0])    #tensor([1.])

def forward(x):
    return x*w

def loss(x,y):
    y_pred = forward(x)
    return (y_pred - y)*(y_pred-y)

print('predict(before training)', 4, forward(4).data[0])    #返回标量

#Training loop
for epoch in range(100):
    for x_val, y_val in zip(x_data, y_data):
        l = loss(x_val,y_val)#l只计算了一个样本
        l.backward()
        print('\tgrad: ', x_val, y_val, w.grad.data[0])
        w.data = w.data - 0.01*w.grad.data

        w.grad.data.zero_()
    print('process： ', epoch, l.data[0])

#after training
print('predict(after training', 4, forward(4).data[0])

