# pip install requests
# requests 就好比一個簡易的瀏覽器, 可以幫我們上網抓資料

import requests

# 台灣證券交易所
# page=requests.get("https://www.twse.com.tw/zh/page/trading/indices/MI_5MINS_HIST.html")

# 簡體網站
page=requests.get("http://www.uuxs.tw/ls/22_22102/")

# 讓網頁能夠正常顯示, 而不是回傳一堆亂碼
page.encoding="utf-8"

# 印出網頁原始碼
print(page.text)
