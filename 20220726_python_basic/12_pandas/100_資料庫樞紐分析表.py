import mysql.connector as mysql
import pandas as pd
from Gfile.G import G

dis=pd.options.display
dis.max_columns=None
dis.max_rows=None
dis.width=None
dis.max_colwidth=None

conn=mysql.connect(host=G.host_loc,
                   user=G.user_loc,
                   password=G.password_loc,
                   database=G.database_loc)
cursor=conn.cursor()
# cmd="select 日期, group_concat(國家) as 國家,"+\
# "sum(case when 水果='Apple' then 數量 else 0 end) as 蘋果,"+\
# "sum(case when 水果='Banana' then 數量 else 0 end) as 香蕉,"+\
# "sum(case when 水果='Orange' then 數量 else 0 end) as 橘子,"+\
# "sum(case when 水果='Grape' then 數量 else 0 end) as 葡萄,"+\
# "format(sum(單價*數量),4) as 總價 "+\
# "from 水果銷售 group by 日期 order by 日期"

cmd="select 日期,"+\
"sum(case when 水果 = 'Apple' then 數量 else 0 end) as 蘋果,"+\
"sum(case when 水果 = 'Banana' then 數量 else 0 end) as 香蕉,"+\
"sum(case when 水果 = 'Orange' then 數量 else 0 end) as 柳橙,"+\
"sum(case when 水果 = 'Grape' then 數量 else 0 end) as 葡萄,"+\
"format(sum(單價*數量), 4) as 總價 "+\
"from 水果銷售 group by 日期 "+\
"order by 日期"


cursor.execute(cmd)
cols=[d[0] for d in cursor.description]
data=[]
for r in cursor.fetchall():
    data.append(r)
cursor.close()
conn.close()
df=pd.DataFrame(data,columns=cols)
print(df)

# 資料量很大時, 不要用 pd.pivot_table, 要使用SQL語法