# pip install opencv-python
# interl 所開發出來的套件, 其目的是要幹掉 Photoshop
import cv2
import pylab as plt

# imread 只能讀取英文檔名
# cv2.decode(np.fromfile('中文檔名'))

# subplot(列, 行, 第幾個繪圖區)
img = cv2.imread('Miro.png')  # BGR
ax = plt.subplot(1, 2, 1)
# 去除labels, axis 方法1
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.imshow(img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ax = plt.subplot(1, 2, 2)
# 去除labels, axis 方法2
ax.axis("off")
ax.imshow(img)

plt.show()