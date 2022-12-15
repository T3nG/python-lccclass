import os

import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

a = tf.constant(10)
# [] 未填入, 0維度, 也就是一般的constant, 基本上不能稱為陣列, 稱為純量
b = tf.ones([], dtype=tf.int32) * 10
print(a)
print(b)
# print(b[0]) 會出錯, b不是陣列

# 一維一元素陣列, 可以用 []指定索引
c = tf.ones([1], dtype=tf.int32) * 10
print(c)
print(c[0])

# 一維多元素陣列
d = tf.ones([10], dtype=tf.int32) * 10
print(d)
print(d[5])

e = tf.ones([3, 5], dtype=tf.int32) * 10
print(e)
print(e[0])
print(e[0][0])
print(e.shape)
print(e.shape[0])  # 列 row
print(e.shape[1])  # 行 column

d_reshape = tf.reshape(d, [2, 5])  # 2*5=10 , 總元素量不變
print(d_reshape)

# 指定陣列的值, 需放到變數裡再去作變更
# 陣列其實是多個常數的集合, 根本不能變更裡面的值
x = tf.zeros([2, 3], dtype=tf.int32)
y = tf.Variable(x)
# y = tf.Variable(tf.zeros([2, 3], dtype=tf.int32))
y[0, 0].assign(100)
print(y)
print(x)
