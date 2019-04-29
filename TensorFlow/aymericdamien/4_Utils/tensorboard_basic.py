import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

learning_rate = 0.01
training_epochs = 5
batch_size = 100
display_epoch = 1
logs_path = '/tmp/tensorflow_logs/example/'

x = tf.placeholder(tf.float32, [None,784],name='InputData')
y = tf.placeholder(tf.float32, [None, 10],name='LabelData')

w = tf.Variable(tf.zeros([784,10]), name='weights')
b = tf.Variable(tf.zeros([10]), name='bias')

with tf.name_scope('model'):
    pred = tf.nn.softmax(tf.matmul(x,w) + b)

with tf.name_scope('loss'):
    cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))

with tf.name_scope('sgd'):
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

with tf.name_scope('accuracy'):
    acc = tf.equal(tf.argmax(pred,1), tf.argmax(y,1))
    acc = tf.reduce_mean(tf.cast(acc, tf.float32))

init = tf.global_variables_initializer()

#create a summary to monitor some tensor
tf.summary.scalar('loss', cost)
tf.summary.scalar('accuracy', acc)
merged_summary_op = tf.summary.merge_all()

with tf.Session() as sess:
    sess.run(init)

    #op to write logs to tensorboard
    summary_writer = tf.summary.FileWriter(logs_path, graph=tf.get_default_graph())

    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            _, c, summary = sess.run([optimizer, cost, merged_summary_op],
                                     feed_dict={x:batch_xs, y:batch_ys})
            summary_writer.add_summary(summary,epoch*total_batch+i)
            avg_cost += c/total_batch

        if (epoch+1) % display_epoch == 0:
            print('Epoch:', '%04d' % (epoch+1),
                  'cost=', '{:.9f}'.format(avg_cost))

    print('Optimization Finished!')

    print('Accuracy:', acc.eval({x:mnist.test.images, y:mnist.test.labels}))

    print("Run the command line:\n" \
          "--> tensorboard --logdir=/tmp/tensorflow_logs " \
          "\nThen open http://0.0.0.0:6006/ into your web browser")