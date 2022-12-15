import mysql.connector as mysql
from Gfile.G import G
conn=mysql.connect(host=G.host,
                   user=G.user,
                   password=G.password,
                   database=G.database)


cursor=conn.cursor()
cmd="select * from 台灣股市 order by 日期"
cursor.execute(cmd)

rs=cursor.fetchall()

for r in rs:
    print(r)
cursor.close()
conn.close()
# 資料取得之後, 關閉cursor與連線(降低伺服器端的負載)

# 把取得的資料放到本機的資料庫內
conn=mysql.connect(host=G.host_loc,
                   user=G.user_loc,
                   password=G.password_loc,
                   database=G.database_loc)
cursor=conn.cursor()
for r in rs:
    try: # 例外處理
        cmd=f"insert into 台灣股市 (日期, 開盤, 最高, 最低, 收盤) values ('{str(r[1])}',{r[2]},{r[3]},{r[4]},{r[5]})"
        print(cmd) # 印出現在新增到哪裡了
        cursor.execute(cmd)
        conn.commit() # commit後才會真正寫入
    except mysql.errors.IntegrityError as e:
        # 把錯誤訊息當成 e 因為太長了, 不印e, 而是印下面的print, print(e.msg) 可以印出錯誤訊息
        print("日期重複...")
cursor.close()
conn.close()

# 日期要轉成字串 'str(r[1])'

# 用這個方式搬需要搬很久