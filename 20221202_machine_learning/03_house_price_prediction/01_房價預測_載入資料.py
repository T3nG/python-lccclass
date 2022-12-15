# http://mahaljsp.asuscomm.com/index.php/2022/10/08/%e6%b3%a2%e5%a3%ab%e9%a0%93%e6%88%bf%e5%83%b9%e9%a0%90%e6%b8%ac/
# 波士頓房價預測
# pip install scikit-learn matplotlib seaborn
# scikit-learn 是學習機器學習時, 常用的入門套件
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html
# 基礎統計學
# http://mahaljsp.asuscomm.com/index.php/2022/10/09/%e5%a4%a7%e6%95%b8%e6%93%9a%e5%88%86%e6%9e%90/
# load_boston() 未來無法使用
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
# 將售價插入df最前面
df.insert(0, column='PRICE', value=boston_dataset.target)
print(df)

# EDA(Explorator Data Analysis) 資料探索分析

# sns.histplot(df['PRICE'], kde=True)  # kde 顯示迴歸線
# 整個圖形往右偏, 會影響我們的預測, 愈偏右(或左), 影響愈大
# 貧富差距愈大, 國人的平均所得就愈差愈大
# 台積電: 年薪  70萬, 80%
#        年薪 200萬,  5%
# 所以要將異常值去除, 把中心點往圖的中間偏, 可以提高預測值

# 皮爾森積差: 計算每一個特徵跟其他特徵的相關性, 愈接近 0愈不相關, 愈接進 1 或 -1 相關性愈大(正相關, 負相關)
corrmat = df.corr()
# 排序, 依最大值
corrmat = corrmat.nlargest(len(corrmat), columns='PRICE')
sns.heatmap(corrmat, annot=True, annot_kws={'size': 6}, fmt='.2f')
plt.show()

# 列出有多少資料
# print(boston_dataset.data.shape)

# 售價, 美金?/平方英呎? per square foot
# print(boston_dataset.target)

# 描述欄位資料, 見以下註解區
# print(boston_dataset.DESCR)
'''
Number of Instances: 506 

Number of Attributes: 13 numeric/categorical predictive. Median Value (attribute 14) is usually the target.

Attribute Information (in order):
    - CRIM     per capita crime rate by town
    - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
    - INDUS    proportion of non-retail business acres per town
    - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
    - NOX      nitric oxides concentration (parts per 10 million)
    - RM       average number of rooms per dwelling
    - AGE      proportion of owner-occupied units built prior to 1940
    - DIS      weighted distances to five Boston employment centres
    - RAD      index of accessibility to radial highways
    - TAX      full-value property-tax rate per $10,000
    - PTRATIO  pupil-teacher ratio by town
    - B        1000(Bk - 0.63)^2 where Bk is the proportion of black people by town
    - LSTAT    % lower status of the population
    - MEDV     Median value of owner-occupied homes in $1000's
'''