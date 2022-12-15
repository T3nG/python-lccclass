'''
很重要, 但不好記, 不好懂, 不好應用, 老師教得好無聊
list       : a=[1,2,3,4,5] , a.append(10)
tuple      : b=(1,2,3,4,5) , 不可變更
dictionary : c={"key":"valuse","key":"valuse"}
set        : d=set([1,2,3,4,5])
'''
#import : 輸入第三方套件
#Python 開發者  : 第一方
#使用者         : 第二方
#其他人開發的工具: 第三方
#Anaconda : 安裝時, python, ide一併安裝,
#裝大量的第三方套件, 肥大而慢, 愚民
import random
import time

a=[]
#timp stamp 時間截記 : 1970/01/01 ~ 現在所經過的秒數
t1=time.time()
#print((2022-1970)*365*86400)
#print(t1)
#此法使用 Python 的迴圈
for i in range(1,100_001):
    a.append(i)
#print(a)
t2=time.time()
print(f"總花費{(t2-t1)*1000}ms")

#第二種寫法
t1=time.time()
b=[i for i in range(1,100_001)] #此法會使用 C語言的迴圈
t2=time.time()
print(f"總花費{(t2-t1)*1000}ms")
#程式碼跑更快了, 建議以這種寫法寫迴圈

t1=time.time()
c=[]
for i in range(1000):
    c.append(random.randint(1,1000))
print(c)
t2=time.time()
print(f"總花費{(t2-t1)*1000}ms")

t1=time.time()
d=[random.randint(1,1000) for i in range(1000)]
print(d)
t2=time.time()
print(f"總花費{(t2-t1)*1000}ms")

#字典
m={"mercury":"水星","venus":"金星"}
#常看到的第二種寫法
n=dict(mercury="水星",
       venus="金星",
       earth="地球"
       )
print(n)

#切片, 子字串, 每一種語言都很常運用這個切片的功能
#重要, 但不好懂
#s[啟始位置:結束位置(但不包含此位置):步進值]
#  0123456789
s="abcdefghijklm"
#       -2:l  -1:m
print(s[3:7]) #3~6
print(s[:])   #從頭抓到尾, 啟示位置沒寫代表0
print(s)      #為什麼不直接print(s)呢?
print(s[::2]) #從頭抓到尾, 每隔2位抓一次
print(s[:-1]) #-1從後面算來
#為什麼要用-1? 比如有以下用法
file="tiger.jpg"
print(file[:-4]) #去除副檔名
print(s[::-1])   #把整個字串反向選取
print(s[13::-1]) #上式為此式之精簡版
#什麼時候會用到反向選取? 比如排序的時候

x=["mercury","venus","earth","mars"]
print(x[::-1])
print(x[:3])