import pandas as pd
import numpy as np
import seaborn as sns
import pylab as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

display=pd.options.display
display.max_columns=None
display.max_rows=None
display.width=None
display.max_colwidth=None

boston_dataset = load_boston()
df = pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)
df.insert(0, column='PRICE', value=boston_dataset.target)
# 負相關的要開根號提高準確度(拉回偏度), 正相關的(房間數愈多愈貴, 要平方立方, 加大偏度)
data = np.c_[df['LSTAT']**(1/5), df['RM']]**5
x = pd.DataFrame(data=data, columns=['LSTAT', 'RM'])
y = df['PRICE']
# 80%訓練, 20%測試準確度
# test_size=0.2 20%用來測試, random_state=5, random seed不是固定的那幾個20%,
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)
# 線性回歸模型
model = LinearRegression()
# 將兩個特徵放入模型訓練
model.fit(x_train, y_train)
# 儲存訓練好的模型, 但此模型 LinearRegression() 不提供
# model.save()
# 執行, 若資料量太大, 會跑很久, 甚至好幾天, 目前在此範例一瞬間就跑完了
# 模型分數, 愈接近1, 表示預測愈準確
print(f'分數: {model.score(x_test, y_test)}')
# 預測值與實際值做比較
y_pred = model.predict(x_test)
# for i in zip(y_pred, y_test):
#     print(i[0]-i[1])

# 未修正前分數: 0.6628996975186952
# LSTAT ^1/3: 分數: 0.7130425972530741
# LSTAT ^1/4: 分數: 0.7179997327261858
# LSTAT ^1/4: 分數: 0.7207128450681075
# LSTAT ^1/5 , RM**3: 分數: 0.7509717952292749
# LSTAT ^1/5 , RM**5: 分數: 0.7622439485013246