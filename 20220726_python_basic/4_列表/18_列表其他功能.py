planets=["mecury","venus","jupiter"]

#附加
planets.append("saturn")

#插入列表, 在指定索引之前插入
planets.insert(2,"earth")
planets.insert(3,"mars")

#修改
planets[2]="hell"  #替換掉

#刪除
planets.pop(2)

print(planets)

#集合中的集合
math=[["thomas",80],["kevin",90],["tracy",100]]
print(math)
print(math[0])
print(math[1])
print(math[0][0]) # 二維list
print(math[0][1])
for m in math:
    print(m)