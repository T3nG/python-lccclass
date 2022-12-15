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

df = px.data.gapminder().query('year==2007')
print(df)

# 互動示圖表, 鼠標移到點上會顯示資料
# facet: 分類依據, col: 直行式呈現
chart = px.scatter(df, x='gdpPercap', y='lifeExp', color='continent',
                   hover_name='country', size='pop', size_max=60,
                   facet_col='continent')
chart.show()
# 存檔, show()是新版才有的, 舊版只能用offline秀圖
plotly.offline.plot(chart, filename='sample.html', auto_open=False)


