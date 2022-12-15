import mysql.connector as mysql
import pandas as pd
import plotly_express as px
from Gfile.G import G

conn = mysql.connect(
    host=G.host,
    user=G.user,
    password=G.password,
    database=G.database)
cur = conn.cursor()
cur.execute("select * from 台銀黃金 where 日期>='2022/1/01' order by 日期")
rows = cur.fetchall()
conn.close()
cur.close()

l1 = [(row[1], row[2], '買進') for row in rows]
l2 = [(row[1], row[3], '賣出') for row in rows]
ls = l1 + l2
columns = ['date', 'price', 'type']
df = pd.DataFrame(ls, columns=columns)

fig = px.line(df,
              x='date',
              y='price',
              color='type'
              )
fig.show()
