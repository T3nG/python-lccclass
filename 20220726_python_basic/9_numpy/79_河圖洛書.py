# 假設有 n*n 格, n必須為奇數
# 最上列, n//2行, 填入1
# 若是在最右上角[n-1,n-1], 往下降一列
# 否則
#   往上右角移動
#   若超出列邊界, 列為 n-1
#   若超出行邊界, 行為 0
#   若右上角有東西, 往左一行, 往下二列

import numpy as np
n=7
d=np.zeros([n,n],dtype=np.int32)
x=n//2
y=0
index=1
while index<=n*n:
    d[y,x]=index
    index+=1
    if x==n-1 and y==0:
        y+=1
    else:
        # x+=1
        # y-=1
        # if y<0:
        #     y=n-1
        # if x>n-1:
        #     x=0
        x=(x+1)%n # 遞增循環 0, 1, 2, 3, 4, 0, 1, 2...
        y=(y-1+n)%n # 遞減循環 4, 3, 2, 1, 0, 4, 3, 2, 1, 0...
        if d[y,x]!=0:
            x-=1
            y+=2

for row in d:
    for col in row:
        print(f"{col:5d}", end="")
    print()
# 讓印出來的方陣好看一點, 去括號去點點
