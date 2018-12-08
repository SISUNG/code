from __future__ import print_function

import numpy as np
import torch as t

x = t.Tensor(5, 3)

x = t.rand(5, 3)

x.size()[0], x.size(1)

y = t.rand(5, 3)

#print(x + y)
#print(t.add(x, y))

result = t.Tensor(5, 3)
t.add(x, y, out=result)
#print(result)

#print('最初y')
#print(y)
#print('第一种加法，y的结果')
y.add(x)
#print(y)
#print('第二种加法， y的结果')
y.add_(x)#inplace加法
#print(y)

#print(x[:, 1])

a = t.ones(5)
b = a.numpy()#Tensor->Numpy

a = np.ones(5)
b = t.from_numpy(a)#Numpy->Tensor
#print(a)
#print(b)

b.add_(1)#Tensor和numpy对象共享内存，如果其中一个变了，另外一个也会随之改变
#print(a)
#print(b)


