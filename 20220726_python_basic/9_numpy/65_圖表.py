# pip install matplotlib
import numpy as np
# import matplotlib.pyplot as plt
import pylab as plt
#plt.legend() # 圖例

rng=np.random.RandomState(1)
# random seed

x=rng.randint(1,100,10)
y=rng.randint(1,100,10)
print(x)
print(y)

plt.scatter(x, y, c="g", s=300)
# 點散圖
# c : color , s : size

plt.show()