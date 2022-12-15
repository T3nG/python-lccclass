# 進行資料大量的搬移的時候, 使用第二種
# 一筆一筆輸入資料的時候, 使用第一種, 速度慢, 效能差, 但即使某筆錯誤, 也可確保其他資料可以寫入
# 大量搬移有可能遇到的問題, 若某一筆出現問題, 全部都不能寫入

# Truncate table => 把資料表內的資料清空
# 日期 UQ 打勾 , 數值唯一不重複
import mysql.connector as mysql
conn=mysql.connect(host="mahaljsp.asuscomm.com",
                   user="lcc",
                   password="lcc0507",
                   database="cloud")
cursor=conn.cursor()
cmd="select * from 台灣股市 order by 日期"
cursor.execute(cmd)
rs=cursor.fetchall()
# for r in rs:
#     print(r)
cursor.close()
conn.close()
# 上: 取得資料
# 下: 寫入資料
conn=mysql.connect(host="localhost",
                   user="dengfixanros",
                   password="666x-GGteng%",
                   database="cloud")
cursor=conn.cursor()
data=[]
for r in rs:
    data.append([str(r[1]),r[2],r[3],r[4],r[5]])
    # 轉成二維格式
    # data的格式 [['2000-01-01',100,200,300,400],[...],[...]]
print(data)
cmd="insert into 台灣股市 (日期, 開盤, 最高, 最低, 收盤) values (%s, %s, %s, %s, %s)"
cursor.executemany(cmd, data) # 只開一次連線, 然後將所有資料一次性寫入
conn.commit()
cursor.close()
conn.close()
