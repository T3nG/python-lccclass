'''
台銀黃金 :
    id PK NN AI
    日期 NN UQ
    買進 double
    賣出 double

今彩539 :
    id PK NN AI
    日期 NN UQ
    期數 varchar9 NN
    n1 int NN
    n2
    n3
    n4
    n5

大樂透649 :
    id PK NN AI
    日期 UQ
    期數 varchar9
    n1 int
    n2
    n3
    n4
    n5
    n6
    n7

face :
    id bigint PK NN AI
    name varchar45 NN
    descriptor BLOB NN
    address varchar45

'''


import mysql.connector as mysql
conn=mysql.connect(host="mahaljsp.asuscomm.com",
                   user="lcc",
                   password="lcc0507",
                   database="cloud")
cursor=conn.cursor()
# cursor.execute("select * from 台灣股市")
# cursor.execute("select * from 台銀黃金")
# cursor.execute("select * from 大樂透649")
# cursor.execute("select * from 今彩539")
cursor.execute("select * from face")
rs=cursor.fetchall()
cursor.close()
conn.close()

conn=mysql.connect(host="localhost",
                   user="dengfixanros",
                   password="666x-GGteng%",
                   database="cloud")
cursor=conn.cursor()
data=[]
# 台灣股市
# for r in rs:
#     data.append([str(r[1]),r[2],r[3],r[4],r[5]])
# cmd="insert into 台灣股市 (日期, 開盤, 最高, 最低, 收盤) values (%s, %s, %s, %s, %s)"

# 台銀黃金
# for r in rs:
#     data.append([str(r[1]),r[2],r[3]])
# cmd="insert into 台銀黃金 (日期, 買進, 賣出) values (%s, %s, %s)"

# 大樂透649
# for r in rs:
#     data.append([str(r[1]),r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9]])
# cmd="insert into 大樂透649 (日期, 期數, n1, n2, n3, n4, n5, n6, n7) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

# 今彩539
# for r in rs:
#     data.append([str(r[1]),r[2],r[3],r[4],r[5],r[6],r[7]])
# cmd="insert into 今彩539 (日期, 期數, n1, n2, n3, n4, n5) values (%s, %s, %s, %s, %s, %s, %s)"

# face
for r in rs:
    data.append([r[1],r[2],r[3]])
cmd="insert into face (name, descriptor, address) values (%s, %s, %s)"

cursor.executemany(cmd, data) # 只開一次連線, 然後將所有資料一次性寫入
conn.commit()
cursor.close()
conn.close()