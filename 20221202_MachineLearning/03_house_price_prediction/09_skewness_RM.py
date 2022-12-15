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
rm = df['RM']**0.4
print(rm.skew())
sns.histplot(rm, kde=True)
plt.show()
