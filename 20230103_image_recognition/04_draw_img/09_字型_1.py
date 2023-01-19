import cv2

from sdk.IvanCv import IvanCv as cv

img = cv.read('老虎.jpg')
img = cv.resize(img, scale=0.25)

# img, 文字, 位置, 字體, 縮放比例, 顏色, 線條寬度, 線條樣式
# 線條樣式: cv2.LINE_AA 反鋸齒, cv2.LINE_8 有鋸齒
# 字型: FONT_HERSHEY_xxxx
# SIMPLEX, PLAIN, DUPLEX, COMPLEX, TRIPLE, COMPLEX_SMALL, SCRIPT_SIMPLEX, SCRIPT_COMPLEX

# 顯示的文字不支援中文
cv2.putText(img, 'tiger', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow('tiger', img)
cv2.waitKey(0)
