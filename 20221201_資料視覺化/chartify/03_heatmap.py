import chartify
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df_o = pd.read_excel('E:\\project\\data\\歷年來台旅客國籍統計2002-2021_total.xlsx')
index = 0
df_n = pd.DataFrame(columns=['area', 'year', 'qty'])
# 轉成流水帳
for i in range(df_o.shape[0]):
    for j in range(2, df_o.shape[1]):
        df_n.loc[index] = [df_o.iloc[i, 0], str(df_o.columns[j]), int(df_o.iloc[i, j])]
        index += 1
ch = chartify.Chart(x_axis_type='categorical', y_axis_type='categorical')
ch.plot.heatmap(
    data_frame=df_n,
    y_column='year',
    x_column='area',
    text_column='qty',
    color_column='qty',
    color_palette='Reds',
    text_format='{:,.0f}'
)
ch.show()
