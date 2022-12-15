# skewness: 偏度
from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import pylab as plt

display=pd.options.display
display.max_columns=None
display.max_rows=None
display.width=None
display.max_colwidth=None

boston_dataset = load_boston()
df=pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)
df.insert(0, column="PRICE", value=boston_dataset.target)
# lstat = df['LSTAT']
lstat = df['LSTAT']**(1/4)  # 去除異常值, 往中間偏, 若只是 1/2 偏得不太夠, 1/4時, skew為0
# 計算偏度
skew = round(lstat.skew(), 2)
# 海生圖畫出來, 發現偏左
sns.histplot(lstat, kde=True)
print(skew)
plt.show()
# skew 若為正數, 則重心往左, 右邊有零星的異常值
# skew 若為負數, 則重心往右, 左邊有零星的異常值
# skew 若為 0, 則不偏不倚

