import requests
# page=requests.get("http://mahaljsp.asuscomm.com/wp-content/uploads/2016/10/img_6279.jpg")

#print(page.text) #印出來是二進制的
# with open("tiger.jpg",'wb') as file: # 抓下來後直接以二進制寫入
#     file.write(page.content)

# 用迴圈一次抓多張圖片
# ls=["urls"]
# for i, l in enumerate(ls):
#     page.requests.get(l)
#     with open(f"{i}.jpg",'wb') as file:
#         file.write(page.content)

# 圖片抓取後, 直接儲存到硬碟
# 儲存到硬碟速度很慢,
# 有沒有辦法直接顯示出來: 儲存到硬碟 -> 從硬碟載入 -> 顯示在螢幕

# pip install opencv-python
# import cv2
# img=cv2.imread("tiger.jpg", cv2.IMREAD_UNCHANGED)
# img=cv2.resize(img, (1024,768), interpolation=cv2.INTER_LINEAR)
# cv2.imshow('test',img)
# cv2.waitKey(0)

# =============== 以上的寫法若圖片很多的話會花很多時間, 若沒有要寫入硬碟, 想要直接顯示出來, 要用下面的寫法
# =============== 改良版, 不存入硬碟, 只是顯示

# pip install Pillow
# pip install matplotlib

from PIL import Image
from io import BytesIO
import pylab as plt

# 下載下來是存在記憶體中
# BytesIO: 將內容轉成 bytes串流
# Image: 形成 Pillow 格式檔
page=requests.get("http://mahaljsp.asuscomm.com/wp-content/uploads/2016/10/img_6279.jpg")
img=Image.open(BytesIO(page.content))
plt.imshow(img)
plt.show()

# Pillow 也可以存檔, 且支援中文檔名
# Opencv 無法讀取或儲存中文檔名, 但有很多強大的功能
img.save("老虎.jpg")

# 將 Pillow 格式轉成 opencv 格式
# Pillow 為RGB, opencv 為BGR
import numpy as np
import cv2

img=np.asarray(img, dtype=np.uint8)
img=cv2.resize(img, (1024,768), interpolation=cv2.INTER_LINEAR)
img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
cv2.imshow("tiger",img)
cv2.waitKey(0)