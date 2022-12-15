# 陣列, 在tf1時稱為 placeholder型態, 為常數, 變數後的第三種型態
# tf2 把 placeholder 移除掉不用了
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np

#a = tf.zeros(shape=(10))
a = tf.zeros(10)
b = np.zeros(10)
print(a)
print(b)

c = tf.zeros(shape=([2, 5]))
d = np.zeros([2, 5])
print(c)
print(d)

e = tf.ones([10])
f = np.ones([10])
print(e)
print(f)

print(e*10)
print(e+10)

g = tf.fill([2, 3], 5)
# h = np.fill([2, 3], 5)  # numpy沒有fill的功能
print(g)

i = tf.random.normal([10])  # 常態分布亂數
j = np.random.standard_normal([10])
j2 = np.random.normal(0, 10, 10)
print(i)
print(j)
print(j2)

k = tf.random.uniform([10])  # 產生均勻分布亂數
l = np.random.uniform(0, 1, 10)
print(k)
print(l)

# 可以指定 dtype, 最大值(不含), 最小值(包含)
m = tf.random.uniform([10], dtype=tf.int32, maxval=10, minval=5)
n = np.random.randint(5, 10, 10)
print(m)
print(n)

o = tf.range(0, 9, 2)  # range(最小值, 最大值(不含), 步進值)
print(o)
