# pip install xlrd / openpyxl
# xlrd: 讀取Excel
# openpyxl: 寫入Excel

import mysql.connector as mysql
import pandas as pd

conn=mysql.connect(host="mahaljsp.asuscomm.com", user="lcc", password="lcc0507", database="cloud")
cursor=conn.cursor()
cursor.execute("select * from 台灣股市")
ds=cursor.description
cols=[d[0] for d in ds]#取得欄位名稱
print(cols)
data=[]
for r in cursor.fetchall():
    data.append(r)
df=pd.DataFrame(data=data, columns=cols)

df.to_excel("台灣股市.xlsx",index=False) # 不寫入索引
df.to_excel("台灣股市.xlsx",sheet_name='資料表',index=False)
# 指定資料表名稱

# 沒有安裝Excel?
# df.to_csv 匯出成 csv檔(純文字)