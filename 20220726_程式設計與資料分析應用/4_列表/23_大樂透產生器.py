import random
# ls=[]
# for i in range(7):
#     ls.append(random.randint(1,49))
# print(ls)
# 會重複, 是有檢查的方法, 但很複雜

nums=set([])
index=0
while len(nums)<7:
    n=random.randint(1,49)
    nums.add(n)
    index+=1
    print(f"產生第{index}次 : {n}")
print(nums)