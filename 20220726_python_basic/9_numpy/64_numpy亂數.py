import random
import numpy as np

# 產生 10 個 0~1 之間的亂數(0<x<1), 格式為陣列
a=np.random.random(10)
print(a)

# python 迴圈, 效能極差
# import random
# b=[random.random() for i in range(10)]


# 產生 10 個 1~(10-1) 之間的整數亂數
c=np.random.randint(1,10,10)
print(c)

# 產生 10 個 1~10 之間的整數亂數
d=[random.randint(1,10) for i in range(10)]
print(d)