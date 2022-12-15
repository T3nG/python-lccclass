import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import time
import numpy as np

x = tf.Variable(3.)
# 宣告函數原型 y=x^2
with tf.GradientTape() as prototype:
    y = tf.pow(x, 2)
# y 對 x 進行降階, 要微分的寫在後面
y_grad = prototype.gradient(y, x)
print('y=', y)
print('y_grad=', y_grad)

# s = v_0 * t + (1/2) * a * t^2
# 位移? 初速 + 加速
t = tf.Variable(10.)
g = tf.constant(9.8)
with tf.GradientTape() as prototype:
    s = 1/2 * g * tf.pow(t, 2)

# v = v_0 + gt
v = prototype.gradient(s, t)
print('十秒後移動的距離: ', s)
print(f'十秒後的速度: {v}m/s')
print(f'十秒後的速度: {v*3.6}km/hr')
# v: m/s => 1000/3600
