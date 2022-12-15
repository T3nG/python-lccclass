import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import random
import cv2
import keras
from keras.applications.vgg19 import preprocess_input

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
path = 'flowers_17'
pairs = {}
for file, d in zip(sorted(os.listdir(path)), dirs):
    filepath = os.path.join(path, file)
    pairs.update({filepath: d})

testRun = 100
match = 0
accuracy = 0
misMatch = []
model = keras.models.load_model('model_flower_17')
for i in range(testRun):
    filepath, flower = random.choice(list(pairs.items()))
    img = cv2.imdecode(
        np.fromfile(filepath, dtype=np.uint8),
        cv2.IMREAD_UNCHANGED)
    x = cv2.resize(img, (224, 224), interpolation=cv2.INTER_LINEAR)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    out = model.predict(x)
    idx = out[0].argmax()  # 取最大值的索引
    filename = filepath.replace('flowers_17\\', '')
    # print(f'偵測第 {i+1} 次')
    # print(f'隨機選中的原始圖與其種類: {filename} : {flower}')
    # print(f'模型偵測的種類: {flowers[idx]}')
    if flower == flowers[idx]:
        match += 1
    else:
        misMatch.append([filename, flower, flowers[idx]])
print(f'偵測準確率: {match/testRun:.2%}')
for m in misMatch:
    print(f'判斷錯誤的組合: {m[0]} : {m[1]}, 模型偵測: {m[2]}')