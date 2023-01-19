from sdk.IvanCv import IvanCv as cv
import cv2

img = cv.read('老虎.jpg')
img = cv.resize(img, scale=0.2)
for i in range(720):
    img_r = cv.rotation(img, angle=i, scale=0.5)
    cv2.imshow('tiger', img_r)
    if cv2.waitKey(30) == 27:
        break

