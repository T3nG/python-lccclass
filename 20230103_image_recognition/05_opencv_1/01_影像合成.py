# 影像合成: 二張圖片的大小必須一致
import cv2
import pylab as plt
from sdk.IvanCv import IvanCv as cv
img_a = cv.read('E:\project\data\img\yolo7testimg\\0000010.jpg')  # 4608 x 3456  1200萬畫素  4:3
img_b = cv.read('E:\project\data\img\yolo7testimg\\0000011.jpg')  # 4096 x 2304   900萬畫素 16:9
img_a = cv.resize(img_a, width=1024, height=768)
# width = 2304/3*4 = 3072 : height = 2304, x1y1=(500,0), x2y2=(3572, 2304)
# 左上右下的點, 其餘切除
img_b = cv.crop(img_b, 500, 0, 3572, 2304)
img_b = cv.resize(img_b, width=1024, height=768)
# plt.subplot(1, 2, 1)
# plt.imshow(img_a[:,:,::-1])
# plt.subplot(1, 2, 2)
# plt.imshow(img_b[:,:,::-1])
# plt.show()

# 最後一個參數為亮度, 0不變, 255白色
img_c = cv2.addWeighted(img_a, 0.4, img_b, 0.6, 0)
cv2.imshow('c', img_c)
cv2.waitKey(0)
