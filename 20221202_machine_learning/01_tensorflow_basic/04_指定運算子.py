import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

# tf會自動將 10包裝成 Tensor的物件
c1 = tf.constant(10)
print(c1 + 10)

# 不論是常數或變數運算, 都會產生新的常數
v1 = tf.Variable(20)
print(v1 + c1)

v2 = tf.Variable(30)
print(v1 + v2)
