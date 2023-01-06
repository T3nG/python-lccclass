import threading
import time

from matplotlib import animation

from AdaGrad import AdaGrad
from MyAdam import MyAdam
from MyBGD import MyBGD
from MyMBGD import MyMBGD
from RMSP import RMSP
from Regression import *
import pylab as plt

from MySGD import MySGD
from MySGDM import MySGDM


def runnable(data):
    global i
    gd.update()
    if not np.isnan(gd.loss) and i <epoch:
        i+=1
        a=gd.a
        b=gd.b
        loss=gd.loss
        ax[0].clear()
        ax[0].set_xlim(-5,5)
        ax[0].set_ylim(-30, 30)
        ax[0].scatter(x, y)
        ax[0].plot([x[0], x[-1]],[a*x[0]+b, a*x[-1]+b], c="orange")
        ax[0].set_title(f'{a:.6f}x+{b:.6f}')

        print('iter=' + str(i) + ', loss=' + '{:.2f}'.format(gd.loss))
        ax[1].set_xlim(-10, 15)
        ax[1].set_ylim(-10, 15)
        ax[1].set_title(f'iter:{i:03d} Loss: {loss:6f}')
        ax[1].plot([gd.a_old, a], [gd.b_old, b], c='r')
        ax[1].scatter(a, b, c='g')
        ax[1].set_xlabel("a")
        ax[1].set_ylabel("b")


i=0
x,y=get_data(100)
mesh, loss=get_loss(x,y)
fig, ax=plt.subplots(nrows=1, ncols=2, figsize=(12,4))

a2=ax[1].contourf(mesh[0], mesh[1], loss,15, cmap=plt.cm.Purples)
plt.colorbar(a2,ax=ax[1])


a = -9
b = -9
ax[1].scatter(a, b, c='g')
batch_size=5
epoch=200
gamma=0.8
# Adam lr=2, batch_size=5
lr = 0.05
beta1=0.5
beta2=0.9
rho=0.9
# gd = MyAdam(a, b, x, y, lr, batch_size, beta1, beta2)
gd = MyMBGD(a, b, x, y, lr, batch_size)
ani=animation.FuncAnimation(fig, runnable, interval=100)
ani.save('grad_32.gif', fps=8)
plt.show()
