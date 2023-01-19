import cv2

from sdk.IvanCv import IvanCv as cv
#blank = cv.blank(500, 500)
blank = cv.read('老虎.jpg')
blank = cv.resize(blank, scale=0.25)
img = cv.blank(500, 500)

# img, (中心點), (長軸, 短軸), 選轉角度(+順-逆), 起始點 度, 結束點 度, (顏色值), 線條寬度
# cv2.ellipse(img, (250, 250), (200, 100), 90, 0, 360, (0, 0, 255), 2)
# for angle in range(0, 360, 5):
#     #img = blank.copy()
#     cv.ellipse(img, (250, 250), (200, 100), angle=angle)
#     cv2.imshow('test', img)
#     cv2.waitKey(2)

angle = 0
while True:
    img = blank.copy()
    h, w, _ = img.shape
    cv.ellipse(img, (int((w-1)/2), int((h-1)/2)), (200, 100), angle=angle, line_width=3)
    cv2.imshow('test', img)
    angle = (angle + 10) % 360
    if cv2.waitKey(20) == 27:
        break


