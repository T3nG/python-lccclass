# pip install pandas
import pylab as plt
import numpy as np
import pandas as pd

datas = [['China', 2000], ['Japan', 1300], ['Taiwan', 500], ['Korea', 800]]
df = pd.DataFrame(datas, columns=['Country', 'population'])
plt.pie(df['population'], labels=df['Country'], autopct='%0.2f%%')  # 2個小數點
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.title('2022各國中標人數', fontsize=20)
plt.show()
