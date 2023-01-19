from sdk.IvanCv import IvanCv as cv
import cv2

img = cv.read('老虎.jpg')
img = cv.resize(img, scale=0.2)
img = cv.shift(img, x=300, y=-100)
cv2.imshow('tiger', img)
cv2.waitKey(0)
