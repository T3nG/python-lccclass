# http://mahaljsp.asuscomm.com/index.php/2021/01/09/%e5%be%ae%e5%88%86/
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

# L(w, b) = E(xw + b - y)^2
# x, y 已知的幾個點
x = tf.constant([[1., 2.], [3., 4.]])
y = tf.constant([[1.], [2.]])
# w, b 指定初值 , initial_value 可以不用打, 因為這兩個是變數是會變的
w = tf.Variable(initial_value=[[1.], [2.]])
b = tf.Variable(initial_value=1.)
with tf.GradientTape() as tape:
    L = tf.reduce_sum(tf.square(tf.matmul(x, w) + b - y))
# L 對 w, b 做偏微分
w_grad, b_grad = tape.gradient(L, [w, b])
print('L:', L)
print('w_grad: ', w_grad)
print('b_grad: ', b_grad)
