import plotly_express as px
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = px.data.gapminder()

df = df[df['continent'] == 'Asia']

# chart = px.box(
#     df,
#     x='year',
#     y='lifeExp',
#     title='亞洲歷年壽命'
# )

chart = px.violin(
    df,
    x='year',
    y='lifeExp',
    title='亞洲歷年壽命'
)
chart.show()
