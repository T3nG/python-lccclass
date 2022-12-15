import pandas as pd

# pandas 跟 numpy 一樣, 都有很多東西還沒講, 跟AI深度學習有關

idx=['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune','pluto']
planets={'mercury':'水星','venus':'金星','earth':'地球','mars':'火星','jupiter':'木星','saturn':'土星','uranus':'天王星','neptune':'海王星','pluto':'冥王星'}

solor=pd.Series(planets) # data可加可不加
# solor=pd.Series(data=planets)
print(solor['earth'])

print(solor[2])
# 字典透過pd.Series轉換, 索引也可找到data


