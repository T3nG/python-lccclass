import pandas as pd
import numpy as np

# idx=['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune','pluto']
# planets=['水星','金星','地球','火星','木星','土星','天王星','海王星','冥王星']
#
# s=pd.Series(data=planets, index=idx) # data=值, index=索引
# print(s)
#
# # 底下這兩個有什麼差異性呢?
# # dict無法使用索引, Series 可以
# print(s[8])
# print(s['pluto'])

import mysql.connector as mysql
from Gfile.G import G
conn=mysql.connect(host=G.host,
                   user=G.user,
                   password=G.password,
                   database=G.database)
cursor=conn.cursor()
cursor.execute("select * from 台灣股市")
ds=cursor.description # 欄位名稱
print(ds)

idx=[d[0] for d in ds] # d[0]? 只取欄位名稱, ds包含了欄位的所有資料
print(idx)

# rs=cursor.fetchall() # 取得全部資料
r=cursor.fetchone() # 取得一筆資料, 若使用迴圈大量存取fetchone會當機, 有bug, 雖較省記憶體
print(r)

s=pd.Series(data=r,index=idx) # data也吃tuple
# print(s)
print(s[5])
print(s['收盤'])
# 當存取資料庫時, 欄位太多的時候, 可以用索引標籤去找特定欄位, 而不用慢慢數是第幾個了