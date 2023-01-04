# 自適應梯度策略 - 可以自動調整學習率, 且可以避開鞍點
# 還是需手動給予學習率初值
# Adagrad Adaptive Gradient Descent
# 公式: x_{t+1}=x_{t}(1-\frac{-r}{\sqrt{G_{t^2}+\varepsilon }}) = x_{t}(1-\frac{-r}{\sqrt{\sum_{t=1}^{n}(\bigtriangledown f(x)_{t})^2}+\varepsilon})
# https://latex.codecogs.com/eqneditor/editor.php
# epsilon 是為了讓分母不為零, 通常是一個極小的數, 比如1e-6
# RMSProp Root Mean Square Propagation 均方根傳播法

import time
import threading
import pylab as plt
import numpy as np
from Regression import get_data, get_loss
from AdaGrad import AdaGrad


def runnable():
    for i in range(epoch):
        gd.update()
        # 如果 loss為 nan, 表示批次取樣已經取完, 需重新打亂再重頭取樣
        if np.isnan(gd.loss):
            break
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


# lr愈大, 速度愈快
n = 50
epoch = 40
a = -9
b = -9
lr = 5
batch_size = 5
x, y = get_data(n)
mesh, loss = get_loss(x, y)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
a2 = ax[1].contourf(mesh[0], mesh[1], loss, 15, cmap=plt.cm.Purples)  # contour 框線, contourf 填滿
plt.colorbar(a2, ax=ax[1])
gd = AdaGrad(a, b, x, y, lr, batch_size)
t = threading.Thread(target=runnable)
t.start()
plt.show()
