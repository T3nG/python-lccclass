import numpy as np
from MyBGD import MyBGD


class MyMBGD(MyBGD):
    def __init__(self, a, b, x, y, lr, batch_size):
        super().__init__(a, b, x, y, lr)
        self.batch_size = batch_size
        # 使更亂
        self.refresh()
        self.update_batch()

    def update_batch(self):
        idx = self.shuffle[self.idx:self.idx+self.batch_size]
        self.idx += self.batch_size
        self.x_batch = self.x[idx]
        self.y_batch = self.y[idx]

    def gradient(self):
        grad_a = 2 * np.mean((self.a * self.x_batch + self.b - self.y_batch) * self.x_batch)
        grad_b = 2 * np.mean(self.a * self.x_batch + self.b - self.y_batch)
        # 提取完所有資料後, 將資料再重新打散, 重新提取, 避免loss 為nan
        if self.idx > len(self.x):
            self.refresh()
        self.update_batch()
        return grad_a, grad_b

    def refresh(self):
        self.shuffle = np.random.permutation(len(self.x))
        self.idx = 0
