import random

import numpy as np

rng=np.random.RandomState(1)
a=rng.randint(1,100,10)
b=rng.randint(1,100,10)
c=a+b
print("陣列相加, 每一項相加")
print(a)
print(b)
print(c)
print("")

random.seed(1)
d=[random.randint(1,100) for i in range(10)]
e=[random.randint(1,100) for i in range(10)]
f=d+e
print("列表相加, 只是把數字串在後面")
print(d)
print(e)
print(f)