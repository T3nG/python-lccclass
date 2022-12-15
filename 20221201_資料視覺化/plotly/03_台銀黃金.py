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
cur.execute("select * from 台銀黃金 where 日期 >= '2018/01/01' order by 日期")
rows = cur.fetchall()
conn.close()
cur.close()
sell = []
buy = []
dates = []
for row in rows:
    dates.append(row[1])
    buy.append(row[2])
    sell.append(row[3])
x = range(len(rows))
f = np.poly1d(np.polyfit(x, sell, 10))
reg = f(x)
# 以下繪圖
trace1 = go.Scatter(
    x=dates,
    y=sell,
    mode='lines',
    name='賣出',
    line=dict(color='royalblue', width=2)
)
trace2 = go.Scatter(
    x=dates,
    y=buy,
    mode='lines',
    name='買進',
    line=dict(color='green', width=2)
)
trace3 = go.Scatter(
    x=dates,
    y=reg,
    mode='lines',
    name='迴歸線',
    line=dict(color='orange', width=2)
)
data = [trace1, trace2, trace3]
fig = go.Figure(data=data)
fig.update_layout(
    dragmode='pan',
    title_text='台銀黃金存摺',
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
