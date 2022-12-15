# numpy(爛派) 是一套統計學的套件(科學計算)
# 其中的格式, 就是矩陣, 矩陣的長度一旦定下, 就不能變更
# pip install numpy
import numpy as np
l=[1,2,3,4,5] # list 有逗號
a=np.array(l) # array(list) 無逗號
print(f"List: {l}")
print(f"Array: {a}")
print("")
print(f"List: {l[0]}")
print(f"Array: {a[0]}")

# 遍訪 list, array 的方法
for i in range(len(a)):
    print(a[i])
for x in a:
    print(x)

# array 無法更改長度
# list 可以更改長度
# 因為array無法更改長度, 所以效能上比list高出好幾千倍
# 索引 vs 雙向連結
# 系統上, 並沒有array, 只有list, 所以MTA不考array
# array必須依靠第三方套件 numpy
l.append(20)
#a.append(20) <==error