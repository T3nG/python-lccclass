import numpy as np
import cv2
import pylab as plt

img = cv2.imdecode(np.fromfile('../Edgerunners-Lucy.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
print(img.shape)
img = cv2.resize(img, (1600,900), interpolation=cv2.INTER_LINEAR)
#cv2.imshow("Lucy Original",img)

# 切片
# img=img[500:, 800:, :] # 第三個項目是RGB, 表示不限定範圍
# cv2.imshow("Lucy",img)
# print(img.shape)

# img[第0維全部, 第1維全部, 第2維全部但反向]
#img=img[:,:,:] :-1 反向選取
#img=img[:,:,::-1] # BGR2RGB
img_rgb=img[...,::-1].copy() # ...前面都一樣, ::-1反向選取
# cv2.cvtColor()使用深度copy 與上述一樣意思

plt.imshow(img_rgb)
#plt.imshow(img)
plt.axis("off")
plt.show()
cv2.waitKey(0)

# 用 plt來顯示還有一個好處, 視窗可以放大縮小

# a=np.array([0,1,2,3,4,5,6,55,66,8,7,6])
# print(a[3:-1:2]) # 步進2
# print(a[::-1]) # 反向選取
# print(a.shape)
# print(a[3:])
# print(a[3:-1])
# print(a[5:-3])

# b=np.array([ [1,2,3,4],[5,6,7,8],[9,10,11,12] ])
# print(b)
# c=b[1:, ]
# print(c)
# d=b[1:, :-1]
# print(d)
# b[第0維起始 : 第0維結束, 第1維起始 : 第1維結束, 第3維起始 : 第3維結束]

e=np.array([1,2,3,4,5])
f=e[2:] # 連結指向, 後續若陣列被改變, 也會跟著變
#f=e[2:].copy() # 深度copy 拷貝新的一份到其他記憶體
f=e[0]=100
print(e)
print(f)