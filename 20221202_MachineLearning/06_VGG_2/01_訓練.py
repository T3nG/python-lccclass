# pip install tensorflow==2.10.1 opencv-python Pillow matplotlib
# 下載圖片 http://mahaljsp.asuscomm.com/files/vgg19/flowers_17.zip
import os

from keras.optimizers import Adam

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import random
import shutil
import numpy as np
import cv2
import time
import pylab as plt
from keras import Sequential
from keras.applications import VGG19
from keras.layers import GlobalAveragePooling2D, Dense, BatchNormalization, Dropout

# 讀取label
flowers = []
dirs = np.empty(0, dtype=object)
with open('label.txt') as file:
    for line in file:
        line = line.strip()
        cols = line.split()
        s = int(cols[0])
        e = int(cols[1])
        flowers.append(cols[2])
        dirs = np.r_[dirs, [cols[2]]*(e-s+1)]
# 準備資料夾
raw_dir = 'flowers_17'
train_dir = 'train_img'  # raw 90% => train
test_dir = 'test_img'  # raw 10% => test
if os.path.exists(train_dir):
    shutil.rmtree(train_dir)
if os.path.exists(test_dir):
    shutil.rmtree(test_dir)
os.mkdir(train_dir)
os.mkdir(test_dir)
for flower in flowers:
    if not os.path.exists(os.path.join(train_dir, flower)):
        os.mkdir(os.path.join(train_dir, flower))
    if not os.path.exists(os.path.join(test_dir, flower)):
        os.mkdir(os.path.join(test_dir, flower))
# 將資料從 flowers_17 分類搬到 train_dir
for file, dir in zip(sorted(os.listdir(raw_dir)), dirs):
    src = os.path.join(raw_dir, file)
    dst = os.path.join(train_dir, dir, file)
    shutil.copy(src, dst)
# 從train_dir 每一種類中選前 10%搬到test_dir
for flower in os.listdir(train_dir):
    files = os.listdir(os.path.join(train_dir, flower))
    for file in files[:8]:
        src = os.path.join(train_dir, flower, file)
        dst = os.path.join(test_dir, flower)
        print(f'move {src} => {dst}')
        shutil.move(src, dst)
# 準備訓練資料
train_data = []
train_labels = []
path = 'train_img'
for flower in flowers:
    for file in os.listdir(os.path.join(path, flower)):
        img = cv2.imdecode(np.fromfile(os.path.join(path, flower, file), dtype=np.uint8),
                           cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img, (224,224), interpolation=cv2.INTER_LINEAR)
        train_data.append(img)
        train_labels.append(flower)
train_data=np.array(train_data)
# 準備驗證資料
test_data = []
test_labels = []
path = 'test_img'
for flower in flowers:
    for file in os.listdir(os.path.join(path, flower)):
        img = cv2.imdecode(np.fromfile(os.path.join(path, flower, file), dtype=np.uint8),
                           cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img, (224,224), interpolation=cv2.INTER_LINEAR)
        test_data.append(img)
        test_labels.append(flower)
test_data=np.array(test_data)

train_labels_onehot = np.zeros([len(train_data), 17], dtype=np.int32)
test_labels_onehot = np.zeros([len(test_data), 17], dtype=np.int32)

for i in range(len(train_labels_onehot)):
    train_labels_onehot[i][flowers.index(train_labels[i])] = 1
    # print(train_labels_onehot[i])
for i in range(len(test_labels_onehot)):
    test_labels_onehot[i][flowers.index(test_labels[i])] = 1
    # print(test_labels_onehot[i])
# 載入模型
model_base = VGG19(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)
# 不要重新訓練VGG19給的權重, 否則捲積核會被破壞掉
for layer in model_base.layers:
    layer.trainable = False

model = Sequential()
model.add(model_base)
model.add(GlobalAveragePooling2D())
model.add(Dense(256, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(64, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Dense(17, activation='softmax'))
# 編譯, optimizer 優化器
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',  # 分類交叉熵
              metrics=['accuracy']
              )
# 開始訓練, 通常會花很長的時間, 又稱為建模
t1 = time.time()
history = model.fit(
    train_data,
    train_labels_onehot,
    batch_size=64,  # 太大會造成顯卡記憶體不足, 數大則每世代的量小, 數小則每世代的量大
    epochs=50,  # 訓練50次
    validation_data=(test_data, test_labels_onehot)
)
t2 = time.time()
print(f'建模花費時間 {t2-t1}秒')
model_path = './model_flower_17'
# 若已有模型, 則移除, 方便測試
if os.path.exists(model_path):
    shutil.rmtree(model_path)
model.save('model_flower_17')

p1 = plt.plot(history.history['accuracy'], label='training accuracy')  # 訓練的準確度
p2 = plt.plot(history.history['val_accuracy'], label='value accuracy')  # 訓練的準確度
p3 = plt.plot(history.history['loss'], label='training loss')  # 訓練時的損失率
p4 = plt.plot(history.history['val_loss'], label='value loss')  # 訓練時的損失率
plt.savefig('Figure_1.png')
plt.legend()
plt.show()
