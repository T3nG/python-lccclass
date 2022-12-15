# 24節氣, 是地球繞太陽的公轉軌道, 不是農民曆
#每19年, 國曆跟農曆會同一天
#一甲子為60年, 為什麼不是120年 沒有甲丑年等

from datetime import datetime
sky=["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
land=["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
animal=["鼠","牛","虎","兔","龍","蛇","馬","羊","猴","雞","狗","豬"]
# print(datetime.now()) #取得目前系統時間
# print(datetime.now().year)
# print(datetime.now().month)
# print(datetime.now().day)
# print(datetime.now().hour)
# print(datetime.now().minute)
# print(datetime.now().second)
# 3d : 3位數, 不足三位以空格填入

yyy=datetime.now().year-1911 # 民國年
print(f"目前為民國{yyy}年")
first=13 #民國13年為甲子年
for i in range(150):
    year=first+i
    if year<=yyy: #判斷歲數
        print(f"民國{year:3d}年 : {sky[i%10]}{land[i%12]} : {animal[i%12]} : {yyy-year+1}歲") #每10個/每12個一循環, +1歲 虛歲
    else:
        print(f"民國{year:3d}年 : {sky[i % 10]}{land[i % 12]} : {animal[i % 12]}")
# 有人說, 學過八字的人, 土地公都會造冊登記