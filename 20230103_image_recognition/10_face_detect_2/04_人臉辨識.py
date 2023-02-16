import pickle
import cv2
import dlib
import numpy as np
import mysql.connector as mysql
from G import G

def get_descriptor(img):
    # if not gpu, remove [0].rect
    try:
        return np.asarray(
            detector_recognition.compute_face_descriptor(img, detector_shape(img, detector_face_gpu(img, 0)[0].rect))
        )
    except:
        return None

detector_face_gpu = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')
detector_shape = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
detector_recognition = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

conn = mysql.connect(
    host=G.host,
    user=G.user,
    password=G.password,
    database=G.database
)
cur = conn.cursor()
cmd = 'select * from 人臉資料'
cur.execute(cmd)
rows = cur.fetchall()
cur.close()
conn.close()

descriptors = []
candidates = []
for row in rows:
    name = row[1]
    descriptor = pickle.loads(row[2])  # 從BLOB轉回 np.array
    candidates.append(name)
    descriptors.append(descriptor)
# print(candidates)
# print(descriptors)

path_testimg = 'E:\\project\\data\\img\\face_detect\\test\\hebe_6.jpg'
path_testimg2 = 'E:\\project\\data\\img\\face_detect\\db\\arina_6.jpg'
img = cv2.imdecode(np.fromfile(path_testimg2, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
img = img[:,:,::-1]
target = get_descriptor(img)
# print(target)
# distance = np.lianlg.norm(target - descriptors[0])  # 線性代數
distance = [np.linalg.norm(target - d) for d in descriptors]
min_index = np.argmin(distance)
print(min_index)
print(f'偵測到是: {candidates[min_index]}')
