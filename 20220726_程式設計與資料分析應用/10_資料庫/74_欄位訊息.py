import mysql.connector as mysql
conn=mysql.connect(host="mahaljsp.asuscomm.com",
                   user="lcc",
                   password="lcc0507",
                   database="cloud")

cursor=conn.cursor()
cursor.execute("select * from 台銀黃金")
for d in cursor.description:
    print(d[0])

# description除了欄位, 後面一堆東西是什麼意思? mysql-connector-python description 去google查
# 或是只看前面的欄位名稱就好

# cursor.close()
# conn.close()
