import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import pylab as plt
import seaborn as sns

batch = 10000
x = tf.random.uniform([batch])
y = tf.random.uniform([batch])

plt.subplot(1, 2, 1)
plt.scatter(x, y, s=0.1)

plt.subplot(1, 2, 2)
sns.histplot(x)

plt.show()
