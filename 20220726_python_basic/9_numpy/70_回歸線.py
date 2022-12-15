# regression
import numpy as np
import pylab as plt

plt.figure(figsize=(6,4))
plt.xlim(20,42)
plt.ylim(50,320)
n=30
x=np.linspace(22,40,n)
# 0<=rng<1
# 0*2 -1 >=rng< 1*2 -1
# -1 <= 2rng-1 < 1

noise=(np.random.random(n)*2-1)*40
# 讓資料呈現更真實, 加入一些亂數打亂形狀
y=(-10)*x+500+noise

plt.scatter(x,y)

# polyfit(x,y,n)
# n 階方程式
# 回歸線的寫法, polyfit用 C 語言的演算法去計算
# args=np.polyfit(x,y,6)
# print(args)
# a=args[0]
# b=args[1]
# c=args[2]
# d=args[3]
# r=a*x**3+b*x**2+c*x+d
# 以 poly1d()直接產生回歸線函數
# f=np.poly1d(args) # 藉由參數, 產生函數
# 由f(x)產生y軸座標

# 精簡版的回歸線程式碼
f=np.poly1d(np.polyfit(x,y,6))
plt.plot(x,f(x),c="g")

plt.show()
