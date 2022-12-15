import pandas as pd
import mysql.connector as mysql
import plotly_express as px
import plotly
import numpy as np
from Gfile.G import G

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# http://mahaljsp.asuscomm.com/index.php/2019/04/17/python_db/
# 如果使用其他資料庫套件, 都是錯誤的教學, 只能使用 mysql-connector-python
conn = mysql.connect(
    host=G.host,
    user=G.user,
    password=G.password,
    database=G.database)
cur = conn.cursor()
cmd = 'select * from covid19'  # 模擬的
cur.execute(cmd)
# 抓取資料
rows = cur.fetchall()
data = []
for row in rows:
    data.append(row)
# 抓取資料庫的欄位
description = cur.description
columns = [d[0] for d in description]

df = pd.DataFrame(data=data, columns=columns)
print(df)

cur.close()
conn.close()

# 一定要設定權杖才能讀取 street地圖
# https://mapbox.com/ 註冊並新增權杖 token
lcc_token = "pk.eyJ1IjoiZGVuZ2ZpeGFucm9zIiwiYSI6ImNsYmY0amliczAycmQzcG1yY2VrbDVtcmkifQ.UZqgv7bRN7jOykHp8H8y8A"
px.set_mapbox_access_token(lcc_token)

fig = px.scatter_mapbox(
    data_frame=df,
    lat='lat',
    lon='lng',
    zoom=10,
    hover_name='address',
    hover_data=['area']
)
fig.update_layout(mapbox_style='streets',
                  margin=dict(l=0, r=0, t=0, b=0))
fig.show()
