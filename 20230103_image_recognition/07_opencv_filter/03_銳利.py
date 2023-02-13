import cv2
import numpy as np
import pylab as plt
from sdk.IvanCv import IvanCv as cv
img_path = 'E:\project\data\img\jpg\girl2.jpg'
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

img = cv.read(img_path)
img = img[:, :, ::-1]
plt.subplot(2, 3, 1)
plt.axis('off')
plt.title('原圖 original')
plt.imshow(img)

kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
sharp = cv2.filter2D(img, -1, kernel=kernel)
plt.subplot(2, 3, 2)
plt.axis('off')
plt.title('銳利 sharp')
plt.imshow(sharp)

kernel2 = np.array([[-0.125, -0.125, -0.125, -0.125, -0.125],
                   [-0.125, 0.25, 0.25, 0.25, -0.125],
                   [-0.125, 0.25, 1, 0.25, -0.125],
                   [-0.125, 0.25, 0.25, 0.25, -0.125],
                   [-0.125, -0.125, -0.125, -0.125, -0.125]], np.float32)
sharp2 = cv2.filter2D(img, -1, kernel=kernel2)
plt.subplot(2, 3, 3)
plt.axis('off')
plt.title('銳利2 sharp2')
plt.imshow(sharp2)

sharp3 = sharp2
for i in range(4):
    sharp3 = cv2.filter2D(sharp3, -1, kernel=kernel2)
plt.subplot(2, 3, 4)
plt.axis('off')
plt.title('銳利-失真')
plt.imshow(sharp3)

plt.show()
