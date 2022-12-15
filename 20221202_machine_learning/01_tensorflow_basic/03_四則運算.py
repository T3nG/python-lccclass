import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

a = tf.constant(100)
b = tf.constant(5.)
c = tf.constant(5, dtype=tf.int64)
d = tf.constant(8)

# print(a+b)
# print(a+c)
# 型態不一樣不能做四則運算

print(a+d)  # 108
print(a-d)  # 92
print(a*d)  # 800
print(a/d)  # 12.5, 整數/整數=小數, 即使整除也是一樣, 傳統語言中會給商數
print(a//d)  # 求商數
print(a%d)  # 求餘數

x = tf.constant(100.)
y = tf.constant(8.)
print(x//y)  # 求商時, 型態為小數
print(x/y)

'''
小數相除/求商, 回傳小數 float32
小數無法求餘數

整數相除, 回傳小數 float64
整數求商, 回傳整數 int32
整數求餘, 回傳整數 int32
'''