# 此主題是在AI視覺辨識的課程
# pip install opencv-python
# opencv 是 intel 開發, 用程式來打敗 photoshop 的利器
import os

import cv2
import numpy as np

# imdecode : 解碼, 存在檔案中的圖片, 都是經過壓縮的, 解碼就是在解壓縮, 解碼後很佔記憶體
# IMREAD_UNCHANGED : ? 可以讀中文檔名
# img=cv2.imdecode(np.fromfile('../老虎.jpg', dtype=np.uint8))

# img=cv2.imdecode(np.fromfile('../Edgerunners-Lucy.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
# img=cv2.resize(img,(1600,900),interpolation=cv2.INTER_LINEAR)
# 改變顯示圖片的大小
# cv2.imshow("Lucy", img)
# cv2.waitKey(0)


# 把大量圖片轉存成縮圖
original="C:/Users/User/OneDrive/圖片/KG/jpg"
thumb="D:/thumb"
if not os.path.exists(thumb):
    os.mkdir(thumb)

# ----
# for file in os.listdir(original):
#     abs_path=os.path.join(original,file)
#     img=cv2.imdecode(np.fromfile(abs_path,dtype=np.uint8),cv2.IMREAD_UNCHANGED)
#     print(img.shape)
#     img=cv2.resize(img,(480,360),interpolation=cv2.INTER_LINEAR)
#     #cv2.imshow(abs_path,img)
#     print(f"目前正在處理{abs_path}...")
#     #print(img) 每一點的RGB, 存成np格式
#     cv2.imencode('.jpg',img)[1].tofile(os.path.join(thumb,file))
#     # 產生出來的是一個tuple, [0] 是紀錄是否成功
# cv2.waitKey(0)
# ----

# ---- 以 pylab 顯示
files = os.listdir(original)
# 決定幾列幾行
count = len(files)
cols=5
rows = count // cols
if rows < count / cols:
    rows += 1
index = 1
import pylab as plt
for file in files:
    abs_path=os.path.join(original,file)
    img=cv2.imdecode(np.fromfile(abs_path,dtype=np.uint8),cv2.IMREAD_UNCHANGED)
    print(img.shape)
    img=cv2.resize(img,(480,360),interpolation=cv2.INTER_LINEAR)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # opencv 的顏色是BGR
    ax=plt.subplot(rows, cols, index)
    index+=1
    ax.axis("off")
    ax.imshow(img)
plt.show()
