# http://mahaljsp.asuscomm.com/index.php/2022/10/05/lof/
# pip install scikit-learn seaborn
import seaborn as sns
import numpy as np
import pylab as plt
from sklearn.neighbors import LocalOutlierFactor as LOF
np.random.seed(1)
# 100組, 2行的標準常態分布
inliers = np.random.randn(100, 2)

# 秀出常態分佈圖
# ax1 = plt.subplot(1, 2, 1)
# ax1.set_xlim(-5, 5)
# ax1.set_ylim(0, 30)
# sns.histplot(inliers[:, 0], kde=True)
# ax2 = plt.subplot(1, 2, 2)
# ax2.set_xlim(-5, 5)
# ax2.set_ylim(0, 30)
# sns.histplot(inliers[:, 1], kde=True)

# 利用+3, -3將兩組在同一畫布上可以區分開來
inliers = np.r_[inliers+3, inliers-3]
# print(inliers)
# x = inliers[:, 0]
# y = inliers[:, 1]
# plt.scatter(x, y, s=5, c='k')

# 加入離群點的值
outliers = np.random.uniform(low=-6, high=6, size=(20, 2))
data = np.r_[inliers, outliers]
x = data[:,0]
y = data[:,1]
plt.scatter(x, y, s=5, c='k')

# 以 LOF函數偵測離群值
lof = LOF(n_neighbors=20, contamination=0.1)
# y_pred 由一群 1 與 -1 組成的集合, 1: 未離群, -1: 離群
# scores 計算每一個點的分數值, 負值愈大, 代表離群的機會愈大
y_pred = lof.fit_predict(data)
scores = lof.negative_outlier_factor_
print(y_pred)
print(scores)

# 使用 0代表沒離群, 2代表有離群
radius = np.ones(len(y_pred))
radius -= y_pred
radius /= 20
# 沒離群的 s=1000*0, 大小等於0, 於是沒有畫出來, 有離群的, 就覆蓋上去, facecolor="none" 變成把離群的點框起來
plt.scatter(x, y, s=1000*radius, edgecolors='r', facecolor="none")

plt.show()
