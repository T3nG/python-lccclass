import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import keras
import cv2
import numpy as np
from keras.applications.vgg19 import preprocess_input

flower_type = {0: 'daisy', 1: 'dandelion', 2: 'roses', 3: 'sunflowers', 4: 'tulips'}
model = keras.models.load_model('model_flower')
# 訓練好後先從原始資料去抓圖, 若能偵測出來, 再去找其他圖片來偵測
test_raw = './flower_photos/roses/394990940_7af082cf8d_n.jpg'
test_img1 = './test_img/rose1.jpg'
test_img2 = './test_img/rose2.jpg'
test_img3 = './test_img/tulips1.jpg'
test_img4 = './test_img/tulips2.jpg'
img = cv2.imdecode(
    np.fromfile(test_img4, dtype=np.uint8),
    cv2.IMREAD_UNCHANGED)
x = cv2.resize(img, (224,224), interpolation=cv2.INTER_LINEAR)
x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
out = model.predict(x)
idx = out[0].argmax()  # 取最大值的索引
print(flower_type[idx])
