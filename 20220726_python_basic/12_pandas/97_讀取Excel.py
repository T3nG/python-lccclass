import pandas as pd
df=pd.read_excel("台灣股市.xlsx", sheet_name='資料表')
print(df)

# C# 亦可以讀取及寫入Excel
# Microsoft Interop Excel 套件, 效能極差, 且沒有安裝Excel就無法寫入讀取
# NPOI : 第三方套件, 效能極高, 直接寫入Excel格式, 不需要安裝Excel

