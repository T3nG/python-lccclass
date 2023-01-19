import cv2
import numpy as np

from sdk.IvanCv import IvanCv as cv
img = cv.blank(500, 300, (0, 255, 255))
# cv.line(img, (0, 0), (0, 300), (0, 0, 255), 1)
# cv.line(img, (100, 0), (100, 300), (0, 0, 255), 1)
# cv.line(img, (200, 0), (200, 300), (0, 0, 255), 1)

n = 50
x = np.arange(0, 500, n)
y = np.arange(0, 300, n)
for i in range(len(x)):
    cv.line(img, p1=(int(x[i]), 0), p2=(int(x[i]), 300), color=(0, 0, 255), line_width=1)
for i in range(len(y)):
    cv.line(img, p1=(0, int(y[i])), p2=(500, int(y[i])), color=(0, 0, 255), line_width=1)

cv2.imshow('test', img)
cv2.waitKey(0)
