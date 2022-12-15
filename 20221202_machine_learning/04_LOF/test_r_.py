import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
c = np.r_[a, b]  # a 後面加上 b
print(c)
print(a+b)  # 變成相加了

x = [1,2,3,4,5]
y = [6,7,8,9,10]
z = x + y
print(z)

# append list: 變成二維的
x.append(y)
print(x)
