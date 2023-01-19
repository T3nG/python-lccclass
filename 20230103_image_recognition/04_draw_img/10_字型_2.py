import platform
import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw

from sdk.IvanCv import IvanCv as cv

img = cv.read('老虎.jpg')
img = cv.resize(img, scale=0.25)

# # 顯示中文的方法

# txt = '老虎'
# size = 50
# x = 10
# y = 50
# color = (0, 255, 0)
# pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# if platform.system() == 'Linux':
#     font = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqz-zenhei.ttc', size)
# else:
#     font = ImageFont.truetype('simsun.ttc', size)
# # if not isinstance(txt, np.unicode):
# #     txt = txt.decode('utf-8')
# ImageDraw.Draw(pil).text((x, y), txt, font=font, fill=color)
# img = np.asarray(pil)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img = cv.text(img, (10, 50), '老虎', size=50, color=(0, 0, 255))

cv2.imshow('tiger', img)
cv2.waitKey(0)