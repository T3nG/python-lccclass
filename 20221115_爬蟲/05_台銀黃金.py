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


def getData(year, month):
    browser.get(f"https://rate.bot.com.tw/gold/chart/{year}-{month:02d}/TWD/1")
    ls = []
    try:
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        soup = BeautifulSoup(browser.page_source, "lxml")
        trs = soup.find_all("tr")
        for i in range(1, len(trs)):
            tds = trs[i].find_all("td")
            ls.append([
                tds[0].text.replace("/", "-"),
                int(tds[3].text.replace(",", "")),
                int(tds[4].text.replace(",", ""))
            ])

    except:
        print("找不到table")
    return ls


opt = Options()
# opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
opt.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=opt)

year = 2022
month = 11

conn = mysql.connect(host=G.host, user=G.user, password=G.password, database=G.dbCloud)
cursor = conn.cursor()
cmd = "insert into 台銀黃金測試 (日期, 買進, 賣出) values (%s, %s, %s)"

for m in range(1, month+1):
    datas = []
    print(f"處理{year}/{m:02d}月資料....")
    datas += getData(year, m)

    cursor.execute(f"delete from 台銀黃金測試 where 日期 like '{year}-{m:02d}%'")
    conn.commit()

    cursor.executemany(cmd, datas)
    conn.commit()
    # 一定要 sleep, 否則會被鎖 ip
    time.sleep(random.randint(5, 8)+random.random())

cursor.close()
conn.close()

