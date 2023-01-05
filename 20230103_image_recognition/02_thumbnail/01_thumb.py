# pip install opencv-python, matplotlib
import os

import cv2
import pylab as plt
import numpy as np
from PIL import Image

path = 'E:\\project\\data\\img\\png'
thumb_path = 'E:\\project\\data\\img\\thumb'
# alt+enter: 自動 import 套件
ls = []
tree = os.walk(path)
for root, subdirs, files in tree:
    for file in files:
        if file.lower().endswith('.png'):
            ls.append(os.path.join(root, file))
if not os.path.exists(thumb_path):
    os.mkdir(thumb_path)
# 開始處理縮圖
for l in ls:
    img = Image.open(l)
    img = np.asarray(img)
    h, w, _ = img.shape
    width = 400
    height = int(width*h/w)
    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_LINEAR)
    basename = os.path.basename(l)
    img = Image.fromarray(img)  # 轉成Pillow
    img.save(os.path.join(thumb_path, basename))
    print(f'目前處理縮圖: {l}')
