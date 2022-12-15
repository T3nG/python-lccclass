import random

class Node(): # node 節點
    def __init__(self):
        self.data=0
        self.next=None
random.seed(10) # 種下種子
datas=[random.randint(1,100) for i in range(10)]

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
    index=index.next  # 往下移的意思

# 0. 以上即是 list 的資料結構
# 1. 別人做出來的, 不表示自己做得出來
# 2. 站在巨人的肩膀上, 死得更快
