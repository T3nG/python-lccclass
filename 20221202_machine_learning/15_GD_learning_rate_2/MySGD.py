# SGD是 BGD的改版, 只隨機選其中一點來計算
import numpy as np
from MyBGD import MyBGD

class MySGD(MyBGD):
    def __init__(self, a, b, x, y, lr):
        super().__init__(a, b, x, y, lr)

    # 覆寫, 函數名稱得一致, 傳統語言會在函數前加上 override
    def gradient(self):
        idx = np.random.randint(len(self.x))  # 0 ~ x-1 隨機取一個整數
        grad_a = 2 * (self.a * self.x[idx] + self.b - self.y[idx]) * self.x[idx]
        grad_b = 2 * (self.a * self.x[idx] + self.b - self.y[idx])
        return grad_a, grad_b

