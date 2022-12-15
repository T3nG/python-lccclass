import pylab as plt
import numpy as np

for i in range(3):
    #ax = plt.subplot(1, 3, i+1)
    x = np.linspace(1, 12, 12)
    y = np.random.randint(1, 30, 12)
    #ax.bar(x, y)
    plt.bar(x, y)
# 合一起顯示, 疊加起來, 或子繪圖區分三個

plt.show()