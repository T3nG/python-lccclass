# SGD: Stochastic Gradient Descent 隨機梯度下降
# 就是把 BGD的總和拿掉, 只隨機計算其中一個點

import time
import threading
import pylab as plt
from Regression import get_data, get_loss
from MySGD import MySGD


def runnable():
    for i in range(epoch):
        gd.update()
        a = gd.a
        b = gd.b
        loss = gd.loss
        ax[0].clear()
        ax[0].set_xlim(-5, 5)
        ax[0].set_ylim(-30, 30)
        ax[0].scatter(x, y)
        ax[0].plot([x[0], x[-1]], [a*x[0]+b, a*x[-1]+b], c='orange')
        ax[0].set_title(f'{a:.6f}x+{b:.6f}')
        ax[1].set_xlim(-10, 15)
        ax[1].set_ylim(-10, 15)
        ax[1].scatter(a, b, c='g')
        ax[1].plot([gd.a_old, a], [gd.b_old, b], c='r')
        ax[1].set_title(f'iter:{i + 1:03d}, loss={loss:.6f}')
        plt.draw()
        time.sleep(0.03)


n = 50
epoch = 100
a = -9
b = -9
lr = 0.01  # 與 BGD的不同之處
x, y = get_data(n)
mesh, loss = get_loss(x, y)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
a2 = ax[1].contourf(mesh[0], mesh[1], loss, 15, cmap=plt.cm.Purples)  # contour 框線, contourf 填滿
plt.colorbar(a2, ax=ax[1])
gd = MySGD(a, b, x, y, lr)
t = threading.Thread(target=runnable)
t.start()
plt.show()
