from torch.nn import init
import torch as t
from torch import nn
linear = nn.Linear(3, 4)

t.manual_seed(1)
print(init.xavier_normal(linear.weight))

import math
t.manual_seed(1)

std = math.sqrt(2)/math.sqrt(7.)
print(linear.weight.data.normal_(0, std))