# http://mahaljsp.asuscomm.com/index.php/2019/10/08/python_seaborn/
# seaborn海生圖, 就是在海量的資料中, 進行統計分析, 畫出一張有用的圖
# pip install seaborn matplotlib
# matplotlib 3.5.2閃退, 請用其他版本
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# normal 常態分布
sample = np.random.normal(size=1000000)
sns.set_style('whitegrid')
plt.subplot(2, 2, 1)
sns.histplot(sample)

sns.set_style('ticks')
plt.subplot(2, 2, 2)
# kde: kernel density estimation (核心密度評估)
sns.histplot(sample, kde=True)

sns.set_style('darkgrid')
plt.subplot(2, 2, 3)
sns.histplot(sample)

plt.show()
