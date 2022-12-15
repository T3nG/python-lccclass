from ChrisLib import *
import pylab as plt
# a=math.sin(deg2rad(45))
# print(a)


plt.figure(figsize=(8,8)) #設定圖形的長寬比
plt.xlim(-100,100) #限定x軸的範圍
plt.ylim(-100,100) #限定y軸的範圍
plt.plot([-100,100],[0,0]) #畫x軸, x範圍[-100,100], y範圍[0,0]
plt.plot([0,0],[-100,100]) #畫y軸

r=100
x=[]
y=[]
xx=[]
yy=[]
for a1 in [30,45,60,90,120,135,150,180,210,225,240,270,300,330,315,330,360]:
    x1,y1=circle(r,a1)
    x.append(x1)
    y.append(y1)
    plt.plot([0,x1],[0,y1])
    print(x1,y1)
plt.plot(x,y,"go")

for a2 in range(0,361):
    x2,y2=circle(r,a2)
    xx.append(x2)
    yy.append(y2)
plt.plot(xx,yy)
plt.show()

