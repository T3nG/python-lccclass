import numpy as np
import pylab as plt
# 正弦波公式 y=A*sin(k*pi*t)
# A為振幅, t為總時間, k為在t時間內會出現的波峰數, 必須是偶數
n=1000
A=20
k=10
x=np.linspace(0,n,n)
y=A*np.sin(k*np.pi*x)
plt.plot(x,y)
plt.show()