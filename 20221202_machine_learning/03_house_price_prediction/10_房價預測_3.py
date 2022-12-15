import pandas as pd
import numpy as np
import seaborn as sns
import pylab as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor as LOF


display=pd.options.display
display.max_columns=None
display.max_rows=None
display.width=None
display.max_colwidth=None

boston_dataset = load_boston()
df = pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)
df.insert(0, column='PRICE', value=boston_dataset.target)
df = df[['PRICE', 'LSTAT', 'RM']]  # 只印出需要的欄位
# 準備資料
x = df[['LSTAT' ,'RM']]
y = df['PRICE']
# 離群分析, 周遭20點, 噪音值0.1
lof = LOF(n_neighbors=20, contamination=0.1)
y_pred = lof.fit_predict(np.c_[x, y])
# print(y_pred.shape)  # 總筆數
# print(y_pred)  # -1即離群值的位置
# loc 列, iloc 儲存格, 把 1 的資料放進新的df
df = pd.DataFrame(data=df.loc[np.where(y_pred==1)].values, columns=['PRICE', 'LSTAT', 'RM'])
# 偏度校正, 負相關可以處理偏度校正, 但正相關就不要處理, 免得跟原始資料脫節
data = np.c_[df['LSTAT']**(1/3), df['RM']]
x = pd.DataFrame(data=data, columns=['LSTAT', 'RM'])
# x = df[['LSTAT', 'RM']]  # 若不處理偏度校正可以這樣寫
y = df['PRICE']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)
# 世上的模型千萬種, 哪有可能每一種都了解, 把模型當成是一個黑盒子即可
model = LinearRegression()
model.fit(x_train, y_train)  # fit 強迫求出迴歸線

y_pred = model.predict(x_test)
for i in zip(y_pred, y_test):
    print(i)
print(f'分數: {model.score(x_test, y_test)}')