import cv2

from sdk.IvanCv import IvanCv as cv
img = cv.blank(500, 300, (0, 255, 255))

# (0, 0)在左上角, 往下往右延伸
# p1(x1, y1), p2(x2, y2), (B, G, R), linewidth(uint))
# cv2.line(img, (100, 100), (200, 200), (0, 0, 255), 5)
# cv.line(img, (100, 100), (200, 200), (0, 0, 255), 5)
cv2.arrowedLine(img, (50, 50), (400, 200), (0, 255, 0), 2)

cv2.imshow('test', img)
cv2.waitKey(0)
