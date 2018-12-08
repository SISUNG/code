#autograd.Variable是Autograd中的核心类,Variable主要包含data、grad、grad_fn这三个属性
import torch as t
from torch.autograd import Variable

x = Variable(t.ones(2,2), requires_grad=True)
#print(x)
y = x.sum()
#print(y)

print(y.grad_fn)

y.backward()
print(x.grad)

y.backward()
print(x.grad)

y.backward()
print(x.grad)

y.backward()
print(x.grad.data.zero_())

y.backward()
print(x.grad)

x = Variable(t.ones(4, 5))
y = t.cos(x)
x_tensor_cos = t.cos(x.data)
print(y)
print(x_tensor_cos)