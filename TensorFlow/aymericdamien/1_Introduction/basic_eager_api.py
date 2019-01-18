from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
import tensorflow.contrib.eager as tfe

# set Eager API
print('Setting Eager mode...')
tfe.enable_eager_execution()

a = tf.constant(2)
print('a= %i' % a)
b = tf.constant(3)
c = tf.add(a, b)
print('c=%i' % c)