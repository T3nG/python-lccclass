# pip install matplotlib
import pylab as plt
import mysql.connector as mysql
from G import G

conn = mysql.connect(host=G.host, user=G.user, password=G.password, database=G.dbCloud)
cursor = conn.cursor()
cmd = "select * from 台銀黃金測試 order by 日期 asc"
cursor.execute(cmd)
rs = cursor.fetchall()
dates = [r[1] for r in rs]
y = [r[3] for r in rs]
x = list(range(len(rs)))
cursor.close()
conn.close()

#plt.plot(dates, y)
plt.plot(x, y)
f = plt.poly1d(plt.polyfit(x, y, 10))

plt.plot(x, f(x), color='r', linewidth=2)
plt.show()


