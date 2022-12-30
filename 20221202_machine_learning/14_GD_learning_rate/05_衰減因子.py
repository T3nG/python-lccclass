# 衰減因子公式: decay 衰退
# lr_i = lr_0 / (1 + decay * i), i: 迭代第幾次
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
        # 每次的學習率會隨著迭代次數改變
        lr_i = lr / (1+decay * i)
        x = x - df(x) * lr_i
        points_x.append(x)
        plt.draw()
        time.sleep(0.03)


# 衰減因子愈大, 衰退愈慢, 反之愈快
decay = 0.5
lr = 0.2
epoch = 200
ax = plt.subplot()
t = threading.Thread(target=runnable)
t.start()
plt.show()
