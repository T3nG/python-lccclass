#set
names=set(["thomas","kevin","tracy"])
print(names) #用的是大括弧
#set裡的資料不能重複
#一樣使用hashcode
#set為無序排列, 不會依照輸入的順序排列

#x=list(names)
#print(x)
#只是轉成list 還是無法留順序
#若真的需要順序呢? 把資料存成list, 再多一行轉成set用以存取及搜尋
#ls=["thomas","kevin","tracy"]
#names=set(ls)

#新增
names.add("john")
print(names)
names.add("kevin")
print(names)

#刪除
names.remove("thomas")
print(names)
names.pop() #移除第一個元素
print(names)

#全部清除
names.clear()
print(names)

#搜尋檔案的正確寫法, 比起轉成字典還要附上空集合
import os
path4="C:\\Users\\User\\OneDrive\\鯨鯨"
files=os.listdir(path4)
fs=set(files)
if "Increasing dominance.pdf" in fs: #秒殺
    print("已經有了")
else:
    print("無此檔案")