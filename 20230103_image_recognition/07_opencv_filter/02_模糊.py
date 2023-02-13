import cv2
import pylab as plt
from sdk.IvanCv import IvanCv as cv
img_path = 'E:\project\data\img\jpg\girl.jpg'
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

img = cv.read(img_path)
img = img[:, :, ::-1]
plt.subplot(2, 3, 1)
plt.axis('off')
plt.title('原圖 original')
plt.imshow(img)

# 平滑模糊 blur (kernel大小): 愈大愈模糊
blur = cv2.blur(img, (55, 55))
plt.subplot(2, 3, 2)
plt.axis('off')
plt.title('平滑模糊 blur')
plt.imshow(blur)

# 高斯模糊 GaussianBlur (kernel大小需為奇數)
# 每個點的權重不一樣, 愈中間權重愈大, 愈旁邊權重愈小
# 高斯模糊比較不會失真, 平滑模糊失真較嚴重
gauss = cv2.GaussianBlur(img, (55, 55), 0)
plt.subplot(2, 3, 3)
plt.axis('off')
plt.title('高斯模糊 GaussianBlur')
plt.imshow(gauss)

# kernel (0,0), sigmaX 及 sigmaY 才會生效, sigmaX 不可為0
# 水平方向高斯模糊
gaussX = cv2.GaussianBlur(img, (0, 0), sigmaX=20, sigmaY=1)
plt.subplot(2, 3, 4)
plt.axis('off')
plt.title('高斯模糊水平方向 GaussianBlurX')
plt.imshow(gaussX)

# 垂直方向高斯模糊
gaussY = cv2.GaussianBlur(img, (0, 0), sigmaX=1, sigmaY=20)
plt.subplot(2, 3, 5)
plt.axis('off')
plt.title('高斯模糊垂直方向 GaussianBlurY')
plt.imshow(gaussY)


plt.show()
