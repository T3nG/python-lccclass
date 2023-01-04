import numpy as np

from MyMBGD import MyMBGD

class AdaGrad(MyMBGD):
    def __init__(self, a, b, x, y, lr, batch_size):
        super().__init__(a, b, x, y, lr, batch_size)
        self.sum_grad_a = 0
        self.sum_grad_b = 0
        self.e = 1e-6  # epsilon

    def update(self):
        self.a_old = self.a
        self.b_old = self.b
        grad_a, grad_b = self.gradient()
        self.sum_grad_a += grad_a ** 2
        self.sum_grad_b += grad_b ** 2
        self.a = self.a_old - (self.lr / (np.sqrt(self.sum_grad_a) + self.e)) * grad_a
        self.b = self.b_old - (self.lr / (np.sqrt(self.sum_grad_b) + self.e)) * grad_b
        self.loss = self.mse()
