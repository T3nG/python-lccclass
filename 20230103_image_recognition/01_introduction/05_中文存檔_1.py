import cv2
import pylab as plt
import numpy as np
img = cv2.imdecode(np.fromfile('老虎.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, (800,600), interpolation=cv2.INTER_LINEAR)

# plt.imshow(img)
# plt.axis('off')
# plt.show()

# imencode 編碼, 壓縮
# 編碼後, 第一個值[0]為success/fail, 第二個值為圖片的資料(np array)
cv2.imencode('.jpg', img)[1].tofile('老虎_縮圖_1.jpg')
# 只支援英文檔名, 可指定壓縮至何種比例
cv2.imwrite('test.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
