from sdk.IvanCv import IvanCv as cv
from sdk.IvanCv import Direction
import cv2

img = cv.read('老虎.jpg')
img = cv.resize(img, scale=0.2)
img = cv.flip(img, direction=Direction.HORIZONTAL)
cv2.imshow('tiger', img)
cv2.waitKey(0)
