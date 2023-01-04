import numpy as np

from MyMBGD import MyMBGD


class MyAdam(MyMBGD):
    def __init__(self, a, b, x, y, lr, batct_size, beta1, beta2):
        super().__init__(a, b, x, y, lr, batct_size)
        self.beta1 = beta1
        self.beta2 = beta2
        self.e = 1e-6
        # 動量總和
        self.sum_ma = 0
        self.sum_mb = 0
        # 梯度平方和累加項
        self.sum_grad_a = 0
        self.sum_grad_b = 0

    def update(self):
        self.a_old = self.a
        self.b_old = self.b
        grad_a, grad_b = self.gradient()
        # 動量
        self.sum_ma = self.beta1 * self.sum_ma + (1 - self.beta1) * grad_a
        self.sum_mb = self.beta1 * self.sum_mb + (1 - self.beta1) * grad_b
        # 梯度平方和
        self.sum_grad_a = self.beta2 * self.sum_grad_a + (1 - self.beta2) * grad_a ** 2
        self.sum_grad_b = self.beta2 * self.sum_grad_b + (1 - self.beta2) * grad_b ** 2
        # 梯度更新(加總)
        self.a -= (self.lr * self.sum_ma) / (np.sqrt(self.sum_grad_a) + self.e)
        self.b -= (self.lr * self.sum_mb) / (np.sqrt(self.sum_grad_b) + self.e)
        self.loss = self.mse()
