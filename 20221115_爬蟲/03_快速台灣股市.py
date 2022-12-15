
# https://www.twse.com.tw/zh/page/trading/indices/MI_5MINS_HIST.html 原始網址
# https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date=20221101
# &date=20221101 控制這邊的日期即可
import json
import random
import time
import requests
import mysql.connector as mysql
from G import G



def getStock(year, month):
    url = f"https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date={year:4d}{month:02d}01"
    page = requests.get(url)
    rows = json.loads(page.text)['data']
    ls = []
    for row in rows:
        ds = row[0].split("/")
        ls += [[f'{int(ds[0])+1911}/{ds[1]}/{ds[2]}',
               float(row[1].replace(",","")),
               float(row[2].replace(",", "")),
               float(row[3].replace(",", "")),
               float(row[4].replace(",", ""))
               ]]
    return ls



year = 2022
month = 12

conn = mysql.connect(host=G.host, user=G.user, password=G.password, database=G.dbCloud)
cursor = conn.cursor()
cmd = "insert into 台灣股市測試 (日期, 開盤, 最高, 最低, 收盤) values (%s, %s, %s, %s, %s)"

for m in range(1, month):
    datas = []
    print(f"處理{year}/{m:02d}月資料....")
    datas += getStock(year, m)

    cursor.execute(f"delete from 台灣股市測試 where 日期 like '{year}-{m:02d}%'")
    conn.commit()

    cursor.executemany(cmd, datas)
    conn.commit()
    # 一定要 sleep, 否則會被鎖 ip
    time.sleep(random.randint(5, 8)+random.random())

cursor.close()
conn.close()