# 用matplotlib顯示圖片的好處是, 可以隨視窗縮放變更比例
import cv2
import pylab as plt
img = cv2.imread('tiger.jpg')
h, w, _ = img.shape
new_width = 1024
new_height = int(new_width * h / w)
img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)  # 內部線性差值
# cv2.imshow('tiger', img)
# cv2.waitKey(0)

# 轉換顏色, 方式一
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 也使用深度copy
# 轉換顏色, 方式二
img = img[:, :, ::-1].copy()  # 深度copy 產生另一個新的陣列
plt.imshow(img)
plt.show()
