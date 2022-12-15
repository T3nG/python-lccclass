# 禁止使用 python 執行此法, 效能非常低, 那偽什麼要講述呢?
# 1. 大學二年級資料結構必考題
# 2. np.sort()就是使用類似此方法, 在使用 C語言執行
# 3. 很多人都說別人已經做出來了, 但不是自己做出來的

# 規則 : 假設有 n 個數 ( 0 ~ n-1)
# 第 i 個 ( 0 ~ n-2 ) 數,
# 要與後面相比 ( i+1 ~ n-1 ), 如果前面的值比較大, 則對調
import time

import numpy as np
np.random.seed(0)
n=10000
a=np.random.randint(0,100,n)
print(a)

t1=time.time()
for i in range(0,n-2+1):
    for j in range(i+1,n-1+1):
        if a[i]>a[j]:
            # tmp=a[i]
            # a[i]=a[j]
            # a[j]=tmp
            # 以上三行是C語言的寫法
            a[i], a[j] = a[j], a[i]
            # 一樣意思, 但實際上是做上面三行的事情
        #print(f"i={i},{a}")
t2=time.time()
print(a)
print(f"總共花費{t2-t1}秒")
