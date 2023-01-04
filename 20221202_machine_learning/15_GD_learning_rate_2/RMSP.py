import numpy as np

from AdaGrad import AdaGrad


class RMSP(AdaGrad):
    def __init__(self, a, b, x, y, lr, batch_size, rho):
        super().__init__(a, b, x, y, lr, batch_size)
        self.rho = rho

    def update(self):
        self.a_old = self.a
        self.b_old = self.b
        grad_a, grad_b = self.gradient()
        self.sum_grad_a = self.rho * self.sum_grad_a + (1 - self.rho) * grad_a ** 2
        self.sum_grad_b = self.rho * self.sum_grad_b + (1 - self.rho) * grad_b ** 2
        # 梯度更新
        self.a = self.a_old - (self.lr / (np.sqrt(self.sum_grad_a) + self.e)) * grad_a
        self.b = self.b_old - (self.lr / (np.sqrt(self.sum_grad_b) + self.e)) * grad_b
        self.loss = self.mse()
