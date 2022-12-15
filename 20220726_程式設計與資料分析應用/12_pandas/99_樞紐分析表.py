import mysql.connector as mysql
import pandas as pd

dis=pd.options.display
dis.max_columns=None
dis.max_rows=None
dis.width=None
dis.max_colwidth=None

conn=mysql.connect(host='localhost',
                   user='dengfixanros',
                   password='666x-GGteng%',
                   database='cloud')
cursor=conn.cursor()
cmd="select * from 水果銷售"
cursor.execute(cmd)

# 欄位資料
idx=[d[0] for d in cursor.description]
idx.remove("id") # 去掉id, 用dataframe的索引

data=[]
for r in cursor.fetchall():
    data.append([str(r[1]),r[2],r[3],r[4],r[5]])

cursor.close()
conn.close()

df=pd.DataFrame(data, columns=idx)
# print(df) 檢查
# df=pd.DataFrame(data, columns=idx).query("國家=='US'")
# 條件式選取單一國家

table=df.pivot_table(index=['日期'],
                     columns=['水果'],
                     values=['數量'],
                     fill_value=0,
                     aggfunc='sum')
# index 最左分類, columns 欄位, values 上層欄位?, fill_value=0 空白欄位填入0, aggfunc='sum', 重複數值相加

print(table)

'''
建議用資料庫mySQL去做樞紐分析表(百萬筆資料)

use cloud;
select 日期, group_concat(國家) as 國家, 
sum(case when 水果='Apple' then 數量 else 0 end) as 蘋果,
sum(case when 水果='Banana' then 數量 else 0 end) as 香蕉,
sum(case when 水果='Orange' then 數量 else 0 end) as 橘子,
sum(case when 水果='Grape' then 數量 else 0 end) as 葡萄,
format (sum(單價*數量),4) as 總價
from 水果銷售 group by (日期) order by 日期

'''