import requests
#url="http://localhost/web/99.html"
url="http://localhost/web/99.php"
page=requests.get(url)
page.encoding="utf-8"
print(page.text)

# request 碰到 javascript就死掉了, 抓不到東西
# 抓php可以抓到東西