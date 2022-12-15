# http://mahaljsp.asuscomm.com/index.php/2022/10/07/vgg19/
# 深度學習, 不須手動提供特徵, 自己會去尋找特徵(要找什麼特徵, 其實還是製模的人提供的啦)
# 製模: 指的是 VGG開發團隊, 他們就在模型裡指定要找 5504個特徵
# 建模: 訓練模型的人, 就是我們自己
# 成千上萬的模型不是一個人可以全部了解, 但如果能了解裡面的結構, 就可以變化重新組合, 使用在別的應用上

# VGG初級應用在圖片的分類, 因為是圖片分類, 所以圖片裡面只能有一個物件
# pip install tensorflow==2.10.1 opencv-python Pillow matplotlib
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
import pylab as plt
import cv2
from PIL import Image, ImageFont, ImageDraw
from keras.applications import VGG19, vgg19
from keras.applications.vgg19 import preprocess_input
# 執行, 下載模型 vgg19_weights_tf_dim_ordering_tf_kernels.h5
# 位置在 C:\Users\登入者\.keras\models
model = VGG19(weights="imagenet", include_top=True)
# 可以讀中文檔名
img = cv2.imdecode(np.fromfile('tiger.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
# VGG19使用 224*224解析度進行訓練, 所以要偵測的圖片也要縮小, 快速建立模型, 但辨識力會受限
x = cv2.resize(img, (224, 224), interpolation=cv2.INTER_LINEAR)
x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)  # BGR => RGB
# VGG19規定訓練或偵測的圖片, 必須是(1, 224, 224, 30) 的維度, 前面的維度是為了做 one-hot
x = np.expand_dims(x, axis=0)  # 變成四維

# 圖片預處理
# preprocess_input 預處理圖片有三種方式, caffe, tf, troch
# caffe 會將 RGB轉成BGR 然後每一個點的 B值 - B的的平均數, GR亦同, 結果就能讓顏色值分布在 0 的左右二邊
# zlibwapi.dll
# https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#prerequisites-windows
# 放到 CUDA 底下的 bin
# C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin
x = preprocess_input(x)
out = model.predict(x)
print(out)

# decode_prediction: 將out 轉成標籤及分數
result = vgg19.decode_predictions(out, top=3)[0][0]  # top=3 只列出前三
name = result[1]
score = result[2]
print(name, score)

img = cv2.resize(img, (1024, 768), interpolation=cv2.INTER_LINEAR)
pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
font = ImageFont.truetype('simsun.ttc', 50)
txt1 = f'種類 : {name}'
txt2 = f'信心度 : {score*100:.2f}%'
ImageDraw.Draw(pil).text((5, 5), txt1, font=font, fill=(255, 0, 0))  # fill 顏色
ImageDraw.Draw(pil).text((5, 50), txt2, font=font, fill=(255, 0, 0))
plt.imshow(pil)
plt.show()
'''
1. 載入 VGG19模型
2. 縮圖成 224*224
3. 擴展成 4 維度
4. caffe 預處理, 將顏色分布於 0 的左右
5. predict 開始辨識評估
辨識時間太久了, 一張圖要 2 秒以上
作為教學適合, 因為是最簡單的
'''