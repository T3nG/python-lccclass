import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import time
import numpy as np

batch = 100_000

incircle = 0
# 平均產生 batch個, 0~1 的 float64小數
xs = np.linspace(tf.cast(0., dtype=tf.float64), 1., batch)
ys = np.linspace(tf.cast(0., dtype=tf.float64), 1., batch)
for i, x in enumerate(xs):
    dist = tf.sqrt(tf.square(x) + tf.square(ys))
    incircle += tf.where(dist < 1).shape[0]
    pi = incircle / ((i+1)*batch) * 4
    print(f'\rEpoch: {i+1:,}, pi={pi}', end='')
# 100,000 => 3.1415696928
# 因為不是亂數產生, 最後的結果會一致
