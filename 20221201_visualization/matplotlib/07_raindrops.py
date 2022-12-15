import pylab as plt
import numpy as np
from matplotlib import animation

fig, ax = plt.subplots()
x = np.random.randint(1, 50, 50)
y = np.random.randint(40, 50, 50)


def run(data):
    for i in range(len(y)):
        if y[i] > 0:
            y[i] -= 1
    ax.clear()
    # ax.axis("off")
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    ax.scatter(x, y, s=80, c=x+y)


# 雖然沒有指定 frames參數, 但是run()一樣要指定參數去接收
ani = animation.FuncAnimation(fig, run, interval=100)
plt.show()
