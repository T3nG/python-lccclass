# pip install plotly-express 是超強的繪圖神器

import pylab as plt
import pandas as pd
import plotly_express as px
# df的scatter必須指定x ,y的值
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = px.data.gapminder().query('year==2007')

# 依 lifeExp 產生不同顏色值, cmap
df.plot(kind='scatter', x='gdpPercap', y='lifeExp', cmap=plt.get_cmap('rainbow'), c='lifeExp')

plt.show()
