# ref: http://mahaljsp.asuscomm.com/index.php/2020/12/04/%e5%bd%b1%e5%83%8f%e7%89%b9%e5%be%b5/
import cv2
import numpy as np
import pylab as plt
from sdk.IvanCv import IvanCv as cv
img_path = 'E:\project\data\img\jpg\\word.jpg'
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

img = cv.read(img_path)
img = img[:, :, ::-1]
plt.subplot(2, 3, 1)
plt.axis('off')
plt.title('原圖 original')
plt.imshow(img)

kernel = np.ones((5, 5), dtype=np.uint8)
erosion = cv2.erode(img, kernel, iterations=2)  # iterations : 次數
plt.subplot(2, 3, 2)
plt.axis('off')
plt.title('侵蝕 erosion')
plt.imshow(erosion)

dilate = cv2.dilate(img, kernel, iterations=2)  # iterations : 次數
plt.subplot(2, 3, 3)
plt.axis('off')
plt.title('膨脹 dilate')
plt.imshow(dilate)
plt.show()

