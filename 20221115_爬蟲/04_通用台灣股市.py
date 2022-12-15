import random
import time

import mysql.connector as mysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup  # pip install BeautifulSoup4 / lxml
from G import G


def getStock(year, month):
    Select(browser.find_element(By.NAME, "yy")).select_by_value(str(year))
    Select(browser.find_element(By.NAME, "mm")).select_by_value(str(month))
    browser.find_element(By.CLASS_NAME, "button").click()
    try:
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.TAG_NAME, "td")))
        soup = BeautifulSoup(browser.page_source, "lxml")
        trs = soup.find_all("tr", role='row')
        ls = []
        for i in range(1, len(trs)):
            tds = trs[i].find_all("td")
            ds = tds[0].text.split("/")
            ls.append([f'{int(ds[0])+1911}-{ds[1]}-{ds[2]}',
                        float(tds[1].text.replace(",","")),
                        float(tds[2].text.replace(",", "")),
                        float(tds[3].text.replace(",", "")),
                        float(tds[4].text.replace(",", ""))
                        ])
    except:
        pass
    return ls
opt = Options()
# opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
opt.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=opt)

browser.get("https://www.twse.com.tw/zh/page/trading/indices/MI_5MINS_HIST.html")

year = 2022
month = 3
datas = []

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