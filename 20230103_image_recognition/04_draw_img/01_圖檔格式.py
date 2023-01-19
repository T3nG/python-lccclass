import cv2

from sdk.IvanCv import IvanCv as cv
img = cv.read('老虎.jpg')
img = cv.resize(img, scale=0.05)
# print(img.shape)
# print(img)
cv2.imshow('tiger', img)
cv2.waitKey(0)
