import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import cv2
import keras
import numpy as np
import pylab as plt
from keras.applications import VGG19
from keras.applications.vgg19 import preprocess_input

model = VGG19(weights='imagenet', include_top=False)

img = cv2.imdecode(np.fromfile('starry_night.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, (224,224), interpolation=cv2.INTER_LINEAR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = np.expand_dims(img, axis=0)
img = preprocess_input(img)

# 將隱藏層移到輸出層
outs_dict = dict([(layer.name, layer.output) for layer in model.layers])
#print(outs_dict)
model = keras.Model(inputs=model.inputs, outputs=outs_dict)


outputs = model(img)
for i, layer in enumerate(outputs):
    print(i+1, layer, outputs[layer].shape)
'''
1 input_1 (1, 224, 224, 3)
2 block1_conv1 (1, 224, 224, 64)
3 block1_conv2 (1, 224, 224, 64)
4 block1_pool (1, 112, 112, 64)
5 block2_conv1 (1, 112, 112, 128)
6 block2_conv2 (1, 112, 112, 128)
7 block2_pool (1, 56, 56, 128)
8 block3_conv1 (1, 56, 56, 256)
9 block3_conv2 (1, 56, 56, 256)
10 block3_conv3 (1, 56, 56, 256)
11 block3_conv4 (1, 56, 56, 256)
12 block3_pool (1, 28, 28, 256)
13 block4_conv1 (1, 28, 28, 512)
14 block4_conv2 (1, 28, 28, 512)
15 block4_conv3 (1, 28, 28, 512)
16 block4_conv4 (1, 28, 28, 512)
17 block4_pool (1, 14, 14, 512)
18 block5_conv1 (1, 14, 14, 512)
19 block5_conv2 (1, 14, 14, 512)
20 block5_conv3 (1, 14, 14, 512)
21 block5_conv4 (1, 14, 14, 512)
22 block5_pool (1, 7, 7, 512)
'''
# b1_c1 = outputs['block1_conv1']
# r, h, w, c = b1_c1.shape  # r 1, h 224, w 224, c 3
# b1_c1 = tf.reshape(b1_c1, (h, w, c))  # 降維
# print(b1_c1)
# for i in range(64):
#     plt.subplot(8, 8, i+1)
#     print(b1_c1[:,:,i].numpy())
#     img = np.reshape(b1_c1[:,:,i].numpy(), (h, w, 1))
#     plt.imshow(img, cmap='gray')
#     plt.axis('off')
# plt.show()
# 64張圖, 64個特徵

b2_c1 = outputs['block1_conv1']
r, h, w, c = b2_c1.shape  # r 1, h 224, w 224, c 3
b2_c1 = tf.reshape(b2_c1, (h, w, c))  # 降維
print(b2_c1)
for i in range(64):
    plt.subplot(8, 8, i+1)
    print(b2_c1[:,:,i].numpy())
    img = np.reshape(b2_c1[:,:,i].numpy(), (h, w, 1))
    plt.imshow(img, cmap='gray')
    plt.axis('off')
plt.show()

# 每種顏色分開考慮 1, 224, 224, 3
# 3 的意義, RGB, 對電腦而言只有一種顏色, 灰階
# block1: 64*2  , 邊緣, 紋理
# block2: 128*2 ,
# block3: 256*4 ,
# block4: 512*4 ,
# block5: 512*4 , 點線等
# 總共特徵數 5504張圖
# VGG19的捲積核是 3*3的陣列
# VGG16好像是 5*5, 待確認



# for i, layer in enumerate(model.layers):
#     print(i+1, layer.name, layer.input, layer.output)
# 每一層都有各自獨立的輸入與輸出
'''2 block1_conv1
輸入
KerasTensor(type_spec=TensorSpec(shape=(None, None, None, 3), 
dtype=tf.float32, name='input_1'), name='input_1', description="created by layer 'input_1'")
輸出
KerasTensor(type_spec=TensorSpec(shape=(None, None, None, 64), 
dtype=tf.float32, name=None), name='block1_conv1/Relu:0', description="created by layer 'block1_conv1'")
'''