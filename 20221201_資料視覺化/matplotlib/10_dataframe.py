# DataFrame 也可以進行繪圖, 但其實是調用 matplotlib 的方法, 所以最後也需用 plt.show() 顯圖

import pylab as plt
import pandas as pd

datas = [['China', 2000], ['Japan', 1300], ['Taiwan', 500], ['Korea', 800]]
df = pd.DataFrame(datas, columns=['Country', 'population'])
df.plot(kind='bar', figsize=(6, 8))
# df.plot(kind='line', figsize=(6, 8))  # plot default line

plt.show()
