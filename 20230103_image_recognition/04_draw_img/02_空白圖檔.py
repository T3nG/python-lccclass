import cv2
import numpy as np
from sdk.IvanCv import IvanCv as cv
# a = np.zeros([200, 200, 3], dtype=np.uint8)  # unsigned 僅有正值
# print(a)
a = cv.blank(200, 200, (255, 255, 255))
a[50:150, 50:150] = (0, 0, 255)
a[:50, :50] = (255, 0, 255)
a[150:, 150:] = (0, 0, 0)
cv2.imshow('test', a)
cv2.waitKey(0)
