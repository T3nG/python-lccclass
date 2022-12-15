# add(x+y) : 自訂函數
# print()  : 系統函數
# *x : 以tuple的方式接收
def add(*x):
    sum=0
    for i in x:
        sum+=i
    return sum

m=[10,20,30,40,50]
z=add(10,20,30,50,60,70)
# z0=add(m) 列表無法如此直接作
z0=add(m[0],m[1],m[2],m[3],m[4])
z1=add(*m) # 將list展開成一個一個的參數
print(z)
print(z0)
print(z1)

# print("a")
# print("a","b")
# print("a","b","c")