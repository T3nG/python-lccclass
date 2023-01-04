import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open('老虎.jpg')
img = np.asarray(img)
img = cv2.resize(img, (800, 600), interpolation=cv2.INTER_LINEAR)

# plt.imshow(img)
# plt.axis('off')
# plt.show()

img = Image.fromarray(img)
img.save('老虎_縮圖_2.jpg')
