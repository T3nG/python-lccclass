# 二元樹排序法規則
# 左邊小, 右邊大
# 左中右, 中間取值
# 一個節點可以產生兩個節點, 第一個節點/值為根, 節點之間互相比較, 第二個值與根相比,
# 往下一層, 比較小就放左邊, 比較大就放右邊
# 但三個值無法放入第一層, 放入第二層, 放哪邊呢? 比根小放左邊, 比根大放右邊, 若已經有節點了,
# 就往下一層, 比那個節點小放左邊, 比他大放右邊
# 第0層 2^0=1
# 第1層 2^1=2
# 第2層 2^2=4
# 比如若有42億筆資料要排序, 只需要排32次 (2^32)

# 已經經過排序的資料, 禁止使用二元樹排序法, 效能會非常差
# 資料愈亂, 速度愈快
# 所以資料庫都是流水帳, 不能經過排序, 要用的時候再以二元樹來排序使用
import time

import numpy as np

class Node():
    def __init__(self, d):
        self.data=d
        self.left=None
        self.right=None

def bs(node):
    if node.left is not None:
        bs(node.left)
    sort_datas.append(node.data)
    if node.right is not None:
        bs(node.right)

def buildTree(node,d):
    if node is None:
        node=Node(d)
    elif d<node.data:
        node.left=buildTree(node.left,d)
    else:
        node.right=buildTree(node.right,d)
    return node

np.random.seed(0)
n=10
datas=np.random.randint(0,10000,n)
print(datas)

root=None
for d in datas:
    root=buildTree(root,d)
sort_datas=[]
test=[]
# t1=time.time()
bs(root)
# t2=time.time()
print(sort_datas)
#print(f"總花費{t2-t1}秒")

