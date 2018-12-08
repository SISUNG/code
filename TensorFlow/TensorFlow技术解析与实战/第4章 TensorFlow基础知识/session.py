"""
import tensorflow as tf
a = tf.constant([1.0, 2.0])
b = tf.constant([3.0, 4.0])
c = a * b
sess = tf.Session()
print(sess.run(c))
sess.close()
"""
"""
import tensorflow as tf
m1 = tf.constant([[3., 3.]], dtype= tf.float32)
m2 = tf.constant([[2.],
                  [2.]], dtype= tf.float32)
product = tf.matmul(m1, m2)

with tf.Session() as sess:
    with tf.device('/cpu:0'):
        result = sess.run([product])
        print(result)
"""

