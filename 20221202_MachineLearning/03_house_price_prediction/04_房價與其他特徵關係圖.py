import pandas as pd
import seaborn as sns
import pylab as plt
from sklearn.datasets import load_boston  # load_xxx 提供許多不同資料

display=pd.options.display
display.max_columns=None
display.max_rows=None
display.width=None
display.max_colwidth=None

boston_dataset = load_boston()
df = pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)
df.insert(0, column='PRICE', value=boston_dataset.target)
features = ['LSTAT', 'RM', 'ZN', 'PTRATIO']  # ZN, PTRATIO 與 PRICE 沒有相關, 對於預測房價沒有太大幫助
plt.figure(figsize=(20, 5))
for i, col in enumerate(features):
    plt.subplot(1, len(features), i+1)
    x = df[col]
    y = df['PRICE']
    plt.scatter(x, y)
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel('PRICE')
plt.show()
# EDA後, 還須將離群值(異常值)刪除, 填入空白值, 在此跳過
