# pip install scipy matplotlib
import numpy as np
import pylab as plt
from scipy.stats import kde

# 常態分布 multivariable_model(平均值, 斜方差, 大小)
# [[1, 0.5]  (1-mean+0.5-mean)^0.5
#  [0.5 ,3]] (0.5-mean+3-mean)^0.5

# 產生200個點, 兩列, 兩百組
data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 3]], 200)
x, y = data.T  # 轉向
fig, ax = plt.subplots(ncols=3, nrows=2, figsize=(10, 10))
ax[0][0].set_title('Scatter')
ax[0][0].plot(x, y, 'ko')

# 六邊形
nbins = 20  # 鄰近點數
ax[0][1].set_title('Hexbin')
ax[0][1].hexbin(x, y, gridsize=nbins, cmap=plt.cm.BuGn_r)

# 直方形
ax[0][2].set_title('hist')
ax[0][2].hist2d(x, y, bins=nbins, cmap=plt.cm.BuGn_r)

# 高斯kde
k = kde.gaussian_kde(data.T)
xi, yi = np.mgrid[x.min():x.max():nbins * 1j, y.min():y.max():nbins * 1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))
# print(zi)
# 密度圖
ax[1][0].set_title('Gaussian KDE')
ax[1][0].pcolormesh(xi, yi, zi.reshape(xi.shape), shading='auto', cmap=plt.cm.BuGn_r)

# 新增陰影
ax[1][1].set_title('GShading')
ax[1][1].pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.cm.BuGn_r)

# 輪廓
ax[1][2].set_title('Contour')
ax[1][2].pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.cm.BuGn_r)
ax[1][2].contour(xi, yi, zi.reshape(xi.shape))

plt.savefig('density.jpg')
plt.show()
