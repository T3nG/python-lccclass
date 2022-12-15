from selenium import webdriver
from bs4 import BeautifulSoup
import os

### webdriver 啟動, 進到輸入頁面 ###
driver=webdriver.Chrome("E:/ChromeDriver/chromedriver.exe")
url="https://www.sto.cx/book-211398-1.html"
driver.get(url)

### 取得輸入頁面的資料以利爬蟲 ###
soup=BeautifulSoup(driver.page_source,"lxml")
content=soup.find(id='BookContent')

### 取得其他頁面的網址 ###
options=soup.find_all('option')
d={}
for option in options :
    d[option.text]=f"https://www.sto.cx/{option['value']}"

### 建立存檔目錄 ###
path="e:/上上簽"
if not os.path.exists(path):
    os.mkdir(path)

### 爬蟲/依每個頁面讀寫入檔案  ###
for key in d.keys():
    try:
        filename=os.path.join(path, f'{key}.txt')
        driver.get(d[key])
        sp=BeautifulSoup(driver.page_source,"lxml")
        ct=sp.find(id='BookContent')
        wordlist = ct.text.strip().split()
        singleStr = '\n\n'.join(wordlist)
        #file=codecs.open(filename,'w','utf-8')
        print(f"目前正在處理{filename}...")
        with open(filename,'w',encoding='utf-8') as file:
            file.write(singleStr)
    except:
        print(f'{filename}<=================error')

### 將所有文字檔寫入單一檔案 ###
fileCount=len(os.listdir(path))
for txt in range(fileCount):
    with open(os.path.join(path,f"{txt+1}.txt"), encoding="utf-8") as f:
        s=''.join(f.read())
    with open(os.path.join(path, "上上簽.txt"),'a',encoding="utf-8") as fa:
        fa.write(s)
#filename=os.path.join(path, f'{key}.txt')