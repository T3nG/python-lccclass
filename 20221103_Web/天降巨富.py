
import os
import requests
url="http://www.uuxs.tw/ls/22_22102/"
page=requests.get(url)
page.encoding="utf-8"
#print(page.text)

# pip install BeautifulSoup4 / lxml 美麗的湯, 解析html的工具, 比elementtree更適合爬蟲來用

from bs4 import BeautifulSoup

# html.parser 使用 lxml工具轉換成 html
soup=BeautifulSoup(page.text,"html.parser")

# prettify() 印出具有內縮的格式
#print(soup.prettify())

# 列出body內的所有字串, 非字串則印出空白
# for l in soup.body.strings:
#     print(l)

# # soup.a.string / soup.a.text 找到第一個 tag為 <a> 的節點
# #node=soup.a.string
# node=soup.li
# print("node.text", node.text)

'''
打開網頁原始碼交叉比對是否有找到想要的節點
這個範例網頁沒有head, 是撰寫網站者的問題, bug
常用找節點的
soup.title
soup.a
soup.li
soup.body
soup.head
'''
'''
<a href="xxx.html">第一章</a>
link=node.find('a') 
link.get("href")    => xxx.html
link.text           => 第一章

'''

# find('a', href='url') 找一個
# find_all('a') 找所有符合的節點
# node=soup.find('a', href='8233492.html')

# <dd><a href="8233492.html" title="第一章 飞龙岂是池中物">第一章 飞龙岂是池中物</a></dd>
# 取得屬性要使用get =>link.get("title")
# 寫title沒什麼作用, 只是方便爬蟲而已
# 文章名稱 link.text

links={}
nodes=soup.find_all('dd')
for node in nodes:
    # print(link.text, link.get("href"))
    # 單一節點中找細節
    link=node.find('a')
    links[link.text] =f"http://www.uuxs.tw/ls/22_22102/{link.get('href')}"
    # key: 標題, value: 連結, 字典型態可以篩選重複的

path="e:/天降巨富"
if not os.path.exists(path):
    os.mkdir(path)

import codecs
for key in links.keys():
    try:
        filename=os.path.join(path, f'{key}.txt')
        page=requests.get(links[key])
        page.encoding="utf-8"
        soup=BeautifulSoup(page.text,'html.parser')
        content=soup.find(id='content')
        #file=codecs.open(filename,'w','utf-8')
        print(f"目前正在處理{filename}...")
        with open(filename,'w',encoding='utf-8') as file:
            file.write(content.text)
    except:
        print(f'{filename}<=================error')
        # 不會中斷爬蟲, 會顯示出哪一筆資料出問題(若有出問題的話)
        # 為防止爬資料的時候出現各種奇葩錯誤, 網路異常等
        # 加入 try except



'''
為什麼href="8882.html"? 
只給最後面的數字呢?
必免日後網址更新時, 需更改大量程式碼
wordpress會參考自己網站內的照片以 img src 新增圖片時, 先上傳到wordpress的媒體庫, 
將圖片網址複製下來後, 網址最前面不需要寫cosmowhale.asuscomm.com
'''