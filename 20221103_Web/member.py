# pip install mysql-connector-python
import mysql.connector as mysql
from G import G



conn = mysql.connect(host=G.host, user=G.user, password=G.password, database=G.database)
cursor = conn.cursor()

cmd = "select * from 會員資料表"
# cmd = "select * from 台灣股市"
cursor.execute(cmd)
rs = cursor.fetchall()
for r in rs:
    print(r)

conn.close()