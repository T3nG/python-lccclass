# pip install matplotlib
import pylab as plt  # import matplotlib.pylab as plt
import numpy as np
# x = [1, 2, 3, 4, 5]
x = np.linspace(0, 10, 11)  # 0~9 分 11 等分
y = [10, 15, 35, 5, 18]
y = np.random.randint(10, 30, 11)

plt.figure(figsize=(20,50))  # 設定畫布大小, 若數值差異過大, 會因空間壓縮而比例失真, 調整畫布大小來解決

# 設定x軸, Y軸, 初值, 尾值
plt.xlim(1, 20)
plt.ylim(1, 50)

# 點散圖, s=設定點的大小, color='r' '#ff0000' 設定點的顏色
# plt.scatter(x ,y, s=250, color='r')

# 折線圖
# plt.plot(x ,y)

# plot畫點散圖, r: 紅色, k: 黑色 o: 圓形, ^:三角形, s:四方形, markersize=設定點點大小
plt.plot(x, y, 'ro', markersize=10)

plt.show()
