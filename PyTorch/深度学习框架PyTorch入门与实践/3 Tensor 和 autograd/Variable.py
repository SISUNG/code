from __future__ import print_function
import torch as t
from torch.autograd import Variable as V

a = V(t.ones(3,4), requires_grad = True)
print(a)

b = V(t.zeros(3,4))
print(b)

c  =a.add(b)
print(c)

d = c.sum()
d.backward()
print(d)

print(c.data.sum())#得到float
print(c.sum())#后者计算sum后仍然是Variable

print(a.grad)

print(a.requires_grad, b.requires_grad, c.requires_grad)

print(a.is_leaf, b.is_leaf, c.is_leaf)
print(c.grad is None)

def f(x):
    y = x ** 2 * t.exp(x)
    return y

def gradf(x):
    dx = 2*x*t.exp(x) + x**2*t.exp(x)
    return dx

x = V(t.randn(3, 4), requires_grad = True)
y = f(x)
print(x)

y.backward(t.ones(y.size()))
print(x.grad)
print(gradf(x))