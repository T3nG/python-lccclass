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
ls = []
for row in rows:
    for i in range(6):
        # 將每一期的六個獎號依序加進 ls
        ls.append(row[3+i])

df = pd.DataFrame({'no': ls})
sns.countplot(x='no', data=df)
plt.show()

conn.close()
cur.close()