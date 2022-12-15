# http://mahaljsp.asuscomm.com/index.php/2021/01/13/tensorflow%e8%bf%b4%e6%ad%b8%e7%b7%9a/
import threading
import time

import numpy as np
import pylab as plt

# 損失函數: 計算迴歸線的


def run():
    a = 0
    b = 0
    epoch = 300
    # learning_rate 有一定的規範, 太大, 一次進太多, 無法繼續, 太小, 進太少, 所耗時間與次數要拉大
    # 有另外的演算法可以算
    learning_rate = 2.5e-3  # 2.5*10^(-3)
    for i in range(epoch):
        ax.clear()
        ax.plot([0, 0], [-10, 10], c='b')
        ax.plot([-15, 15], [0, 0], c='b')
        ax.set_xlim(-15, 15)
        ax.set_ylim(-10, 10)
        ax.scatter(x, y)
        f = np.poly1d(np.polyfit(x, y, 1))
        reg = f(x)
        plt.plot(x, reg, linewidth=5, color='g')

        y_pred = a * x + b
        # 對a及b的偏微分
        da = (y_pred-y).dot(x)
        db = (y_pred-y).sum()
        a = a - learning_rate * da
        b = b - learning_rate * db

        ax.plot(x, a*x+b, color='red', linewidth=1)
        # 更新渲染, 須給他時間畫圖, 不然會出錯
        plt.draw()
        time.sleep(0.05)


n= 20
np.random.seed(1)
x = np.linspace(-10, 10, n)
# y=ax+b -亂數偏移量, 讓這條線上下比較不規則, 否則就只是一條直線而已
y = 0.5 * x + 3 - np.random.randint(-5, 5, n)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot()

# 叫新執行緒來執行
t = threading.Thread(target=run)
t.start()

plt.show()

# numpy 畫迴歸線
# np.polyfit(x, y, 1) => (a, b) => y=ax+b
# np.polyfit(x, y, 2) => (a, b, c) => y=ax^2+bx+c
# f = np.poly1d(a, b, c...) => f = ax^2 + bx + c
# f = np.poly1d(np.polyfit(x, y, 1))
# reg = f(x)
# plt.plot(x, reg, linewidth=3, color='orange')

# # y=ax+b 迴歸線說明
# x = np.array([0, 1, 2, 3, 4, 5, 6])
# #  2 為斜率, dy/dx, 5 為偏移量bias, 當x=0, y=偏移量
# y = 2 * x + 5
# plt.figure(figsize=(6, 6))
# plt.xlim(0, 20)
# plt.ylim(0, 20)
# plt.plot(x, y)
# plt.show()
