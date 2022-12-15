# pip install xlrd openpyxl
# 長條圖, 圓餅圖目前沒有 3D的功能, 日後可能也不會有
import plotly.graph_objects as go
import plotly
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv',
    dtype='float')
print(df)
trace = go.Surface(z=df.values)
data = [trace]

layout = go.Layout(
    title='地形圖',
    margin=dict(l=50, r=50, b=50, t=50)  # 上下左右的間隔(離邊界)
)

fig = go.Figure(data=data, layout=layout)

# Layout 看要在前面加或後面加
# fig.update_layout()

fig.show()
