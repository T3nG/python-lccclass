import pylab as plt
import numpy as np

x = np.linspace(1, 12, 12)  # 1~12月
# y = np.random.randint(1, 20, 12)  # 模擬不良率
rates = [5, 15, 12, 13, 6, 8, 12, 10, 20, 13, 10, 6]
# 設計不同顏色, 比如依月份而有不同顏色, 或以數值大小, 值域範圍來區分, 依設計好的順序加入 colors
colors = []
for rate in rates:
    if rate <= 5:
        colors.append('green')
    elif rate <= 10:
        colors.append('yellow')
    else:
        colors.append('red')

plt.bar(x, rates, color=colors, width=0.8)
# 只要設定字型就可以顯示正常, 字型可更改, 只要有安裝都可以, windows/fonts
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.xlabel('月份', fontsize=14)
plt.ylabel('不良率', fontsize=14)
plt.title('2022產品不良率統計', fontsize=20)
plt.show()
