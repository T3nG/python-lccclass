# fast: Edward/Tom 高速拐角檢測
# 跟哈里斯類似, 但速度較快, 背景最好是白色, 偵測路徑及角點, 敏感度的問題
import cv2
import numpy as np
import pylab as plt
from sdk.IvanCv import IvanCv as cv
img_path_whiteBG = 'E:\project\data\img\jpg\\fast.jpg'
img_path_blackBG = 'E:\project\data\img\jpg\\poly.jpg'
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

img = cv.read(img_path_whiteBG)
img = img[:, :, ::-1]
plt.subplot(2, 2, 1)
plt.axis('off')
plt.title('原圖 original')
plt.imshow(img)

fast = cv2.FastFeatureDetector_create()  # 建立偵測器
key_point = fast.detect(img)  # 偵測, 建立 key point
img_fast = cv2.drawKeypoints(img, key_point, None, color=(255, 0, 0))
plt.subplot(2, 2, 2)
plt.axis('off')
plt.title('高速拐角點 fast')
plt.imshow(img_fast)

img2 = cv.read(img_path_blackBG)
img2 = img2[:, :, ::-1]
plt.subplot(2, 2, 3)
plt.axis('off')
plt.title('原圖-黑BG original black')
plt.imshow(img2)

key_point2 = fast.detect(img2)
img2_fast = cv2.drawKeypoints(img2, key_point2, None, color=(255, 0, 0))
plt.subplot(2, 2, 4)
plt.axis('off')
plt.title('高速拐角點2 fast black')
plt.imshow(img2_fast)


plt.show()