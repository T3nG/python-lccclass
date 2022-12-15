import numpy as np
import pylab as plt

plt.figure(figsize=(6,6))
plt.xlim([-100,100])
plt.ylim([-100,100])

a=np.linspace(-100,100,11)
s=((len(a))*(len(a)),2)
b=np.zeros(s)
for i in range(len(a)*len(a)):
    for j in range(len(a)*len(a)):
        b[j][1] = a[j % 11]
    b[i][0] = a[i // 11]

plt.plot([-100,100],[a,a],c="#87cefa",linewidth=0.5) # x軸平行
plt.plot([a,a],[-100,100],c="#87cefa",linewidth=0.5) # y軸平行

plt.scatter(b[:,0],b[:,1],c="r",s=50)

# 兩點間畫線 plt.plot([x1,x2],[y1,y2])
plt.plot([-100,100],[0,0],c="g") # x軸
plt.plot([0,0],[-100,100],c="g") # y軸

x=[1,50]
y=[1,60]

plt.plot(x,y)
#plt.savefig("test007.jpg") # 將圖表存成檔案
plt.show()
'''
老師的寫法

n=20
#繪製水平線
for y in range(-100,100,n):
    plt.plot([-100,100],[y, y], c='#00bbff', linewidth=0.5)

#繪製垂直線
for x in range(-100,101,n):
    plt.plot([x,x],[-100,100], c='#00bbff', linewidth=0.5)

#繪製圓點
for x in range(-100,101,n):
    for y in range(-100,101, n):
        plt.scatter(x,y, c='red')
'''
