import pandas as pd
import numpy as np

# DataFrame 就是產生跟 Excel 類似的表格資料
# C#就是 Tables

# 第一種產生方式
# 字典={key1:[], key2:[], ...} ,
# key是欄位名稱, 每個list的長度都需一樣, 因為代表著筆數
data = {
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['段譽', '虛竹', '喬峰', '張三豐', '張無忌', '趙敏'],
    'account': ['thomas', 'kevin', 'eric', 'wind', 'kenneth', 'vivian'],
    'password': ['1234', '2345', '3456', '4567', '5678', '6789'],
    'sex': ['M', 'M', 'M', 'M', 'M', 'F'],
    'address': ['大理', '少林', '大寮', '武當', '光明頂', '蒙古']
}
df = pd.DataFrame(data)
print(f'第一種方式\n{df}')
print()

# 第二種方式: 以列為主, 每列以 {欄1:值1, 欄2:值2, ...}
# 的字典方式形成, 再將每列加入list中
# 此種方式比較少用
# 但寫入資料的時候, 可以不管順序
data2 = []
data2.append({'id': 1, 'name': '段譽', 'account': 'thomas', 'password': '1234', 'sex': 'M', 'address': '大理'})
data2.append({'id': 2, 'name': '虛竹', 'account': 'kevin', 'password': '2345', 'sex': 'M', 'address': '少林'})
data2.append({'id': 3, 'account': 'eric', 'name': '喬峰', 'password': '3456', 'sex': 'M', 'address': '大寮'})
data2.append({'id': 4, 'name': '張三豐', 'account': 'wind', 'password': '4567', 'sex': 'M', 'address': '武當'})
data2.append({'id': 5, 'name': '張無忌', 'account': 'kenneth', 'password': '5678', 'sex': 'M', 'address': '光明頂'})
data2.append({'id': 6, 'name': '趟敏', 'account': 'vivian', 'password': '6789', 'sex': 'F', 'address': '蒙古'})
df2 = pd.DataFrame(data2)
print(f'第二種方式\n{df2}')
print()

# 第三種方式: 也是以列為主, 每列的資料集合在list中,
# 再將每列加入list中, 最後指定columns, 在列舉資料表時, 最為常用
data3 = []
data3.append([1, '段譽', 'thomas', '1234', 'M', '大理'])
data3.append([2, '虛竹', 'kevin', '2345', 'M', '少林'])
data3.append([3, '喬峰', 'eric', '3456', 'M', '大寮'])
data3.append([4, '張三豐', 'wind', '4567', 'M', '武當'])
data3.append([5, '張無忌', 'kenneth', '5678', 'M', '光明頂'])
data3.append([6, '趟敏', 'vivian', '6789', 'F', '蒙古'])
cols = ['id', 'name', 'account', 'password', 'sex', 'address']
df3 = pd.DataFrame(data=data3, columns=cols)  # 註記 .Series(data=, index=)
print(f'第三種方式\n{df3}')
print()
