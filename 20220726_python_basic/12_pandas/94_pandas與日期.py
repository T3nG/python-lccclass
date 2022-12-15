import pandas as pd
from datetime import timedelta
from datetime import datetime # 為導入datetime.py 裡的 datetime函數
import time
#import datetime # 為導入 datetime.py


dates=pd.date_range('2022/2/20', periods=20)
# 從指定的日期開始, 往後數幾天
#print(dates)

t1=time.time()
print(f'{t1:,}秒')
# 取得目前的系統時間 : 以 TimeStamp秒數為單位, 後面有小數, 代表ms
# TimeStamp : 時間截記, 自1970/01/01 00:00:00 到現在所經歷過的秒數

a=(2022-1970)*365*86400+(9*30*86400)
print(f'{a:,}秒\n')
# 真的是從 1970/01/01開始嗎? 粗算如上

d1=datetime.now()
print(f'目前時間, 格式為 datatime: \n{d1}\n')
print(f"轉成字串, 年-月-日  \n{d1.strftime('%Y-%m-%d')}\n")
print(f"轉成字串, 時:分:秒 \n{d1.strftime('%H:%M:%S')}\n")

d2=datetime(1970,1,1)
print(d2)

diff=d1-d2
print(diff.days*86400)
print()
# 二時間相減, 會產生 timedelta格式

d3=datetime(2022,1,1)
d=d1-d3
print((d.days+6)%7) # 1月1日星期6, 除7的餘數=> 可以得知今天星期幾, 0代表星期日
print()

print(f"今天是星期: {d1.strftime('%w')}")
print(f"今天是今年第幾週: {d1.strftime('%W')}")
print()

# 2022-01-01 是第二條路線, 今天要跑哪一條? 每四天循環(四條路線)
d=d1-d3
print(f"今天要跑: {(d.days+2)%4}路線")
print()

# 往後幾天
d4=d1+timedelta(days=10)
print(d4)

# 往前幾天
d5=d1+timedelta(days=-2)
# d5=d1-timedelta(days=2)
print(d5)
print()

'''
常用的幾個使用時間的方式
x=pd.date_range('2022/2/20', periods=20)
    從指定的日期開始, 往後數幾天
x=time.time()
    目前系統時間, TimeStamp秒 (從1970-01-01 00:00:00 開始的秒數)
x=datetime.now()
    目前時間, datetime格式, 得轉成字串才能正確印出來
    x.strftime('%Y-%m-%d %H:%M:%S')
x=datetime(1970,1,1)
    指定日期, datetime格式
'''
import numpy as np

d1=datetime.now().strftime('%Y-%m-%d')
days=pd.date_range(d1,periods=10)
df=pd.DataFrame(np.random.randn(10,4), index=days, columns=['香蕉','蘋果','芒果','柳丁'])
# randn 以常態分佈產生的亂數, 置中為 0
print(df)
# 為每日產生亂數值
