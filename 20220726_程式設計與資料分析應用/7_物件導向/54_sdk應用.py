
# from 目錄.檔案名 import 類別名稱
from sdk.ChrisSdk import ChrisSdk
from sdk.ChrisSdk import MathSdk
print(ChrisSdk.triangle(3,4))

# 往後要應用各種專案時, 直接把自己的sdk抓進來就可以使用

# 使用sdk中的函數庫
from sdk.ChrisSdk import triangle
from sdk.ChrisSdk import tp # 每要使用一個函數就要 import
from sdk.ChrisSdk import *  # 但若函數太多可能造成執行緩慢

print(triangle(3,4))