'''
datas[0]=2732
root=buildTree(None,2732)
    =buildTree(Node(2732),2732)
    =return node
    =Node(2732)
================================================
Node(2732) data=2732 left=None right=None
================================================
datas[1]=9845
root=buildTree(rood=Node(2732),d=9845)
root=buildTree(Node(2732),9845)
    Node(2732).right=buildTree(Node(2732).right,9845)
                    =buildTree(None,9845)
                    =buildTree(Node(9845),9845)
                    =Node(9845)   
    =return node
    =Node(2732)
================================================
Node(2732) data=2732 right=Node(9845) left=None
Node(9845) data=9845 right=None       left=None
================================================
datas[2]=3264
root=buildTree(root=Node(2732),d=3264)
root=buildTree(Node(2732),3264)
    Node(2732).right=buildTree(Node(2732).right,3264)
                    =buildTree(Node(9845),3264)
                    Node(9845).left=buildTree(Node(9845).left,3264)
                                   =buildTree(None,3264)
                                   =buildTree(Node(3264),3264)
                                   =Node(3264)
                    =return node
                    =Node(9845)
    =return node
    =Node(2732)
================================================
Node(2732) data=2732 right=Node(9845) left=None
Node(9845) data=9845 right=None       left=Node(3264)
Node(3264) data=3264 right=None       left=None
================================================
datas[3]=4859
root=buildTree(root=Node(2732),d=4859)
    =buildTree(Node(2732),4859)
    Node(2732).right=buildTree(Node(2732).right,4859)
                    =buildTree(Node(9845),4859)
                    Node(9845).left=buildTree(Node(9845).left,4859)
                                   =buildTree(Node(3264),4859)
                                   Node(3264).right=buildTree(Node(3264).right,4859)
                                                   =buildTree(None,4859)
                                                   =buildTree(Node(4859),4859)
                                                   =return node
                                                   =Node(4859)
                                   =return node
                                   =Node(3264)
                    =return node
                    =Node(9845)
    =return node
    =Node(2732)
================================================
Node(2732) data=2732 right=Node(9845) left=None
Node(9845) data=9845 right=None       left=Node(3264)
Node(3264) data=3264 right=Node(4859) left=None
Node(4859) data=4859 right=None       left=None
================================================                     
datas[4]=9225
root=buildTree(root=Node(2732),d=9225)
    =buildTree(Node(2732),9225)
    Node(2732).right=buildTree(Node(2732).right,9225)
                    =buildTree(Node(9845),9225)
                    Node(9845).left=buildTree(Node(9845).left,9225)
                                   =buildTree(Node(3264),9225)
                                   Node(3264).right=buildTree(Node(3264).right,9225)
                                                   =buildTree(Node(4859),9225)
                                                   Node(4859).right=buildTree(Node(4859).right,9225)
                                                                   =buildTree(None,9225)
                                                                   =buildTree(Node(9225),9225)
                                                                   =return node
                                                                   =Node(9225)
                                                   =return node
                                                   =Node(4859)
                                   =return node
                                   =Node(3264)
                    =return node
                    =Node(9845)
    =return node
    =Node(2732)
================================================
Node(2732) data=2732 right=Node(9845) left=None
Node(9845) data=9845 right=None       left=Node(3264)
Node(3264) data=3264 right=Node(4859) left=None
Node(4859) data=4859 right=Node(9225) left=None
Node(9225) data=9225 right=None       left=None
================================================                  
datas[5]=7891
root=buildTree(Node(2732),7891)
    Node(2732).right=buildTree(Node(2732).right,7891)
                    =buildTree(Node(9845),7891)
                    Node(9845).left=buildTree(Node(9845).left,7891)
                                   =buildTree(Node(3264),7891
                                   Node(3264).right=buildTree(Node(3264).right,7891)
                                                   =buildTree(Node(4859),7891)
                                                   Node(4859).right=buildTree(Node(4859).right,7891)
                                                                   =buildTree(Node(9225),7891)
                                                                   Node(9225).left=buildTree(Node(9225).left,7891)
                                                                                  =buildTree(None,7891)
                                                                                  =buildTree(Node(7891),7891)
                                                                                  =return node
                                                                                  =Node(7891)
                                                                   =return node
                                                                   =Node(9225)
                                                   =return node
                                                   =Node(4859)
                                   =return node
                                   =Node(3264)
                    =return node
                    =Node(9845)
    =return node
    =Node(2732)
================================================
Node(2732) data=2732 right=Node(9845) left=None
Node(9845) data=9845 right=None       left=Node(3264)
Node(3264) data=3264 right=Node(4859) left=None
Node(4859) data=4859 right=Node(9225) left=None
Node(9225) data=9225 right=None       left=Node(7891)
Node(7891) data=7891 right=None       left=None
================================================         
datas[6]=4373
root=buildTree(Node(2732),4373)
    Node(2732).right=buildTree(Node(2732).right,4373)
                    =buildTree(Node(9845),4373)
                    Node(9845).left=buildTree(Node(9845).left,4373)
                                   =buildTree(Node(3264),4373)
                                   Node(3264).right=buildTree(Node(3264).right,4373)
                                                   =buildTree(Node(4859),4373)
                                                   Node(4859).left=buildTree(Node(4859).left,4373)
                                                                  =buildTree(None,4373)
                                                                  =buildTree(Node(4373),4373)
                                                                  =return node
                                                                  Node(4373)
                                                   =return node
                                                   =Node(4859)
                                   =return node
                                   =Node(3264)
                    =return node
                    =Node(9845)
    =return node
    =Node(2732)
================================================
Node(2732) data=2732 right=Node(9845) left=None
Node(9845) data=9845 right=None       left=Node(3264)
Node(3264) data=3264 right=Node(4859) left=None
Node(4859) data=4859 right=Node(9225) left=Node(4373)
Node(9225) data=9225 right=None       left=Node(7891)
Node(7891) data=7891 right=None       left=None
Node(4373) data=4373 right=None       left=None
================================================
datas[7]=5874
root=buildTree(Node(2732),5874)
    Node(2732).right=buildTree(Node(2732).right,5874)
                    =buildTree(Node(9845),5874)
                    Node(9845).left=buildTree(Node(9845).left,5874)
                                   =buildTree(Node(3264),5874)
                                   Node(3264).right=buildTree(Node(3264).right,5874)
                                                   =buildTree(Node(4859),5874)
                                                   Node(4859).right=buildTree(Node(4859).right,5874)
                                                                   =buildTree(Node(9225),5874)
                                                                   Node(9225).left=buildTree(Node(9225).left,5874)
                                                                                  =buildTree(Node(7891),5874)
                                                                                  Node(7891).left=buildTree(Node(7891).left,5874)
                                                                                                 =buildTree(None,5874)
                                                                                                 =buildTree(Node(5874),5874)
                                                                                                 =return node
                                                                                                 =Node(5874)
                                                                                  =return node
                                                                                  =Node(7891)
                                                                   =return node
                                                                   =Node(9225)
                                                   =return node
                                                   =Node(4859)
                                   =return node
                                   =Node(3264)
                    =return node
                    =Node(9845)
    =return node
    =Node(2732)
================================================
Node(2732) data=2732 right=Node(9845) left=None
Node(9845) data=9845 right=None       left=Node(3264)
Node(3264) data=3264 right=Node(4859) left=None
Node(4859) data=4859 right=Node(9225) left=Node(4373)
Node(9225) data=9225 right=None       left=Node(7891)
Node(7891) data=7891 right=None       left=Node(5874)
Node(4373) data=4373 right=None       left=None
Node(5874) data=5874 right=None       left=None
================================================
datas[8]=6744
root=buildTree(Node(2732),6744)
    Node(2732).right=buildTree(Node(2732).right,6744)
                    =buildTree(Node(9845),6744)
                    Node(9845).left=buildTree(Node(9845).left,6744)
                                   =buildTree(Node(3264),6744)
                                   Node(3264).right=buildTree(Node(3264).right,6744)
                                                   =buildTree(Node(4859),6744)
                                                   Node(4859).right=buildTree(Node(4859).right,6744)
                                                                   =buildTree(Node(9225),6744)
                                                                   Node(9225).left=buildTree(Node(9225).left,6744)
                                                                                  =buildTree(Node(7891),6744)
                                                                                  Node(7891).left=buildTree(Node(7891).left,6744)
                                                                                                 =buildTree(Node(5874),6744)
                                                                                                 Node(5874).right=buildTree(Node(5874).right,6744)
                                                                                                                 =buildTree(None,6744)
                                                                                                                 =buildTree(Node(6744),6744)
                                                                                                                 =return node
                                                                                                                 =Node(6744)
                                                                                                 =return node
                                                                                                 =Node(5874)
                                                                                  =return node
                                                                                  =Node(7891)
                                                                   =return node
                                                                   =Node(9225)
                                                   =return node
                                                   =Node(4859)
                                   =return node
                                   =Node(3264)
                    =return node
                    =Node(9845)
    =return node
    =Node(2732)
================================================
Node(2732) data=2732 right=Node(9845) left=None
Node(9845) data=9845 right=None       left=Node(3264)
Node(3264) data=3264 right=Node(4859) left=None
Node(4859) data=4859 right=Node(9225) left=Node(4373)
Node(9225) data=9225 right=None       left=Node(7891)
Node(7891) data=7891 right=None       left=Node(5874)
Node(4373) data=4373 right=None       left=None
Node(5874) data=5874 right=Node(6744) left=None
Node(6744) data=6744 right=None       left=None
================================================
datas[9]=3468
root=buildTree(Node(2732),3468)
    Node(2732).right=buildTree(Node(2732).right,3468)
                    =buildTree(Node(9845),3468)
                    Node(9845).left=buildTree(Node(9845).left,3468)
                                   =buildTree(Node(3264),3468)
                                   Node(3264).right=buildTree(Node(3264).right,3468)
                                                   =buildTree(Node(4859),3468)
                                                   Node(4859).left=buildTree(Node(4859).left,3468)
                                                                  =buildTree(Node(4373),3468)
                                                                  Node(4373).left=buildTree(Node(4373).left,3468)
                                                                                 =buildTree(None,3468)
                                                                                 =buildTree(Node(3468),3468)
                                                                                 =return node
                                                                                 =Node(3468)
                                                                  =return node
                                                                  =Node(4373)
                                                   =return node
                                                   =Node(4859)
                                   =return node
                                   =Node(3264)
                    =return node
                    =Node(9845)
    =return node
    =Node(2732)
================================================
Node(2732) data=2732 right=Node(9845) left=None
Node(9845) data=9845 right=None       left=Node(3264)
Node(3264) data=3264 right=Node(4859) left=None
Node(4859) data=4859 right=Node(9225) left=Node(4373)
Node(9225) data=9225 right=None       left=Node(7891)
Node(7891) data=7891 right=None       left=Node(5874)
Node(4373) data=4373 right=None       left=Node(3468)
Node(5874) data=5874 right=Node(6744) left=None
Node(6744) data=6744 right=None       left=None
Node(3468) data=3468 right=None       left=None
================================================

THE TREE
ROOT-Node(2732)-left = None
               -right= Node(9845)-left = Node(3264)-left = None
                                 -right= None      -right= Node(4859)-left = Node(4373)-left = Node(3468)-left = None
                                                                                       -right= None      -right= None
                                                                     -right= Node(9225)-left = Node(7891)-left = Node(5874)-left = None
                                                                                       -right= None      -right= None      -right= Node(6744)-left = None
                                                                                                                                             -right= None
def bs(node):
    if node.left is not None:
        bs(node.left)
    sort_datas.append(node.data)
    if node.right is not None:
        bs(node.right)

bs(root)        
bs(Node(2732))
    Node(2732).left is None
    sort_datas.append(2732)                                                                         [2732]                    
    Node(2732).right is not None                                                                    .
        bs(Node(2732).right)                                                                        .
        bs(Node(9845))                                                                              .
            Node(9845).left is not None                                                             .
                bs(Node(9845).left)                                                                 .
                bs(Node(3264))                                                                      .
                    Node(3264).left is None                                                         .
                    sort_datas.append(3264)                                                         [2732,3264]
                    Node(3264).right is not None                                                    .
                        bs(Node(3264).right)                                                        .
                        bs(Node(4859))                                                              .
                            Node(4859).left is not None                                             .
                                bs(Node(4859).left)                                                 .
                                bs(Node(4373))                                                      .
                                    Node(4373).left is not None                                     .
                                        bs(Node(4373).left)                                         .
                                        bs(Node(3468))                                              .
                                            Node(3468).left is None                                 .
                                            sort_datas.append(3468)                                 [2732,3264,3468]
                                            Node(3468).right is None                                .
                                    sort_datas.append(4373)                                         [2732,3264,3468,4373]
                                    Node(4373).right is None                                        .
                            sort_datas.append(4859)                                                 [2732,3264,3468,4373,4859]
                            Node(4859).right is not None                                            .
                                bs(Node(4859).right)                                                .
                                bs(Node(9225))                                                      .
                                    Node(9225).left is not None                                     .
                                        bs(Node(9225).left)                                         .
                                        bs(Node(7891))                                              .
                                            Node(7891).left is not None                             .
                                                bs(Node(7891).left)                                 .
                                                bs(Node(5874))                                      .
                                                    Node(5874).left is None                         .
                                                    sort_datas.append(5874)                         [2732,3264,3468,4373,4859,5874]
                                                    Node(5874).right is not None                    .
                                                        bs(Node(5874).right)                        .
                                                        bs(Node(6744))                              .
                                                            Node(6744).left is None                 .
                                                            sort_datas.append(6744)                 [2732,3264,3468,4373,4859,5874,6744]
                                                            Node(6744).right is None                .
                                            sort_datas.append(7891)                                 [2732,3264,3468,4373,4859,5874,6744,7891]
                                            Node(7891).right is None                                .
                                    sort_datas.append(9225)                                         [2732,3264,3468,4373,4859,5874,6744,7891,9225]
                                    Node(9225).right is None                                        .
            sort_datas.append(9845)                                                                 [2732,3264,3468,4373,4859,5874,6744,7891,9225,9845]
            Node(9845).right is None


'''