import torch as t
from matplotlib import pyplot as plt
from IPython import display

t.manual_seed(1000)#设置随机数种子，保证在不同计算机上运行时下面的输出一致

def get_fake_data(batch_size = 8):
    x = t.rand(batch_size, 1) * 20
    y = x * 2 + (1 + t.randn(batch_size, 1)) * 3
    return x, y

#x, y = get_fake_data()
#plt.scatter(x.squeeze().numpy(), y.squeeze().numpy())
#plt.show()

w = t.rand(1, 1)
b = t.zeros(1, 1)
lr = 0.001 #学习率

for ii in range(20000):
    x, y = get_fake_data()

    y_pred = x.mm(w) + b.expand_as(y)
    loss = 0.5 * (y_pred - y) ** 2 #均方根差
    loss = loss.sum()

    dloss = 1
    dy_pred = dloss * (y_pred - y)

    dw = x.t().mm(dy_pred)
    db = dy_pred.sum()

    w.sub_(lr * dw)
    b.sub_(lr * dw)

    if ii % 1000 == 0:
        display.clear_output(wait=True)
        x = t.arange(0, 20).view(-1, 1)
        y = x.mm(w) + b.expand_as(x)
        plt.scatter(x.numpy(), y.numpy())

        x2, y2 = get_fake_data(batch_size=20)
        plt.scatter(x2.numpy(), y2.numpy())#true data

        plt.xlim(0, 20)
        plt.ylim(0, 41)
        plt.show()
        plt.pause(0.5)
        plt.show()

        print(w.squeeze()[0], b.squeeze()[0])

