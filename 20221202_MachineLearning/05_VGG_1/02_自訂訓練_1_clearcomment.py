_# 下載圖片, 放到專案底下 http://download.tensorflow.org/example_images/flower_photos.tgz
# 解壓縮flower_photos至專案目錄下, 並把底下的 LICENSE.txt 刪除
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import shutil
import time
import random
import numpy as np
import cv2

import pylab as plt
from keras import Sequential
from keras.layers import GlobalAveragePooling2D, Dense, BatchNormalization, Dropout
from keras.optimizers import Adam
from keras.applications import VGG19

# count = 3670
data = []
labels = []
path = "flower_photos"
for flower in os.listdir(path):  # flower = daisy, dandelion, roses, sunflowers, tulips
    for file in os.listdir(os.path.join(path, flower)):
        absFilePath = os.path.join(path, flower, file)
        img = cv2.imdecode(np.fromfile(absFilePath, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img, (224,224), interpolation=cv2.INTER_LINEAR)
        data.append(img)
        labels.append(flower)
type = {'daisy': 0, 'dandelion': 1, 'roses': 2, 'sunflowers': 3, 'tulips': 4}
upset = list(zip(data, labels))
random.shuffle(upset)  # 將upset裡的每一列資料依亂數重排
data[:], labels[:] = zip(*upset)
train_data = np.array([data[i] for i in range(len(data)) if i % 9 > 1])  # if i % 9 > 1  => 90% 放入 train_data
train_label = np.array([labels[i] for i in range(len(labels)) if i % 9 > 1])
test_data = np.array([data[i] for i in range(len(data)) if i % 9 <= 1])  # if i % 9 <= 1  => 10% 放入 test_data
test_label = np.array([labels[i] for i in range(len(labels)) if i % 9 <= 1])
# 底下將 label 變成 one hot
# trains_labels, test_labels 創建判斷用的二維陣列, 每一列有5個元素, 列數 = train_label
train_labels = np.zeros([len(train_label), 5])
test_labels = np.zeros([len(test_label), 5])
for i in range(len(train_labels)):
    train_labels[i][type[train_label[i]]] = 1
for i in range(len(test_labels)):
    test_labels[i][type[test_label[i]]] = 1
#print(test_labels)

model_base = VGG19(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)
for layer in model_base.layers:
    layer.trainable = False
# Sequential 空模型, 按照一層一層的順序進行計算, 沒有if 也沒有迴圈
model = Sequential()
model.add(model_base)
model.add(GlobalAveragePooling2D())
model.add(Dense(256, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(64, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Dense(5, activation='softmax'))

model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',  # 分類交叉熵
              metrics=['accuracy']
              )

t1 = time.time()
history = model.fit(
    train_data,
    train_labels,
    batch_size=64,
    epochs=50,
    validation_data=(test_data, test_labels)
)
t2 = time.time()
print(f'建模花費時間 {t2-t1}秒')
model_path = './model_flower_2'
if os.path.exists(model_path):
    shutil.rmtree(model_path)
model.save('model_flower_2')

p1 = plt.plot(history.history['accuracy'], label='training accuracy')  # 訓練的準確度
p2 = plt.plot(history.history['val_accuracy'], label='value accuracy')  # 訓練的準確度
p3 = plt.plot(history.history['loss'], label='training loss')  # 訓練時的損失率
p4 = plt.plot(history.history['val_loss'], label='value loss')  # 訓練時的損失率
plt.legend()
plt.show()
