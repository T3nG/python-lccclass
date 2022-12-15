# pip install mysql-connector-python matplotlib
import mysql.connector as mysql
from bokeh.plotting import figure, show
from bokeh.models import FactorRange
import numpy as np
import pylab as plt
from Gfile.G import G
conn = mysql.connect(
    host=G.host,
    user=G.user,
    password=G.password,
    database=G.database)
cur = conn.cursor()
cmd = "SELECT * FROM 台銀黃金 WHERE 日期 >= '2022/01/01' ORDER BY 日期"
cur.execute(cmd)
rows = cur.fetchall()
conn.close()
cur.close()

# str from time
date = [row[1].strftime('%Y-%m-%d') for row in rows]
sell = [row[3] for row in rows]

p = figure(width=1024, height=400, title='台銀黃金, 賣出', x_range=FactorRange(factors=date))
# x 軸標籤轉45度
p.xaxis.major_label_orientation = np.pi/4
p.title.text_color = 'olive'
p.title.text_font_style = 'italic'
p.line(date, sell, color='blue', alpha=0.6, line_width=2)
# 回歸線
n = len(rows)
x = np.linspace(1, n, n)
# np, plt 都可以, 推測應該是 plt 去調用 np
f = np.poly1d(np.polyfit(x, sell, 10))
# f = plt.poly1d(plt.polyfit(x, sell, 10))
line = f(x)
p.line(date, line, color='red', alpha=0.6)
show(p)
