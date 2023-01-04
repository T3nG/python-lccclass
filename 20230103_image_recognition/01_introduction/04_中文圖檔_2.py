# pip install Pillow
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Pillow 的顏色值為 RGB
img = Image.open('老虎.jpg')
# 將 Pillow格式轉成 numpy array
img = np.asarray(img)
plt.imshow(img)
plt.show()
