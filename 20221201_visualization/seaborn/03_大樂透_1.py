# pip install mysql-connector-python
import seaborn as sns
import pandas as pd
import pylab as plt
import mysql.connector as mysql
from Gfile.G import G

conn = mysql.connect(
    host=G.host,
    user=G.user,
    password=G.password,
    database=G.database)
cmd = 'select * from 大樂透649 order by 日期'
cur = conn.cursor()
cur.execute(cmd)

rows = cur.fetchall()
x = []
y = []

for row in rows:
    for i in range(7):
        x.append(i+1)       # [1, 2, 3, 4, 5, 6, 7, ...]
        y.append(row[3+i])  # 七個獎號

df = pd.DataFrame({'x': x, 'y': y})
# catplot: 分類數據圖, swarm: 成群, box: 箱型圖, boxen: 拳擊, bar: 長條圖, point: 折線圖
sns.catplot(data=df, x='x', y='y', kind='boxen')
plt.show()

conn.close()
cur.close()