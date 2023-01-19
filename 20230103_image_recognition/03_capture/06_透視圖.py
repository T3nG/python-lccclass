import numpy as np

from sdk.IvanCv import IvanCv as cv
from sdk.IvanCv import Direction
import cv2

img = cv.read('老虎.jpg')
img = cv.resize(img, width=800, height=600)
# np.float32([[左上, 右上], [右上], [左下], [右下]])
pts1 = np.float32([[0, 0], [800, 0], [0, 600], [800, 600]])
pts2 = np.float32([[0, 0], [800, 0], [200, 600], [600, 600]])
img = cv.perspective(img, pts1, pts2)
cv.write(img, 'tiger2.jpg')

cv2.imshow('tiger', img)
cv2.waitKey(0)
