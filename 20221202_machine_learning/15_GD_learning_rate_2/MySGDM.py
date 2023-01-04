from MyMBGD import MyMBGD


class MySGDM(MyMBGD):
    def __init__(self, a, b, x, y, lr, batch_size, gamma):
        # gamma 就是摩擦力, <1
        super().__init__(a, b, x, y, lr, batch_size)
        self.gamma = gamma
        self.ma = 0
        self.mb = 0

    def update(self):
        grad_a, grad_b = self.gradient()
        self.a_old = self.a
        self.b_old = self.b
        self.ma = self.gamma * self.ma + self.lr * grad_a
        self.mb = self.gamma * self.mb + self.lr * grad_b
        self.a -= self.ma
        self.b -= self.mb
        self.loss = self.mse()
