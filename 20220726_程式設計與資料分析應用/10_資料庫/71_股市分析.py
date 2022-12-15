# 使用 Python 連線 MySQL時, 需要驅動程式
# mysqlclient : 官方版本(oracle), 由c/c++寫成, 效能高
# mysql-connector-python : 官方版本, 純Python寫成, 執行 ORM時效能高
# pymysql : 日本人寫的, 純Python寫成, 效能奇差無比

import mysql.connector as mysql
import numpy as np
import pylab as plt

# 建立連線
conn=mysql.connect(host="mahaljsp.asuscomm.com",
                   user="lcc",
                   password="lcc0507",
                   database="cloud")

# 建立執行命令的物件 - cursor : 游標
cursor=conn.cursor()

cmd="select * from 台灣股市 where 日期>='2022-01-01' order by 日期"
# SQL的字串使用"", ''留給SQL語法
cursor.execute(cmd)

rs=cursor.fetchall() # recordSet

for r in rs:
    print(r)

# x軸的值
x=list(range(len(rs))) # x軸的值, 第一筆到最後一筆
y=[r[5] for r in rs]   # y軸的值, 收盤價
plt.figure(figsize=(12,6))
plt.scatter(x,y)
# 回歸線
f=np.poly1d(np.polyfit(x,y,10))
plt.plot(x,f(x),c="r")
plt.show()

cursor.close()
conn.close()