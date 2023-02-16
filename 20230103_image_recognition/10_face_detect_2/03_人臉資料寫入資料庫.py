# 啟動天眼計畫的訓練
# pip install mysql-connector-python
import os
import cv2
import dlib
import numpy as np
import pylab as plt
import mysql.connector as mysql
from G import G
detector_face = dlib.get_frontal_face_detector()

# 使用 gpu偵測人臉時, 圖片大小若超過 1200萬像素(4000*3000)
# 連 RTX-3080Ti 12G都會 out of memory
# http://mahaljsp.asuscomm.com/files/mmod_human_face_detector.dat.bz2
# 載入模型切換到 gpu會花一些時間
detector_face_gpu = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')
detector_shape = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
detector_recognition = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

def get_descriptor(img):
    # if not gpu, remove [0].rect
    try:
        return np.asarray(
            detector_recognition.compute_face_descriptor(img, detector_shape(img, detector_face_gpu(img, 0)[0].rect))
        )
    except:
        return None

# path_img = 'E:\project\data\img\jpg\\arina1.jpg'
# img = cv2.imdecode(np.fromfile(path_img, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
# print(get_descriptor(img))

path_db = 'E:\project\data\img\\face_detect\db'
# database table 人臉資料, id, name, descriptor (BLOB)
conn = mysql.connect(
    host=G.host,
    user=G.user,
    password=G.password,
    database=G.database
)
cur = conn.cursor()


for file in os.listdir(path_db):
    img = cv2.imdecode(np.fromfile(os.path.join(path_db, file), dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    h, w, _ = img.shape
    r = w / h
    if w > 2000:  # 依顯卡記憶體大小做調整
        w = 2000
        h = int(w / r)
        img = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)
    name = file.split('_')[0]
    img = img[:,:,::-1]  # 轉成RGB
    descriptor = get_descriptor(img)
    if descriptor is not None:
        dump = descriptor.dumps()  # 轉成 BLOB
        cmd = 'insert into 人臉資料 (name, descriptor) values (%s, %s)'
        cur.execute(cmd, (name, dump))
        print(f'正在寫入 {file} ...')
        conn.commit()
cur.close()
conn.close()
