# pip install openpyxl xlrd

import chartify
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df_o = pd.read_excel('E:\\project\\data\\歷年來台旅客國籍統計2002-2021_total.xlsx')
print(df_o)
# 將樞紐分析表格式轉成流水帳
# loc[x]: 第x列
# iloc[x, y]: 儲存格
# df_o.shape[0]: 共幾列
# df_o.shape[1]: 共幾行
index = 0
df_n = pd.DataFrame(columns=['area', 'year', 'qty'])
for i in range(df_o.shape[0]): # 列
    for j in range(2, df_o.shape[1]):
        df_n.loc[index] = [df_o.iloc[i, 0], str(df_o.columns[j]), int(df_o.iloc[i, j])]
        index += 1
print(df_n)

# 堆積圖?
# ch = chartify.Chart(x_axis_type='datetime')
# ch.plot.area(data_frame=df_n, x_column='year', y_column='qty', color_column='area', stacked=True)

# 比例圖
ch = chartify.Chart(x_axis_type='categorical')
# 橫向
# ch = chartify.Chart(y_axis_type='categorical')
ch.plot.bar_stacked(data_frame=df_n, categorical_columns='year',
                    stack_column='area', numeric_column='qty',
                    normalize=True)
ch.set_legend_location('outside_bottom')
ch.show()
