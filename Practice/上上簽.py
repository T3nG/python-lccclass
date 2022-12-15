import os
import requests
from bs4 import BeautifulSoup

#url="https://www.sto.cx/book-211398-1.html"
url="https://www.banxia.co/50_50303/"
page=requests.get(url)
page.encoding="utf-8"
soup=BeautifulSoup(page.text,"html.parser")
content=soup.find(id="BookContent")
print(soup.prettify())

# links={}
# nodes=soup.find_all('dd')
# for node in nodes:
#     # print(link.text, link.get("href"))
#     # 單一節點中找細節
#     link=node.find('a')
#     links[link.text] =f"http://www.uuxs.tw/ls/22_22102/{link.get('href')}"
#     # key: 標題, value: 連結, 字典型態可以篩選重複的
#
# path="e:/上上簽"
# if not os.path.exists(path):
#     os.mkdir(path)
#
# import codecs
# for key in links.keys():
#     try:
#         filename=os.path.join(path, f'{key}.txt')
#         page=requests.get(links[key])
#         page.encoding="utf-8"
#         soup=BeautifulSoup(page.text,'html.parser')
#         content=soup.find(id='BookContent')
#         #file=codecs.open(filename,'w','utf-8')
#         print(f"目前正在處理{filename}...")
#         with open(filename,'w',encoding='utf-8') as file:
#             file.write(content.text)
#     except:
#         print(f'{filename}<=================error')
