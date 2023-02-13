# Harris 哈里斯角點: 偵測邊緣轉折點, 應用於倉庫中, 有畫行徑路線的無人車
# 無人駕駛車: LiDAR 雷射二極體
# CP值較高的: KUGA
import cv2
import numpy as np
import pylab as plt
from sdk.IvanCv import IvanCv as cv
img_path = 'E:\project\data\img\jpg\\poly.jpg'
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

img = cv.read(img_path)
img = img[:, :, ::-1]
plt.subplot(2, 3, 1)
plt.axis('off')
plt.title('原圖 original')
plt.imshow(img)

# 哈里斯需先轉成灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
# cornerHarris(img, blockSize, ksize, k)
# blockSize: 角點檢測區域大小, ksize: sobel使用的 kernel大小, k: 自由引數
harris_detector = cv2.cornerHarris(gray, 2, 3, 0.01)
dilate = cv2.dilate(harris_detector, None)  # 小角度時也能判定
threshold = 0.01 * dilate.max()
harris = img.copy()
harris[dilate > threshold] = [255, 0, 0]
plt.subplot(2, 3, 2)
plt.axis('off')
plt.title('哈里斯角點 harris')
plt.imshow(harris)

plt.show()
