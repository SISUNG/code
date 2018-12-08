import torch as t
from torch.autograd import Variable as V

x = V(t.ones(1))
b = V(t.rand(1), requires_grad = True)
w = V(t.rand(1), requires_grad = True)

y = w * x
z = y + b

#print(x.requires_grad, b.requires_grad, w.requires_grad)

#print(y.requires_grad)

print(x.is_leaf, w.is_leaf, b.is_leaf, y.is_leaf, z.is_leaf)
print(z.grad_fn)
print(z.grad_fn.next_functions)

print(z.grad_fn.next_functions[0][0] == y.grad_fn)

print(y.grad_fn.next_functions)

print(w.grad_fn, x.grad_fn)

#print(y.grad_fn.saved_variables)#AttributeError: 'MulBackward1' object has no attribute 'saved_variables'

