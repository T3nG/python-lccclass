import cv2
from PIL import Image
from sdk.IvanCv import IvanCv
import numpy as np

img = IvanCv.read('老虎.jpg')
# img = IvanCv.resize(img, scale=0.5)
img = IvanCv.resize(img, 1024, 768)
img = IvanCv.crop(img, 1, 1, 512, 384)

# img = Image.open('老虎.jpg')
# img = np.asarray(img)
# img = img[:,:,::-1].copy()
# img = cv2.resize(img, (1024,768), interpolation=cv2.INTER_LINEAR)

# 切片
# img = img[1:768, 1:1024]  # [height, width]
cv2.imshow('tiger', img)
cv2.waitKey(0)
