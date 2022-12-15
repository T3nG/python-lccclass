import plotly
import plotly_express as px
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = px.data.gapminder()

# 使用地圖顯示人口數
chart = px.choropleth(df,
                      locations='iso_alpha',
                      color_continuous_scale=px.colors.sequential.Plasma,
                      color='lifeExp',
                      animation_frame='year',
                      projection='natural earth'
                   )
chart.show()
