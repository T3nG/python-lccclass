import cv2
import numpy as np

from sdk.IvanCv import IvanCv as cv
img = cv.blank(500, 500)

# img, 中心點座標, 半徑, 顏色值, 線條寬度
# cv2.circle(img, (250, 250), 100, (0, 255, 0), 2)
cv.circle(img, (250, 250), 100, line_width=-1)


# 圓的演算法, 禁止在 python使用, 因為用迴圈寫
# r = 150
# # 0, 360, 4 三角形, 5 菱形, 6 五邊形, ...
# a = np.linspace(0, 360, 6)
# # a = np.linspace(0, 360, 720)
# y = r * np.cos(a * np.pi / 180) + 250
# x = r * np.sin(a * np.pi / 180) + 250
# for i in range(len(x)-1):
#     cv.line(img, p1=(int(x[i]), int(y[i])), p2=(int(x[i+1]), int(y[i+1])), color=(0, 255, 0), line_width=5)

cv2.imshow('test', img)
cv2.waitKey(0)
