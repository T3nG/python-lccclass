import os
from datetime import datetime

# while(True): # (視窗程式的idle, while只是placeholder, don't run as iS)
#     try:
#         pass
#         # 專案內容
#     except Exception as e:
#         with open("log.txt","a") as f: # a: append
#             d=datetime.datetime.now()
#             f.write(f"{str(d)}:{e}") # 發生錯誤的時間與訊息
#
# # 寫專案的時候這樣寫, 方便除錯


# 無論有沒有錯誤, finally 都會被執行
# 甚至下達exit() , 死之前都要先執行finally
# try:
#     x=10
#     y=0
#     print(x/y)
#     exit()
# except Exception as e:
#     print(f"error:{e}")
#     exit()
# finally:
#     print("finally區塊")

# 應用

# locals().keys() 包含
# '__name__', '__doc__', '__package__', '__loader__', '__spec__',
# '__annotations__', '__builtins__', '__file__', '__cached__',
# 'os', 'datetime', 'file'

# try:
#     # 檔案錯誤時出問題
#     file=open('e:/test.txt','r',encoding='utf-8')
#     print(locals().keys())
#     line=file.read()
#     print(line)
# except Exception as e:
#     print(f"發生錯誤:{e}")
# finally:
#     if 'file' in locals().keys(): # 如果檔案有開起來, 才關閉
#         file.close()
#     print("檔案已關閉")
# 這種寫法很煩人, 在Java6.0必須得這麼寫

# 底下類似java的try-catch-resource (Java7.0才支援)

# 開啟檔案時的正確寫法
try:
    with open("e:/testt.txt",'r',encoding='utf-8') as file:
        line=file.read()
        print(line)
        # 離開 with區塊前, 會自動幫我們close()
except FileNotFoundError as e: # 沒有此檔案時
    print(e)
except IOError as e: # 硬碟壞掉時
    print(e)

# 此時finally就不需要了, 因為自動幫我們close()了