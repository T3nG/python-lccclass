# pip install mysql-connector-python
import numpy as np
import plotly.graph_objects as go
import mysql.connector as mysql
from Gfile.G import G
conn = mysql.connect(
    host=G.host,
    user=G.user,
    password=G.password,
    database=G.database)
cur = conn.cursor()
cur.execute("select * from 台灣股市 where 日期 >= '2020/01/01' order by 日期")
rows = cur.fetchall()
conn.close()
cur.close()
points = []
dates = []
for row in rows:
    points.append(row[5])  # 收盤價
    dates.append(row[1])
x = range(len(rows))
f = np.poly1d(np.polyfit(x, points, 10))
reg = f(x)
# 以下開始畫圖
fig = go.Figure()
# 折線圖
fig.add_trace(
    go.Scatter(
        x=dates,
        y=points,
        mode='lines+markers',
        name='大盤指數',  # legend
        line=dict(color='royalblue', width=2)  # line color and width
    )
)
# 迴歸線
fig.add_trace(
    go.Scatter(
        visible=True,
        x=dates,
        y=reg,
        mode='lines',
        name='日k縣',
        line=dict(color='orange', width=2)
    )
)
# rangeslider 範圍選擇器, 4個選項, 1個月, 6個月, 1年, 全部
fig.update_layout(
    dragmode='pan',  # 平移
    title_text='台灣股市分析',
    xaxis=go.layout.XAxis(
        rangeselector=dict(
            buttons=[
                dict(count=1, label='1 month', step='month',stepmode='backward'),
                dict(count=6, label='6 month', step='month',stepmode='backward'),
                dict(count=1, label='1 year', step='year',stepmode='backward'),
                dict(label='全部', step='all')
            ]
        ),
        rangeslider={'visible': True}
    )
)
fig.show()
