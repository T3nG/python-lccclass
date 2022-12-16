# http://mahaljsp.asuscomm.com/index.php/2022/10/17/vgg19%e7%89%b9%e5%be%b5/
# pip install matplotlib Pillow opencv-python tensorflow==2.10.1
from keras.applications import VGG19

# VGG19 共有最前面的輸出層, 隱藏層: 5個區塊(block), 最後面的輸出層(全連接層)
# pool: 池化層, 刪除多餘的資料 ; conv: 捲積層
# block1: 2個捲積層
# block2: 2個捲積層
# block3: 4個捲積層
# block4: 4個捲積層
# block5: 4個捲積層
# 隱藏層有 16個捲積層
# 輸出層有 3層 flatten/fc1/fc2
# 所以叫做 VGG19 (19層)
# VGG19比起VGG16 較精準, 較費效能
model = VGG19(weights='imagenet', include_top=True)  # include_top=False 不使用輸出層(23 24 25 26層)
for i, layer in enumerate(model.layers):
    print(i+1, layer.name, layer)
print(model.input)
print(model.output)
'''
1 input_1 <keras.engine.input_layer.InputLayer object at 0x0000027E7D08E588>
2 block1_conv1 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F765808>
3 block1_conv2 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F7AF748>
4 block1_pool <keras.layers.pooling.max_pooling2d.MaxPooling2D object at 0x0000027E2F835CC8>
5 block2_conv1 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F84A648>
6 block2_conv2 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F84A448>
7 block2_pool <keras.layers.pooling.max_pooling2d.MaxPooling2D object at 0x0000027E2F8A7688>
8 block3_conv1 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F8AEFC8>
9 block3_conv2 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F8AAD88>
10 block3_conv3 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F8A0B48>
11 block3_conv4 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F8B8DC8>
12 block3_pool <keras.layers.pooling.max_pooling2d.MaxPooling2D object at 0x0000027E2F8BD5C8>
13 block4_conv1 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F8BBB08>
14 block4_conv2 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F8C6C88>
15 block4_conv3 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F8CF7C8>
16 block4_conv4 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F8CFE08>
17 block4_pool <keras.layers.pooling.max_pooling2d.MaxPooling2D object at 0x0000027E2F8D5C88>
18 block5_conv1 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2FA25748>
19 block5_conv2 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F8D8388>
20 block5_conv3 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F8D5A08>
21 block5_conv4 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000027E2F8D2948>
22 block5_pool <keras.layers.pooling.max_pooling2d.MaxPooling2D object at 0x0000027E2F8C8388>
23 flatten <keras.layers.reshaping.flatten.Flatten object at 0x0000027E2F8B8C48>
24 fc1 <keras.layers.core.dense.Dense object at 0x0000027E2F8CFA48>
25 fc2 <keras.layers.core.dense.Dense object at 0x0000027E2FA2BF88>
26 predictions <keras.layers.core.dense.Dense object at 0x0000027E2FA32AC8>
'''