from sdk.IvanCv import IvanCv as cv
import cv2
import pylab as plt

img = cv.read('E:\project\data\img\yolo7testimg\\0000010.jpg')
img = cv.resize(img, scale=0.2)

# 灰階化 256色, 只有灰階圖片才可以二值化
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
# binary
# 顏色值比較門檻值 127, 小於則設為 0(黑), 大於則設為 255(白)
ret1, th1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# binary_inv
# 顏色值比較門檻值 127, 大於則設為 0, 小於則設為 255
ret2, th2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

# trunc
# 顏色值比較門檻值 127, 小於則不變, 大於則設為 255
ret3, th3 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TRUNC)

# tozero
# 顏色值比較門檻值 127, 大於則不變, 小於則設為 0, 第三個參數用不到, 但又不能去掉
ret4, th4 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)

# tozero_inv
# 顏色值比較門檻值 127, 小於則不變, 大於則設為 0, 第三個參數用不到, 但又不能去掉
ret5, th5 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO_INV)

# 優化
titles = ['gray', 'binary', 'binary_inv', 'trunc', 'tozero', 'tozero_inv']
imgs = [img_gray, th1, th2, th3, th4, th5]
for i, img in enumerate(imgs):
    plt.subplot(2, 3, i+1)
    plt.axis('off')
    plt.title(titles[i])
    plt.imshow(imgs[i], cmap='gray')

plt.show()
