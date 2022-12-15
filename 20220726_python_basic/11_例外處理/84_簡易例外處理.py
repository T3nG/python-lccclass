# import mysql.connector as mysql
# conn=mysql.connect(hots="localhost",
#                    password="lcc0507",
#                    database="cloud")
# cursor=conn.cursor()
# cmd=f"insert into 台灣股市 (日期,開盤,最高,最低) values ({'2022-09-29'},150,160,170,140)"
# try:
#     cursor.execute(cmd)
#     conn.commit()
# except: # Java/C# try{} catch(Exception e){}
#     print("日期重複")
# conn.close()

# C/C++並沒有例外處理
# 如果是要撰寫系統, 或是韌體(比如驅動程式), 或駭客入侵程式, 就必須使用 C/C++
# 應用程式, 就須使用 C#/Java/Kotlin/QT : 發布執行檔給客戶
# 工具 : Python

# print(10/0) # 此行出錯, 程式閃退, 下面不會執行
# print("程式要結束了喔...")


# try:
#     print(10/0)
# except:
#     print("被除數不可以為0")
# print("程式要結束了喔...")

# try:
#     print(10/0)
# except Exception as e:
#     print(e)
# print("程式要結束了喔...")

# try:
#     print(10/0)
# except Exception as e:
#     if str(e)=="division by zero":
#         print("被除數為0")
#     else:
#         print("不明錯誤")
# print("程式要結束了喔...")

# pip install requests

# 從url下載圖片到目錄, 只有一張的話還好, 百萬張呢?
import time
from urllib.error import URLError

import requests
from requests import HTTPError


# 通常用執行緒去跑這種無窮迴圈, 發生錯誤後, 幾秒後可再繼續執行
# 比如一次下載好多圖片, 若只有一張出錯, 比如網路出錯等等, 程式不會整個結束, 而是等待幾秒後再繼續執行
while(True):
    # print(10/0)
    # 老師的經驗
    # 從google提供的地址資料發現錯誤, 要存成檔名的時候有特殊字元
    try:
        for i in range(100):
            address="台北市內湖區$瑞光路10號.jpg".replace("$","").replace("@","") # ... 或正規表示法去做
            page = requests.get("http://mahaljsp.asuscomm.com/wp-content/uploads/2016/10/img_6279.jpg")
            with open('tiger.jpg','wb') as f: # wb以二進位寫入
                f.write(page.content)
    except HTTPError as e:
        time.sleep(5)
        print("網路斷線")
    except URLError as e:
        time.sleep(5)
        print("網址錯誤")
    except Exception as e:
        time.sleep(5)
        print(f"其他錯誤: {e}")

# 不要執行 just as an example not meant to run