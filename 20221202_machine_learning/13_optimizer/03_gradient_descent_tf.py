# pip install tensorflow==2.10.1
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import threading
import time

import numpy as np
import pylab as plt
import tensorflow as tf


# 目標函數
def f(x):
    return np.square(x)


def bias(a, x):
    b = f(x) - a * x
    return b


def runnable():
    xs = tf.linspace(-10, 10, 100)
    x = tf.Variable(-10.)  # 一定要用 Variable, 不可以使用 constant
    points_x = [x]
    for i in range(epoch):
        with tf.GradientTape() as tape:
            y = tf.pow(x, 2)  # 梯度下降後, 會改 x 的值, 所以 x 一定要用 Variable
        ax.clear()
        ax.set_xlim(-11, 11)
        ax.set_ylim(-50, 200)
        ax.plot(xs, f(xs))
        ax.scatter(points_x, f(points_x), c='y')
        ax.scatter(x, f(x), c='g', s=200)
        # 進行微分
        a = tape.gradient(y, x)  # y對x微分, 要微分的參數放後面
        b = bias(a, x)
        x_l = x - 3
        x_r = x + 3
        line_x = [x_l, x_r]
        line_y = [a * x_l + b, a * x_r + b]
        ax.plot(line_x, line_y, c='r')
        ax.text(-8, -15, f'{a} * x + {b}', c='r')
        # 逼近
        v = -a * lr
        x = tf.Variable(x+v)
        points_x.append(x)
        plt.draw()
        time.sleep(0.03)



lr = 0.2
epoch = 100
ax = plt.subplot()
t = threading.Thread(target=runnable)
t.start()
plt.show()
