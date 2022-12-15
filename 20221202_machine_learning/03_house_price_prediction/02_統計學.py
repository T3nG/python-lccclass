import numpy as np
import pylab as plt
np.random.seed(1)
batch = 100
a = np.random.randint(1, 100, batch)
print('a:', a)
b = np.sort(a)
print('b:', b)

# 中位數: 中間那個數, 若總數目為偶數, 則為中間二數的平均
print(f'中位數: {np.median(b)}')

# 平均數: 總和/總數
print(f'平均數: {np.mean(b)}')
# 當點數愈多時, 愈往二極端的中間值靠攏
# x = np.linspace(1, batch, batch)
# plt.scatter(x, a, s=0.5)
# plt.plot([0, batch], [b.mean(), b.mean()])
# plt.show()

# 標準差: sqrt(E(xi-mean)^2/n), standard deviation
sd = np.std(b)
print(f'標準差: {sd}')
# 或是利用以下方法
x = np.sqrt(np.sum(np.square(a-a.mean()))/a.shape)
print(f'標準差: {x[0]}')

xn = np.linspace(1, batch, batch)
plt.scatter(xn, a, s=0.5)
plt.plot([0, batch], [b.mean(), b.mean()])
plt.plot([0, batch], [sd, sd])
plt.show()
