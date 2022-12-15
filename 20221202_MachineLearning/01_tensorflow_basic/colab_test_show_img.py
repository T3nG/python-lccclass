# pip install opencv-python, matplotlib

import cv2
import pylab as plt
# from google.colab import drive

# drive.mount('/data')  # data 名稱可自定義
img = cv2.imread('Miro.png')
# img = cv2.imread('/data/MyDrive/colab/pictures/Miro.png')

# matplotlib 顯圖
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# ax = plt.subplot(1,1,1)
# ax.axis('off')
# ax.imshow(img)
# plt.show()

# cv2 顯圖, 原圖
img = cv2.resize(img, (512, 768), cv2.INTER_LINEAR)
cv2.imshow('Miro', img)  # colab無法使用, 需使用 專用的, from google.colab.patches import cv2_imshow
# cv2_imshow(img)
cv2.waitKey(0)  # 在colab不須waitKey

