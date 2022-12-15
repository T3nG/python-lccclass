# pip install plotly-express
# plotly-express 是一種精美繪製圖表的套件, 比 matplotlib要強
# 但需要輸入及微調的參數更多
import plotly_express as px
import pandas as pd
dis=pd.options.display
dis.max_columns=None
dis.max_rows=None
dis.width=None
dis.max_colwidth=None

df=px.data.gapminder() # data.gapminder()是用pandas的DataFrame來做的
#print(df)
'''
country: 國家
continent: 洲別
gdpPercap: 國民所得
iso_alpha: 國別代碼
lifeExp: 平均壽命
pop: 人口數
'''

# DataFrame可以用類似資料庫的查詢功能
# dfTaiwan=df.query("country=='Taiwan'")
# print(dfTaiwan)
df2007=df.query('year==2007')

# 讀取列
# ls=df.values
# for i in range(10,20):
#     print(ls[i])

dv=df.values # df.values.dtype 可以顯示出, 此為物件
print(dv)
print("讀取values\n")

# dv[[0,1,2,3,4]], 外面的[]是索引, 裡面的[]是list, 這是DataFrame的功能
print(dv[0]) # 以索引讀取列
print("以索引讀取第 0 列\n")

print(dv[[0,1,2,3,4]]) # 以列表讀取列
print(dv[:5])
print("以列表讀取 第 0 ~ 4 列\n")
# dv[[0,1,2,3,4]] 與 dv[:5] 意思相同

print(dv[2:5]) # 讀取第 2, 3, 4 列
print("讀取第 2, 3, 4 列\n")

# 讀取儲存格
di=df.iloc

print(di[0,0]) # 第 0 列, 第 0 行
print("讀取第 0 列, 第 0 行\n")

print(di[0, : ]) # 單列時, 列出每一欄的資料 或? print(di[0])
print("讀取單列時, 垂直列出每一欄的資料\n")

print(di[0:5, : ]) # 列切片時, 採用橫向列印 或? print(di[0:5])
print("以列切片讀取時, 採橫向列印\n")

# 讀取整行資料
dcol=df2007[['country','continent','year']]
print(dcol)

# 每個欄位又稱為特徵, 是AI機器學習的重要觀念