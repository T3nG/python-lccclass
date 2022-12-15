import mysql.connector as mysql
from Gfile.G import G
conn=mysql.connect(host=G.host,
                   user=G.user,
                   password=G.password,
                   database=G.database)

cursor=conn.cursor()
cursor.execute("select * from 台銀黃金")
for d in cursor.description:
    print(d[0])

# description除了欄位, 後面一堆東西是什麼意思? mysql-connector-python description 去google查
# 或是只看前面的欄位名稱就好

# cursor.close()
# conn.close()
