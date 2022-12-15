# 下載圖片, 放到專案底下 http://download.tensorflow.org/example_images/flower_photos.tgz
# 解壓縮flower_photos至專案目錄下, 並把底下的 LICENSE.txt 刪除
import os
import shutil
import time

import pylab as plt
from keras import Sequential
from keras.layers import GlobalAveragePooling2D, Dense, BatchNormalization, Dropout
from keras.optimizers import Adam

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import random
import numpy as np
import cv2
from keras.applications import VGG19, vgg19
from keras.applications.vgg19 import preprocess_input

# count = 3670
data = []
labels = []
path = "flower_photos"
for flower in os.listdir(path):  # flower = daisy, dandelion, roses, sunflowers, tulips
    for file in os.listdir(os.path.join(path, flower)):
        absFilePath = os.path.join(path, flower, file)
        img = cv2.imdecode(np.fromfile(absFilePath, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        # 沒有縮小的話記憶體會不夠用!!
        img = cv2.resize(img, (224,224), interpolation=cv2.INTER_LINEAR)
        data.append(img)
        labels.append(flower)
kind = {'daisy': 0, 'dandelion': 1, 'roses': 2, 'sunflowers': 3, 'tulips': 4}
upset = list(zip(data, labels))
random.shuffle(upset)  # 將upset裡的每一列資料依亂數重排
data[:], labels[:] = zip(*upset)
train_data = np.array([data[i] for i in range(len(data)) if i % 9 > 1])  # if i % 9 > 1  => 90% 放入 train_data
train_label = np.array([labels[i] for i in range(len(labels)) if i % 9 > 1])
test_data = np.array([data[i] for i in range(len(data)) if i % 9 <= 1])  # if i % 9 <= 1  => 10% 放入 test_data
test_label = np.array([labels[i] for i in range(len(labels)) if i % 9 <= 1])
# 底下將 label 變成 one hot
'''
one hot 是一個挺笨的量化方式, 若種類一多, 每列裡面的元素會超級多
整列中, 只有一個元素是1, 其他都是0, 將rose轉成數字, 叫像量化, 量化, 數字化
[[0,0,0,1,0],
 [0,0,0,0,1],
 ... 共 OO 張
 ]
'''
# trains_labels, test_labels 創建判斷用的二維陣列, 每一列有5個元素, 列數 = train_label
train_labels = np.zeros([len(train_label), 5])
test_labels = np.zeros([len(test_label), 5])
for i in range(len(train_labels)):
    train_labels[i][kind[train_label[i]]] = 1
for i in range(len(test_labels)):
    test_labels[i][kind[test_label[i]]] = 1
#print(test_labels)

# include_top=False  不使用最上面的三個全連接層, 也就是輸出層 FC1 FC2 softmax , 因為預設是 1000種, 這裡只有 5 種花卉
# http://mahaljsp.asuscomm.com/index.php/2022/10/17/vgg19%e7%89%b9%e5%be%b5/
model_base = VGG19(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)
# 不要重新訓練VGG19給的權重, 否則捲積核會被破壞掉
for layer in model_base.layers:
    layer.trainable = False
# Sequential 空模型, 按照一層一層的順序進行計算, 沒有if 也沒有迴圈
model = Sequential()
model.add(model_base)
# 將224*224*3 變成 1*1*3維度, 前面的224個數變成一個字, 作用平均值
model.add(GlobalAveragePooling2D())
# Dense 具有輸入及輸出, 輸出256種狀況(從5504)
# activation 激活函數, 常見的有:
# sigmoid 介於 0~1之間
# softmax 將值轉成機率, 總和為1
# relu 線性整流, 將 負值變成0
model.add(Dense(256, activation='relu'))
# BatchNormalization 將數字集中在平均為0, 標準差為1的常態分佈
model.add(BatchNormalization())
model.add(Dense(64, activation='relu'))
model.add(BatchNormalization())
# 丟掉20%的值
# 池化層 去除不必要的資訊, 隨機關閉 20%的神經元(權重), 這是為了防止神經元之間有過度擬合的現象
model.add(Dropout(0.2))
model.add(Dense(5, activation='softmax'))

# 編譯, optimizer 優化器
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',  # 分類交叉熵
              metrics=['accuracy']
              )

# 開始訓練, 通常會花很長的時間, 又稱為建模
t1 = time.time()
history = model.fit(
    train_data,
    train_labels,
    batch_size=64,  # 太大會造成顯卡記憶體不足, 數大則每世代的量小, 數小則每世代的量大
    epochs=50,  # 訓練50次
    validation_data=(test_data, test_labels)
)
t2 = time.time()
print(f'建模花費時間 {t2-t1}秒')
model_path = './model_flower'
# 若已有模型, 則移除, 方便測試
if os.path.exists(model_path):
    shutil.rmtree(model_path)
model.save('model_flower')

p1 = plt.plot(history.history['accuracy'], label='training accuracy')  # 訓練的準確度
p2 = plt.plot(history.history['val_accuracy'], label='value accuracy')  # 訓練的準確度
p3 = plt.plot(history.history['loss'], label='training loss')  # 訓練時的損失率
p4 = plt.plot(history.history['val_loss'], label='value loss')  # 訓練時的損失率
plt.savefig('Figure_1.png')
plt.legend()
plt.show()
