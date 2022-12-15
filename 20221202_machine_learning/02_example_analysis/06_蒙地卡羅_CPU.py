# http://mahaljsp.asuscomm.com/index.php/2022/11/10/%e8%92%99%e5%9c%b0%e5%8d%a1%e7%be%85%e6%b3%95/
# Monte Carlo method: 統計類比方法, 是屬於強迫求解的一種方法
# # 強迫求解, 用python迴圈
# sum = 0
# for i in range(1, 101):
#     sum += i
# print('1+2+3+4+...+100 = ', sum)

# 請用最快速的方法計算 1+2+3+...+100
# # print((1+100)*100/2)
# 因為知道公式才能使用的方法

import numpy as np
import time

# 一次要塞多少個點
batch = 100_000_000
# 世代, 要執行幾次
epoch = 100
# 為什麼要分成兩階段? 怕記憶體不足, batch * epoch 愈大, pi值愈準確
t1 = time.time()
incircle = 0
for e in range(epoch):
    # points = [(x1, x2,...), (y1, y2,...)], 0~1 的範圍可以精準控制, 範圍若加大, 撒下去的點要更多才會精準
    points = [np.random.uniform(0, 1, batch), np.random.uniform(0, 1, batch)]
    # dist = (x^2 + y^2)^(1/2)  亂數點到原點的距離
    dist = np.sqrt(np.square(points[0]) + np.square(points[1]))
    # shape[0]: 因為where找出來的第0項是陣列, 意義等同 len()
    incircle += np.where(dist < 1)[0].shape[0]
    # pi = area * 4, area = pi * r^2 / 4 為什麼是四分之一圓? 因為產生的x, y點是落在第一象限, 以及上述原因
    pi = incircle / ((e+1)*batch) * 4
    print(f'\rEpoch: {e+1:03d}, pi={pi}', end='')
t2 = time.time()
print(f'\n耗時: {t2 - t1}秒')
