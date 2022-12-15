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

p = figure(width=1024, height=400, title='台銀黃金, 賣出', x_range=FactorRange(factors=date))  # x_axis_type=None
# x 軸標籤轉45度
p.xaxis.major_label_orientation = np.pi/4
p.title.text_color = 'olive'
p.title.text_font_style = 'italic'
# bottom: 以下的不畫, 會太長
p.vbar(x=date, top=sell, bottom=1500, width=0.5, color='blue', alpha=0.6, line_width=2)

# map dataframe indices to date strings and use as label overrides
# p.xaxis.major_label_overrides = {
#     i: d for i, d in enumerate(date)
# }
from bokeh.models import SingleIntervalTicker, LinearAxis
ticker = SingleIntervalTicker(interval = 5, num_minor_ticks = 10)
xaxis = LinearAxis(ticker = ticker)
p.add_layout(xaxis, 'below')
show(p)
