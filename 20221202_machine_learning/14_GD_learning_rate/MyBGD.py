import numpy as np


class MyBGD():
    def __init__(self, a, b, x, y, lr):
        self.a = a
        self.b = b
        self.x = x  # 代入的x, y為集合
        self.y = y
        self.lr = lr
        self.a_old = a  # 歷史資料
        self.b_old = b
        self.loss = None  # 損失函數

    def mse(self):
        loss = ((self.a * self.x + self.b) - self.y) ** 2
        return np.mean(loss)

    # 梯度下降, 偏微分
    def gradient(self):
        grad_a = 2 * np.mean((self.a * self.x + self.b - self.y) * self.x)
        grad_b = 2 * np.mean(self.a * self.x + self.b - self.y)
        return grad_a, grad_b

    def update(self):
        grad_a, grad_b = self.gradient()
        self.a_old = self.a
        self.b_old = self.b
        self.a = self.a - self.lr * grad_a  # 逼近法
        self.b = self.b - self.lr * grad_b
        self.loss = self.mse()
