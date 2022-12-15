import numpy as np
np.random.seed(0) # random seed, 偽亂數
a=np.random.randint(0,100,10)
print(a)

# rng=np.random.RandomState(0) # random seed, 偽亂數
# b=rng.randint(0,100,10)
# print(b)

# 以上兩種寫法都一樣, 擇一即可

# 使產生的亂數可以排列
# 第一種 List
b=sorted(a) # 傳回list
print(b)

# 第二種
c=np.sort(a) # 傳回array
print(c)

# 演算法, 很難懂, 論文級, 比如接下來要說的氣泡排序法

