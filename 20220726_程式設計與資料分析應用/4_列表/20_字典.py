# ()元祖, []列表, {}字典
#{key:value, key:value}
#以key去找value
planets={"mecury":"水星", "venus":"金星", "earth":"地球"}
print(planets)
print(planets["mecury"])
#print(planets["水星"]) #反過來不行, 要再建立一組字典
#有辦法用程式碼去轉換, 但等會再說, 比較複雜
#print(planets[0]) #字典無法用索引
c2n={"水星":"mecury", "金星":"venus", "地球":"earth"}
print(c2n["水星"])


print(planets.keys())   #planets.keys():字典裡的key
print(planets.values()) #planets.values():字典裡的value

#keys:只是變數的集合, 關鍵字
#for, in:保留字, 指令
for key in planets.keys():
    print(key,planets[key]) #key:key, planets[key]:value
                            #as in print(planets["mecury"])
#for i in planets.keys():
#    print(i,planets[i])

for value in planets.values():
    #print(value,planets[value]) #無法從value回去找key
    print(value)

#建立新資料: 新增指定key與對應的value
#list : append
planets["mars"]="火星" #直接新增
print(planets)

#修改資料: 指定key更改value
#關鍵字不能重複, 若重複, 會覆蓋其值
planets["earth"]="地獄"
print(planets)

#刪除: 指定key, 刪除key及value
planets.pop("earth")
print(planets)

#如果沒有指定的key, 就會發生 KeyError而閃退
#第一種解決方式, 加條件判斷
if "jupiter" in planets.keys(): #or? if "jupiter" in planets
    print(planets["jupiter"])
    planets.pop("jupiter")

#第二種解決方式, 以get去找
#取得"jupiter"這個關鍵字的值, 若無此key, 傳回後面的值
x=planets.get("jupiter","沒這個字啦")
print(x)

#字典的key值, 採用 hashcode雜湊碼, 所以速度非常的快速
#比如相對的 list[n]: 會從0開始取, 依序取到n, 速度就比較慢
#1. 雜湊碼是一種演算法, 保證不同的物件, 不會有相同的雜湊碼
#2. 系統依據雜湊碼, 就知道要到哪裡去存取
#哲學, 宗教, 監獄

