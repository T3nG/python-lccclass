import cv2

from sdk.IvanCv import IvanCv as cv
img = cv.blank(500, 300, (0, 255, 255))

# img, 左上, 右下, 顏色, 線條樣式or線條寬度, 寬度= -1 時, 劃出實心矩形
# 樣式比如 cv2.LINE_AA
# cv2.rectangle(img, (77, 77), (400, 100), (0, 0, 255), -1)
cv.rectangle(img, (50, 50), (450, 250), (0, 0, 255), -1)

cv2.imshow('test', img)
cv2.waitKey(0)
