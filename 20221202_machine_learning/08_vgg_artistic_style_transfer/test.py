import tensorflow as tf

a = tf.constant([6,2])
b = tf.constant([3,4])
c = tf.square(a-b)
print(c)
# (6-3)^2  (2-4)^2
print(tf.reduce_sum(c))
