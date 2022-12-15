import plotly_express as px
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = px.data.gapminder()

df = df[df['iso_alpha'] == 'TWN']
print(df)

chart = px.bar(
    df,
    x='year',
    y='pop',
    title='台灣歷年來人口數',
)
chart.show()