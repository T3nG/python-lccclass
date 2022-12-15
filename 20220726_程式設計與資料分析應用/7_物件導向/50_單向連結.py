# Single Link 單向連結
# 大二資料結構必考題
# planets=['mercury', 'venus']
# planets.append('earth')
# list : 本身可以更改長度, 一直到記憶體爆掉為止
import random

class Node(): # node 節點
    def __init__(self):
        self.data=0
        self.next=None
random.seed(10) # 種下種子
datas=[random.randint(1,100) for i in range(10)]
# import numpy as np
# d=np.random.randint(1,100,10) 一樣的
print(datas)
root=Node()
index=root            # index 初始值等同 root
for d in datas:
    index.data=d      # 第一個值放入 index.data
    index.next=Node() # 產生新的空節點到 index.next
    index=index.next  # index.next 的值放入 index (更新)
# 遍訪
index=root # 索引拉到最前面
while index.next is not None:
    print(f"{index.data} ,",end="")
    index=index.next # 往下移的意思

# index.data=d[1]   # 第二個值放入 index.data
# index.next=Node() # 產生新的空節點到 index.next
# index=index.next  # index.next 的值放入 index (更新)
#
# index.data=d[2]
# index.next=Node()
# index=index.next
#
# index.data=d[3]
# index.next=Node()
# index=index.next