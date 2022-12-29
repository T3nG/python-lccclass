# 求斜率, 也就是微分, 又稱為梯度下降(AI), 也有人稱導數(大陸), 其目的就是在找極值
# 在二維空間中的任何一條曲線, 都可以量化成一元多次方程式
# y = ax^5 + bx^4 + cx^3 + dx^2 + ex + f
# 在三維空間中, 任何一條曲線, 都可以量化成二元多次方程式
# z = ax^3 + by^3 + cx^2 + dy^2 + ex + fy + g
# 在 n 維資料中, 任何一條曲線都可以量化成 (n-1)元多次方程式
import threading
import time

import numpy as np
import pylab as plt


# 目標函數: 演算到最後, 最希望得到的函數
def f(x):
    # y = x^2
    return np.square(x)


def df(x):
    return 2*x
    # y'=2x = 0: 斜率為水平時, 表示有極值(最小/最大值)
    # 但是當函數過於複雜時, 就無法用微分找到極值, 要用逼近法來找極值


def bias(a, x):
    b = f(x) - a * x
    return b


def runnable():
    xs = np.linspace(-10, 10, 100)
    x = xs[0]
    points_x = [x]  # 歷史資料
    for i in range(epoch):
        ax.clear()
        ax.set_xlim(-11, 11)
        ax.set_ylim(-50, 200)
        ax.plot(xs, f(xs))
        # 繪製歷史資料
        ax.scatter(points_x, f(points_x), c='y')
        # 目前的點
        ax.scatter(x, f(x), c='g', s=200)
        # 導線 y'=ax+b
        a = df(x)
        b = bias(a, x)
        x_l = x - 3
        x_r = x + 3
        line_x = [x_l, x_r]
        line_y = [a * x_l + b, a * x_r + b]
        ax.plot(line_x, line_y, c='r')
        ax.text(-8, -15, f'{a} * x + {b}', c='r')
        # 開始逼近
        # x += 0.1
        # learning rate: 由導線斜率 * lr 來決定下一次 x 的步進值
        x = x - df(x) * lr
        points_x.append(x)
        plt.draw()
        time.sleep(0.03)


lr = 0.2
epoch = 200
ax = plt.subplot()
t = threading.Thread(target=runnable)
t.start()
plt.show()
