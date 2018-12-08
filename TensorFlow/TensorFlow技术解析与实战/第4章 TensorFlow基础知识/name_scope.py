import tensorflow as tf
with tf.variable_scope('foo'):
    with tf.name_scope('bar'):
        v = tf.get_variable('v', [1])
        b = tf.Variable(tf.zeros([1]), name='b')
        x = 1.0 + v

assert v.name == 'foo/v:0'
assert b.name == 'foo/bar/b:0'
assert x.op.name == 'foo/bar/add'