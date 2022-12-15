import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

# 格式為二維陣列
c = np.c_[a, b]
print(c)

# 結合為tuple
d = zip(a,b)
print(list(d))
