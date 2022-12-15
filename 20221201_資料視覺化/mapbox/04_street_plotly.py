# http://mahaljsp.asuscomm.com/index.php/2022/05/11/mapbox-with-px/
import pandas as pd
import mysql.connector as mysql
import plotly_express as px
import plotly.graph_objects as go
import numpy as np
from Gfile.G import G

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# http://mahaljsp.asuscomm.com/index.php/2019/04/17/python_db/
# 如果使用其他資料庫套件, 都是錯誤的教學, 只能使用 mysql-connector-python
conn = mysql.connect(
    host=G.host,
    user=G.user,
    password=G.password,
    database=G.database)
cur = conn.cursor()
cmd = 'select * from covid19'  # 模擬的
cur.execute(cmd)
# 抓取資料
rows = cur.fetchall()
lat = np.array([r[3] for r in rows])
lng = np.array([r[2] for r in rows])
addr = np.array([r[5] for r in rows])
cur.close()
conn.close()

# mapbox token
lccclass_token = "pk.eyJ1IjoiZGVuZ2ZpeGFucm9zIiwiYSI6ImNsYmY0amliczAycmQzcG1yY2VrbDVtcmkifQ.UZqgv7bRN7jOykHp8H8y8A"
fig = go.Figure(
    go.Scattermapbox(
        lat=lat,
        lon=lng,
        # 因為資料庫內的資料是亂數排列的, 軌跡圖秀出來只是一堆跳來跳去的線
        # mode='markers+lines',
        mode='markers',
        hovertext=addr,  # 額外顯示資訊(包含原本顯示的經緯度)
        # text=addr,
        # hoverinfo='text'  # 取代原本顯示的經緯度
        # 圖標無法點擊, marker沒有click去產生另一個視窗, 無法按
        marker=dict(
            symbol='car',
            size=20
        )
    )
)
fig.update_layout(
    mapbox=dict(
        accesstoken=lccclass_token,
        zoom=10,
        bearing=0,  # 逆時針旋轉, 度, 在手機可以偵測目前的方位而動態旋轉(android, kotlin)
        center=go.layout.mapbox.Center(
            # 以最後一點的經緯度作為中心點
            lat=lat.mean(),
            lon=lng.mean()
        )
    ),
    mapbox_style='streets',  # 不指定就呈現灰色
    margin=dict(l=0, r=0, t=0, b=0)
)
fig.show()

'''symbol list 有的可以用有的不行
airfield
airport
alcohol-shop
amusement-park
aquarium
art-gallery
attraction
bakery
bank
bar
beer
bicycle
bicycle-share
bus
cafe
campsite
car
castle
cemetery
cinema
circle
circle-stroked
clothing-store
college
dentist
doctor
dog-park
drinking-water
embassy
entrance
fast-food
ferry
fire-station
fuel
garden
golf
grocery
harbor
heliport
hospital
ice-cream
information
laundry
library
lodging
marker
monument
mountain
museum
music
park
pharmacy
picnic-site
place-of-worship
playground
police
post
prison
rail
rail-light
rail-metro
religious-christian
religious-jewish
religious-muslim
restaurant
rocket
school
shop
stadium
star
suitcase
swimming
theatre
toilet
town-hall
triangle
triangle-stroked
veterinary
volcano
zoo


請參照官網 : https://plotly.com/python/mapbox-layers/
'''