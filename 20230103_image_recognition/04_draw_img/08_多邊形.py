import cv2
import numpy as np

from sdk.IvanCv import IvanCv as cv
img = cv.blank(500, 500, (255, 255, 255))

# pts 為二維陣列, 紀錄每個點的座標
# True 閉合, False, 不閉合
pts = np.array([[150, 50], [250, 100], [150, 250], [50, 100]])
# cv2.polylines(img, [pts], True, (0, 255, 0), 2)
# cv.polylines(img, pts, line_width=5)
cv.fillPoly(img, pts)

cv2.imshow('test', img)
cv2.waitKey(0)
