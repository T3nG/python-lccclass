import cv2
import dlib
import numpy as np
import pylab as plt

img_path = 'E:\project\data\img\jpg\\face25.jpg'
img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
h, w, _ = img.shape
w1 = 1024
h1 = int(w1*h/w)
img = cv2.resize(img, (w1, h1), interpolation=cv2.INTER_LINEAR)

# 產生人臉偵測器
detector = dlib.get_frontal_face_detector()
# 第二個參數為反取樣次數, 預設為0, 圖片若太小, 可以設定高一點, 但偵測時間較久, 最後一個數值是分數, 大於才顯示出來
# faces 每張臉的座標
# scores 每張臉的分數
# indexes 每張臉的方向 https://github.com/davisking/dlib/blob/master/dlib/image_processing/frontal_face_detector.h
faces, scores, indexes = detector.run(img, 1, 0.5)

for i, face in enumerate(faces):
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    txt = f'{indexes[i]}({scores[i]:2.2f})'
    # 0.4 => 縮放比例, 1 => 粗細
    cv2.putText(img, txt, (x1, y1-2), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 255), 2)
cv2.imshow('face', img)
cv2.waitKey(0)
