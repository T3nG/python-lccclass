import pandas as pd
import mysql.connector as mysql
from Gfile.G import G

# pandas DataFrame 印不出來? 出現省略記號 ...
# 完美列印 : 第一種
# 缺點: 打字串的時候容易打錯字出bug
# pd.set_option('display.max_columns',None) # 預設顯示欄位數 ? 個
# pd.set_option('display.max_rows',None) # 預設顯示列數 ? 個 max_r, max_ro, max_row, max_rows 都可以...
# pd.set_option('display.width',None) # 預設顯示寬度 ?
# pd.set_option('display.max_colwidth',None) # 預設單一欄寬度 ?
# 以上全部取消限制, 讓所有資料都可以print出來, 老師預測此種方式將來可能被取消

# 完美列印 : 第二種
dis=pd.options.display
# print(dis.max_columns)
# print(dis.max_rows)
# print(dis.width)
# print(dis.max_colwidth)
dis.max_columns=None
dis.max_rows=None
dis.width=None
dis.max_colwidth=None


conn=mysql.connect(host=G.host,
                   user=G.user,
                   password=G.password,
                   database=G.database)
cursor=conn.cursor()
cursor.execute("select * from 台灣股市")
ds=cursor.description # 欄位名稱

cols=[d[0] for d in ds] # 取得欄位
print(cols)

data=[]
for r in cursor.fetchall():
    data.append(r)
df=pd.DataFrame(data=data, columns=cols)
print(df)

'''以下跳至 95_讀取行列 以繼續'''
ls=df.values
for i in range(10,20):
    print(ls[i])
# 將df的每一列變成集合
# 取其中的10列


