#練習題
#產生n個整數亂數, 放在list裡

import random
n=10
listB=[]
for i in range(n):
    listB.append(random.randint(1,500)) #randint 必須給範圍
#print(listB)

#計算總和
sum=0
for i in listB:
    sum+=i
print(sum)   # 總和
print(sum/n) # 平均數
