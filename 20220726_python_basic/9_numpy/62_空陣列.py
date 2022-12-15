import numpy as np
a=np.array([1,2,3,4,5])
b=np.zeros([100])
# 創建一個100個位置的空陣列(預設值為0)

b[20]=5000
# 設定位置20的值為5000

print(b)

c=np.ones([20])
# 創建一個20個位置的空陣列(預設值為1)

print(c)

d=np.ones([10])*100
# 創建一個10個位置的空陣列(預設值為1*100)
# 使用c的迴圈一個一個改, 速度極快

print(d)

e=np.zeros([10])+5
# 創建一個10個位置的空陣列(預設值為0+5)

print(e)

# python迴圈很慢, 只能用迴圈一個一個改預設值
l=[1 for i in range(10)]
print(l)

for i in range(len(l)):
    l[i]=100
print(l)