#from 檔名 import 函數名
#from yhtLib import c2f
#from yhtLib import f2c
# 要引進100個全都要寫出來?
# from yhtLib import * 全部都import
#但有可能造成程式肥大, 速度緩慢
from yhtLib import *

# f=c2f(100)
# print(f)
# print(c2f(100))
# c=f2c(212)
# print(c)
#matplotlib為繪製圖表的套件
#pip install matplotlib : 於Terminal安裝套件matplotlib
#or file>settings>project: fcu_0726>interpreter
#click on plus icon>search for matplotlib>install
#as 別名, 把pylab 換成plt
import pylab as plt
r=100
x=[]
y=[]
for a in range(0,361):
    x1, y1=circle(r,a)
    x.append(x1)
    y.append(y1)
    print(x1,y1)

plt.figure(figsize=(6,6)) #設定圖形的長寬比
plt.xlim(-100,100) #限定x軸的範圍
plt.ylim(-100,100) #限定y軸的範圍
plt.plot([-100,100],[0,0]) #畫x軸
plt.plot([0,0],[-100,100]) #畫y軸
plt.plot(50,50,"go")
plt.plot([0,50],[0,50])
plt.plot([0,-1,-2,-3,-4,-5],[0,-1,-2,-3,-4,-5])
#有"ro":畫點, 沒有"ro":畫線
plt.plot(x,y) #繪製 r:red, o:圓點
plt.show()         #呈現
#資料視覺化

