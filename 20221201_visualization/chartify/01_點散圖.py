# chartify: 專門用來處理流水帳的統計套件, 使用html(javascript)繪製圖表
# pip install chartify pandas

import chartify
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# 範例資料
df = chartify.examples.example_data()
# 產生一個圖表
ch = chartify.Chart(blank_labels=True)  # blank_labels=True, 取消標籤顯示
ch.set_title('各國水果價格')
ch.axes.set_xaxis_label('單價')
ch.axes.set_yaxis_label('總價')
ch.plot.scatter(data_frame=df, x_column='unit_price', y_column='total_price')
ch.show()

print(df)
