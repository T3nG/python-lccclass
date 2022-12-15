import numpy as np
# numpy.dot() 相乘, 支援不同數值型態, 比如陣列相乘
a = 10
b = 20
print(np.dot(a, b))

c = [1, 2, 3]
d = [4, 5, 6]
print(np.dot(c, d))
# 1*4 + 2*5 + 3*6 = 32

e = np.array([1, 2, 3])
f = np.array([4, 5, 6])
print(e.dot(f))

g = e * f  # [4, 10, 18]
print(g.sum())

# 二維陣列時, 矩陣相乘
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,2],[3,4],[5,6]])
print(x.dot(y))
print(np.matmul(x, y))
'''
1 2 3   1 2 
4 5 6   3 4
        5 6
1*1+ 2*3+ 3*5 =22   1*2+ 2*4+ 3*6 =28
4*1+ 5*3+ 6*5 =49   4*2+ 5*4+ 6*6 =64
'''
