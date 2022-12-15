# pip install plotly plotly-express mysql-connector-python xlrd openpyxl
import pandas as pd
import plotly_express as px

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
print(df)
# lat: latitude 緯度
# lon: longitude 經度
fig = px.scatter_mapbox(
    data_frame=df,
    lat='lat',
    lon='lon',
    hover_name='City',
    hover_data=['State', 'Population'],
    zoom=4,  # set default zoom level (default 12)
    color_discrete_sequence=['fuchsia']  # 改變顏色
)
# 美化顯示 左右上下的邊界去除
fig.update_layout(mapbox_style='open-street-map',
                  margin=dict(l=0, r=0, t=0, b=0))
fig.show()
# 大陸封鎖 GoogleMap, 除非翻牆, 否則無法顯示
# 自己開發高德地圖 - 包含台灣資料
# 地圖資料: 圖資, 中研院的國家地理圖資非常差, 台灣世新圖資要花很多錢
