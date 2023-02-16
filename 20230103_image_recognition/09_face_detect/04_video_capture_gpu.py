# 需下載人臉訓練資料, .dat放入專案下 http://mahaljsp.asuscomm.com/files/mmod_human_face_detector.dat.bz2
import time

import cv2
import dlib
# VideoCapture('0')  讀取相機
video_path = 'E:\project\data\\video\gemsky_2.mp4'
video = cv2.VideoCapture(video_path)
# 設定從第幾個毫秒開始撥放 (100秒)
# video.set(cv2.CAP_PROP_POS_MSEC, 100000)
# 捲積神經人臉偵測器
detector = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')
while True:
    t1 = time.time()
    success, img = video.read()
    h, w, _ = img.shape
    w1 = 400
    h1 = int(w1*h/w)
    img = cv2.resize(img, (w1, h1), interpolation=cv2.INTER_LINEAR)

    faces = detector(img, 1)
    for i, d in enumerate(faces):
        f = d.rect
        x1 = f.left()
        y1 = f.top()
        x2 = f.right()
        y2 = f.bottom()
        img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('video', img)
    t2 = time.time()
    spent = t2 - t1
    # 29.7fps
    # 1000ms/29.7 => 33.67 ms/frame
    if spent < 33:
        key = cv2.waitKey(int(33 - spent))
        if key == ord('q') or key == 27:
            break
