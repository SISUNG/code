import tensorflow as tf

"""
with tf.variable_scope('foo') as scope:
    v = tf.get_variable('v', [1])
    v2 = tf.get_variable('v2', [1])

assert v2.name == 'foo/v2:0'
"""

"""
with tf.variable_scope('foo') as scope:
    v = tf.get_variable('v', [1])

with tf.variable_scope('foo', reuse=True):
    v1 = tf.get_variable('v', [1])

assert v1 == v
"""

"""
with tf.variable_scope('foo') as foo_scope:
    v = tf.get_variable('v', [1])
with tf.variable_scope(foo_scope):
    w = tf.get_variable('w', [1])

assert w.name == 'foo/w:0'
"""

"""
#如果在开启的一个变量作用域里使用之前预先定义的一个作用域，则会跳过当前变量的作用域，保持预先存在的作用域不变
with tf.variable_scope('foo') as foo_scope:
    assert foo_scope.name == 'foo'

with tf.variable_scope('bar'):
    with tf.variable_scope('baz') as other_scope:
        assert other_scope.name == 'bar/baz'
        with tf.variable_scope(foo_scope) as foo_scope2:
            assert foo_scope2.name == 'foo'
    with tf.variable_scope('bay') as y_scope:
        assert y_scope.name == 'bar/bay'
"""

"""
with tf.variable_scope('foo', initializer=tf.constant_initializer(0.4)):
    v = tf.get_variable('v', [1])
    assert v.eval() == 0.4
"""
with tf.variable_scope('foo'):
    x = 1.0 + tf.get_variable('v', [1])
    assert x.op.name == 'foo/add'



