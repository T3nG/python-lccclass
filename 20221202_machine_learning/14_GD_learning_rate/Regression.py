import numpy as np

np.random.seed(1)


def get_data(n):
    x = np.arange(-5, 5.1, 10 / n)  # arange(起始值, 結束值(不含), 步進值
    y = 3 * x + 2 + (np.random.rand(len(x)) - 0.5) * 20
    return x, y


# 迴歸線損失函數
def get_loss(xs, ys):
    a = np.arange(-10, 16, 1)
    b = np.arange(-10, 16, 1)
    mesh = np.meshgrid(a, b)
    loss = 0
    for x, y in zip(xs, ys):
        loss += (mesh[0] * x + mesh[1] - y) ** 2
    loss /= len(xs)
    return mesh, loss
