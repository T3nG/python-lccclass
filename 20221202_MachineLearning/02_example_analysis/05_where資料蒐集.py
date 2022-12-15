import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
import time

batch = 10

tf.random.set_seed(1)
x = tf.random.uniform([batch])
print('x:' ,x)

# 取索引
idx = tf.where(x <= 0.5)
print('idx: ', idx)

# 取值, gather: 收集, 聚餐
values = tf.gather(x, idx)
print('值: ', values)
