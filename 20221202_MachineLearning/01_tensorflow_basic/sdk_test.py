import cv2

from sdk.YHT import YHTCv
from sdk.YHT import circle

print(circle(100))
img = YHTCv.read('Miro.png')
img = YHTCv.resize(img, 512, 768)
cv2.imshow('Miro', img)
cv2.waitKey(0)

'''colab, 於雲端硬碟新增檔案後, 需中斷目前執行階段, 重新連線, 才能讀取到
import cv2
import os
import sys

from google.colab import drive
from google.colab.patches import cv2_imshow

drive.mount('/data')
img_path=os.path.join('/data/MyDrive/colab/pictures','Miro.png')
sdk_path='/data/MyDrive/colab/sdk'
sys.path.append(sdk_path)  # 記錄著要import的路徑
!ls $sdk_path  # 列出檔案
!ls $img_path  # 列出檔案

from YHT import YHTCv
from YHT import circle

print(circle(100))
img=YHTCv.read(img_path)
img=YHTCv.resize(img, 512, 768)
cv2_imshow(img)

'''