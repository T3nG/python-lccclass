# pip install plotly plotly-express
# plotly 是最厲害的繪圖神器(甚至可以取代前面介紹過的所有套件), 但使用上非常不方便, 所以重新包裝其函數庫成 plotly-express
# 使用網頁顯示圖表, 所吃的資料為DataFrame格式
# DataFrame本身也可以繪圖, 但使用的是matplotlib
# 基本圖表 20種, 統計 12種, 科學 21種, 財務 2種, 地圖 8種, 3d 19種...
import plotly
import plotly_express as px
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = px.data.gapminder()

# gdp與平均壽命關係圖
chart = px.scatter(df, x='gdpPercap', y='lifeExp', color='continent',
                   size='pop', size_max=60, hover_name='country',
                   animation_frame='year', animation_group='country',
                   range_x=[10, 100000], range_y=[25, 100], log_x=True
                   )
chart.show()
