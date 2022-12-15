# http://mahaljsp.asuscomm.com/index.php/2022/08/25/matplotlib%e8%a9%b3%e8%a7%a3/
import pylab as plt
import cv2

# img = cv2.imread('Miro.png')
# fig, ax = plt.subplots(2,2, figsize=(12, 6))
# ax[0][0].axis('off')
# ax[0][0].imshow(img)
#
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# ax[1][1].axis('off')
# ax[1][1].imshow(img)

img = cv2.imread('Miro.png')
fig, ax = plt.subplots(1,2, figsize=(12, 6))
ax[0].axis('off')
ax[0].imshow(img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ax[1].axis('off')
ax[1].imshow(img)

plt.show()
