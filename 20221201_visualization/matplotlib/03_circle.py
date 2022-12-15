import pylab as plt
import numpy as np

n = 360
radius = 100

angle = np.linspace(0, 360, n)  # 0~360 分成 10 等分

x = radius * np.cos(np.pi * angle/180)  # 角度轉徑度, 帶入三角函數
y = radius * np.sin(np.pi * angle/180)

plt.figure(figsize=(6, 6))
plt.plot(x ,y)
plt.show()