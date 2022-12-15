import numpy as np
import pylab as plt
from scipy.interpolate import interp1d
t=np.linspace(0,10,10)
noise=(np.random.random(10)*2-1) *0.1 # 產生介於 -0.1 ~ 0.1之間的亂數
y=np.sin(2*np.pi*t)+noise
# plt.scatter(t,y) # 畫點散圖
#plt.plot(t,y) # 畫直線
plt.plot(t,y,'go') # 畫點散圖, r : 顏色, o : 圓形, s : 四方型, ^ : 三角形, ...

x=np.linspace(0,10,50)
# 底下為一元一次方程式
#f=interp1d(t,y) # 依 t,y產生內插值的函數

# 底下為一元三次方程式
f=interp1d(t,y,kind='cubic')

plt.plot(x,f(x),'ro')
plt.plot(x,f(x),c='yellow')

plt.show()