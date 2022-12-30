# BGD: Batch Gradient Descent, 批量梯度下降
# ref: http://mahaljsp.asuscomm.com/index.php/2022/12/23/optimizer/
import threading
import time

import pylab as plt

from MyBGD import MyBGD
from Regression import *


def runnable():
    for i in range(epoch):
        gd.update()
        a = gd.a
        b = gd.b
        loss = gd.loss
        # ax[0] 於左側點散圖繪製動畫迴歸線
        ax[0].clear()
        ax[0].set_xlim(-5, 5)
        ax[0].set_ylim(-30, 30)
        ax[0].scatter(x, y)
        ax[0].plot([x[0], x[-1]], [a*x[0]+b, a*x[-1]+b], c='orange')
        ax[0].set_title(f'{a:.6f}x+{b:.6f}')
        # ax[1] 於右側繪製 a,b的歷史資料
        ax[1].set_xlim(-10, 15)
        ax[1].set_ylim(-10, 15)
        ax[1].scatter(a, b, c='g')
        ax[1].plot([gd.a_old, a], [gd.b_old, b], c='r')
        ax[1].set_title(f'iter:{i + 1:03d}, loss={loss:.6f}')
        plt.draw()
        time.sleep(0.03)


n = 10000  # 設定幾筆資料, 資料量一多, 就要花更多時間找極值, 因此學習率與初始值的設定就很重要
x, y = get_data(n)
mesh, loss = get_loss(x, y)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
ax[0].scatter(x, y)
a2 = ax[1].contourf(mesh[0], mesh[1], loss, 15, cmap=plt.cm.Purples)
plt.colorbar(a2, ax=ax[1])
ax[1].set_xlabel('a')
ax[1].set_ylabel('b')


epoch = 50
lr = 0.0577  # 得手動調整, 愈快找到極值愈佳
a = -9  # 初始值
b = -9
# 馬上就找到
# a = 3
# b = 2
gd = MyBGD(a, b, x, y, lr)
t = threading.Thread(target=runnable)
t.start()
plt.show()
