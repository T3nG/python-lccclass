import random


class Node():
    def __init__(self):
        self.prev=None
        self.data=0
        self.next=None
random.seed(1)
datas=[random.randint(1,100) for i in range(10)]
# print(datas)

root=Node()
index=root

for i in datas:
    index.data=i
    index.next=Node()
    index.next.prev=index
    index=index.next


# 正向列印
index=root
while index.next is not None:
    print(f"{index.data} ",end="")
    index=index.next

print()

# 反向列印 (先將指標移到最後一位, 再反向列印)
# 不論指標在哪, 先把它移到最後一位
while index.next is not None:
    index=index.next
while index.prev is not None:
    print(f"{index.prev.data} ",end="")
    index=index.prev

'''
root, index, 皆為節點, 產生時都包含三個變數 prev, data, next

初始化
root=Node() 定義變數root 為類別Node(), 一個空的節點
index=root  定義變數index初始值等於root, 一個空的節點

index.data=datas  將檔案放入 index.data


'''