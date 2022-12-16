import numpy as np
import pylab as plt
from PIL import Image
import cv2

img = np.asarray(Image.open('dog.jpg'))  # opencv的numpy格式, 但屬於RGB格式
# img = cv2.resize(img, (1024,768))
oh, ow, _ = img.shape  # _ 第三個參數不接收 (rgb)
# 設定高度, 維持寬度比例
height = 200
width = int(ow*height/oh)
img = cv2.resize(img, (width, height))
print(f"gram_matrix_size: {(width*height)**2*3:,}")
print("太大可能導致記憶體不足!")
cv2.imshow('dog', img)
cv2.waitKey(0)
# plt.imshow(img)
# plt.axis('off')
# plt.show()
