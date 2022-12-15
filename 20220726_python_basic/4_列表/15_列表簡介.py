#lsit : 列表, 資料型態
a=[10,20,30,40,50]
print(a[0]) # [索引 index, 由 0 開始]
print(a[1])
print(a[2])
print(a)
# print(a[5]) # list index out of range 索引超出範圍
print(len(a)) # 列出 a 的長度
print(type(a)) # class : list

#使用迴圈遍訪所有的元素, 指定索引
for i in range(len(a)): # i=0,1,2,3,4
    print(a[i])

#使用 for-each遍訪所有元素, 將list a裡面的元素直接丟給i
for i in a: # i= 10,20,30,40,50
    print(i)
#list : 像哆啦A夢的百寶袋, 而且是很髒的百寶袋, 便當, 大便都可以裝
#list 裡的資料格式可以混用, 不需要一樣
#list 裡可以裝的元素, 沒有數量限制, 直到記憶體爆掉為止
#就算800萬筆資料, 32G也不會爆
b=["mecury", 100, "venus", "earth", 50]
print(b)
for i in b:
    print(f"{i}", end=" ")
print()

#list 長度可以變更
c=["mecury", "venus", "earth"]
c.append("mars") #append : 附加在最後面
c.append("jupiter")
print(c)

