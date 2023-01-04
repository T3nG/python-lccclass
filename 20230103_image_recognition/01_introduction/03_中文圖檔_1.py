import cv2
import pylab as plt
import numpy as np
# cv2不支援中文檔名
# img = cv2.imread('老虎.jpg')
# decode 解碼, 將壓縮檔解開, 會很佔記憶體

# IMREAD_COLOR 忽略透明值(alpha)
# IMREAD_UNCHANGED
# IMREAD_ GRAYSCALE
img = cv2.imdecode(np.fromfile('老虎.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
img = img[:, :, ::-1].copy()
plt.imshow(img)

# img = cv2.imdecode(np.fromfile('老虎.jpg', dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
# plt.imshow(img, cmap='gray')

plt.axis('off')
plt.show()
