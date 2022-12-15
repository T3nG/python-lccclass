import mysql.connector as mysql
import requests, json # 讀音 jason

url = "http://localhost/web/login_post.php"
account = "asus"
password = "1234"
# 底下是使用 GET 的方式
# 不安全, 會員帳密都顯示在網址列了
# params = f"{url}?account={account}&password={password}"
# page = requests.get(params)
# print(page.text)

# 底下是使用 POST 的方式
# 記得 php 要改成 $_POST["account] , $_POST["password]
params = {"account":account, "password":password}
page = requests.post(url, params)
print(page.text)

# 轉成 Python字典格式
dbInfo = json.loads(page.text)
print(dbInfo)
dbAccount = dbInfo["dbAccount"]
dbPassword = dbInfo["dbPassword"]

# 資料庫存取
conn = mysql.connect(host="localhost", user=dbAccount, password=dbPassword, database="cloud")
cursor = conn.cursor()
cursor.execute("select * from 會員資料表")
rs = cursor.fetchall()
for r in rs:
    print(r)