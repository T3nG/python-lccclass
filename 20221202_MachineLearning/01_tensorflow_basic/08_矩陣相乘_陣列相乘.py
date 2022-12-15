import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

a = tf.constant([[1, 2, 3], [4, 5, 6]])  # 2*3
b = tf.constant([[1, 2], [3, 4], [5, 6]])  # 3*2
c = tf.constant([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])  # 3*5
print(a)
print(b)
print(tf.matmul(a, b))

'''
a (2* 3)
1 2 3
4 5 6

b (3 *2)
1 2
3 4
5 6

a第一列*b第一行 a第一列*b第二行
a第二列*b第一行 a第二列*b第二行
1*1+ 2*3+ 3*5  1*2+ 2*4+ 3*6
4*1+ 5*3+ 6*5  4*2+ 5*4+ 6*6
'''
# 第一個陣列的行 必須與第二個陣列的列 相同, 才可以相乘
# [2, 3] matmul [3, 5] -> 3 == 3 可以相乘 -> [2, 5]
print(tf.matmul(a, c))

# [3, 5] matmul [2, 3] -> 5 != 2 無法相乘
# print(tf.matmul(c, a))

# 底下為 陣列相乘, 相乘的陣列維度必須相同
ax = tf.constant([[1, 2, 3], [4, 5, 6]])  # 2*3
bx = tf.constant([[1, 2, 1], [2, 3, 2]])  # 2*3
print(ax * bx)
'''
1*1 2*2 3*1
4*2 5*3 6*2
'''
print(ax + bx)
print(ax - bx)
print(ax / bx)
