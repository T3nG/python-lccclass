import cv2
import numpy as np
import pylab as plt
from sdk.IvanCv import IvanCv as cv
img_path = 'E:\project\data\img\jpg\\road.jpg'
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

img = cv.read(img_path)
img = img[:, :, ::-1]
plt.subplot(2, 3, 1)
plt.axis('off')
plt.title('原圖 original')
plt.imshow(img)

# Sobel Gray 索伯及蓋瑞
# 得先轉成灰階, 再適度高斯模糊
# kernel為 [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5),0)  # 愈模糊邊緣線愈不明顯, 但每張圖有不同結果
# 低門檻值, 高門檻值, 建議調 1:2 或 1:3, 自行調配
canny = cv2.Canny(blurred, 30, 150)  # 低於多少變0, 高於多少變255
plt.subplot(2, 3, 2)
plt.axis('off')
plt.title('邊緣')
plt.imshow(canny, cmap='gray')

# road.jpg
# 偵測車道線, 用於自動駕駛訓練

plt.show()
