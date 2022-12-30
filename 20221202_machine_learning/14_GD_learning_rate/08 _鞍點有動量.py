import threading
import time
import numpy as np
import pylab as plt


def f(x):
    x = np.array(x)
    y = (np.power(x, 4) - 60 * np.power(x, 3) - x + 1) / shrink_y
    return y


def df(x):
    return (4 * x ** 3 - 180 * x ** 2 - 1) / shrink_y


def bias(a, x):
    b = f(x) - a * x
    return b


def runnable():
    xs = np.linspace(-30, 60, 100)
    x = xs[0]
    points_x = [x]  # 歷史資料
    v = 0  # 一開始在左上角, 動量為 0
    mu = 0.9  # 將動量縮小, 模擬摩擦力, mu愈大, 摩擦力愈小
    for i in range(epoch):
        ax.clear()
        ax.set_xlim(-35, 65)
        ax.set_ylim(-2, 3)
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
        dx = df(x)
        v = -dx * lr + mu * v
        x = x + v
        # x = x - df(x) * lr
        points_x.append(x)
        plt.draw()
        time.sleep(0.03)


shrink_y = 1e6
plt.figure(figsize=(10, 6))
epoch = 60
# lr 過大會越過鞍點, 太小則連鞍點都達不到
lr = 30
ax = plt.subplot()
t = threading.Thread(target=runnable)
t.start()
plt.show()
