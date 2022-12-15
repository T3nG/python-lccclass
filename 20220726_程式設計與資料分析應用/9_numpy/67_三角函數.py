import numpy as np
import pylab as plt

a=np.linspace(10,1,10)
# line 縣性 ; space 空間
# 等差級數 : linspace(a,b,c)
# 公差    : (b-c)/(c-1)
# 第一項  : a
print(a)

b=np.linspace(0,360,100)
r=100
x=r*np.cos(b*np.pi/180)
y=r*np.sin(b*np.pi/180)
print(x)
print(y)

plt.figure(figsize=(8,8)) # 長寬比
plt.xlim([-100,100])      # x軸限制
plt.ylim([-100,100])      # y軸限制
plt.scatter(x,y, c="yellow")
plt.plot(x,y, c="green")
plt.show()