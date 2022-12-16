from keras.applications import VGG19

model = VGG19(weights='imagenet', include_top=False)  # include_top=False 不使用輸出層(23 24 25 26層)
for i, layer in enumerate(model.layers):
    print(i+1, layer.name, layer)
'''
1 input_1 <keras.engine.input_layer.InputLayer object at 0x0000019BF9459108>
2 block1_conv1 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019BFBCEC548>
3 block1_conv2 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019BFBD2C508>
4 block1_pool <keras.layers.pooling.max_pooling2d.MaxPooling2D object at 0x0000019BFBDB4E88>
5 block2_conv1 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019B97F8B788>
6 block2_conv2 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019B97F8B4C8>
7 block2_pool <keras.layers.pooling.max_pooling2d.MaxPooling2D object at 0x0000019B97F967C8>
8 block3_conv1 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019B97FA1108>
9 block3_conv2 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019B97F9DB48>
10 block3_conv3 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019B97FA12C8>
11 block3_conv4 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019B97FA0E88>
12 block3_pool <keras.layers.pooling.max_pooling2d.MaxPooling2D object at 0x0000019BF5B04248>
13 block4_conv1 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019BF981CC48>
14 block4_conv2 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019BFB6C0608>
15 block4_conv3 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019B97FBE6C8>
16 block4_conv4 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019B97FC3FC8>
17 block4_pool <keras.layers.pooling.max_pooling2d.MaxPooling2D object at 0x0000019B97FC5D88>
18 block5_conv1 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019B97FD4548>
19 block5_conv2 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019B97FCF648>
20 block5_conv3 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019B97FCFAC8>
21 block5_conv4 <keras.layers.convolutional.conv2d.Conv2D object at 0x0000019BF9EAE208>
22 block5_pool <keras.layers.pooling.max_pooling2d.MaxPooling2D object at 0x0000019BFBD77B48>
'''