import os

from PIL import Image
from keras.applications import VGG19
from keras.applications.vgg19 import preprocess_input
from keras.optimizers import SGD

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import shutil
import keras
import cv2
import numpy as np
import tensorflow as tf


def gram_matrix(x):
    x = tf.reshape(x, (x.shape[1], x.shape[2], x.shape[3]))
    x = tf.transpose(x, (2, 0, 1))  # 對調RGB的值
    # 將 x轉成二維
    features = tf.reshape(x, (tf.shape(x)[0], -1))  # -1 展開
    gram = tf.matmul(features, tf.transpose(features))
    return gram


def style_loss(style_feature, combination_feature):
    S = gram_matrix(style_feature)
    C = gram_matrix(combination_feature)
    channel = 3
    size = height*width
    return tf.reduce_sum(tf.square(S-C)) / (4.0 * (channel**2)*(size**2))


def compute_loss_and_grads(combination_image, base_image, style_image):
    with tf.GradientTape() as tape:
        loss = tf.zeros(shape=())  # 純數字的tensorflow, 不是陣列
        base_features = model(base_image)
        base_feature = base_features[content_layer_name]
        combination_features = model(combination_image)
        combination_feature = combination_features[content_layer_name]
        # 因為square(cm-base)再加總, 非常的大, 所以要讓
        loss = loss + content_weight*tf.reduce_sum(tf.square(combination_feature-base_feature))
        # 計算風格照與合成照的損失
        style_features=model(style_image)
        for layer_name in style_layer_names:
            style_feature = style_features[layer_name]
            combination_feature = combination_features[layer_name]
            style_loss_values = style_loss(style_feature, combination_feature)
            loss += (style_weight / len(style_layer_names))*style_loss_values
    grads = tape.gradient(loss, combination_image)
    return loss, grads


def deprocess_image(img):
    # 將圖片調亮
    img = img.reshape(height, width, 3)  # 降維
    # 調亮RGB顏色的亮度, 每張圖不一樣, 得測試
    img[:, :, 0] += 103.939
    img[:, :, 1] += 116.779
    img[:, :, 2] += 123.68
    img = img[:, :, ::-1]  # 將RGB轉BGR
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 有做深度copy, 產生出另一個新的陣列
    # 將每個點的顏色值, 強迫介於0~255之間
    img = np.clip(img, 0, 255).astype(np.uint8)
    return img

model = VGG19(weights="imagenet", include_top=False)
output_dict=dict([layer.name, layer.output] for layer in model.layers)
model = keras.Model(inputs=model.inputs, outputs=output_dict)
# 風格照與合成圖
style_layer_names = [
    "block1_conv1",
    "block2_conv1",
    "block3_conv1",
    "block4_conv1",
    "block5_conv1"
]
# 原始圖 block5_conv2 與合成圖 block5_conv2計算損失, 可偵測圖片的紋理
content_layer_name = "block5_conv2"
total_variation_weight = 1e-6
style_weight = 1e-6
content_weight = 1e-6

# 原始圖
base_path = "dog.jpg"
base_image = np.array(Image.open(base_path))
height = 600  # 以顯卡記憶體不會爆掉為主(可設置小一點)
width = 800
# oh, ow = base_image.shape[:2]
# width = int(ow*height/oh)
base_image = cv2.resize(base_image, (width, height), interpolation=cv2.INTER_LINEAR)
# cv2.imshow("dog", base_image)
# cv2.waitKey(0)
# 最前面加入一個空的維度是為了儲存權重
base_image = np.expand_dims(base_image, axis=0)
# 將每一個顏色值與其平均值相減, 產生介於 0左右二邊的常態分佈, 此時是 float的格式(由np.uint8轉來)
base_image = preprocess_input(base_image)

# 風格照
style_path = "starry_night.jpg"
style_image = np.array(Image.open(style_path))
height = 600
width = 800
# oh, ow = style_image.shape[:2]
# width = int(ow*height/oh)
style_image = cv2.resize(style_image, (width, height), interpolation=cv2.INTER_LINEAR)
# cv2.imshow("starry_night", style_image)
# cv2.waitKey(0)
style_image = np.expand_dims(style_image, axis=0)
style_image = preprocess_input(style_image)

# 組合, 以原始照為底
combination_image = tf.Variable(base_image)
iteration = 4000  # 測試完成後改成4000
# 優化器: SGD 隨機梯度下降, 一開始學習率為 100, 每訓練 100次就減少 4%
optimizer = SGD(
    # tensorflow keras
    tf.keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate=100.0, decay_steps=100, decay_rate=0.96
    )
)
if os.path.exists("output"):
    shutil.rmtree("output")
os.mkdir("output")

# 迭代開始
for i in range(1, iteration+1):
    loss, grads = compute_loss_and_grads(combination_image, base_image, style_image)
    # 產生合成圖的地方
    optimizer.apply_gradients([(grads, combination_image)])
    if i%100 == 0:
        print(f'Iteration {i}:loss={loss:.2f}')
        img = deprocess_image(combination_image.numpy())
        file = f'combination_at_iteration_{i}.png'
        keras.utils.save_img(os.path.join("output", file), img)
        cv2.imshow("dog", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        cv2.waitKey(5)  # ms
cv2.waitKey(0)
