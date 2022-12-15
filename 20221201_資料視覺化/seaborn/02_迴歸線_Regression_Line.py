import pandas as pd
import seaborn as sns
import pylab as plt
import numpy as np

x = np.random.randint(1, 1000, 1000)
y = np.random.randint(1, 1000, 1000)

# 畫回歸線必須要用dataframe
df = pd.DataFrame({'x': x, 'y': y})

# fig_reg決定是否顯示迴歸線
sns.lmplot(x='x', y='y', data=df, height=6, fit_reg=True)
plt.show()
