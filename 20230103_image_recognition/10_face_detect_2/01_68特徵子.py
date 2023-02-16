import cv2
import dlib
import numpy as np
import pylab as plt
# 劉亦菲
path_img = 'E:\project\data\img\jpg\\arina1.jpg'
img = cv2.imdecode(np.fromfile(path_img, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
# 人臉偵測器
# detector_face = dlib.get_frontal_face_detector()
# faces = detector_face(img, 1)

# http://mahaljsp.asuscomm.com/files/mmod_human_face_detector.dat.bz2
detector_face_gpu = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')
faces = detector_face_gpu(img, 1)

# http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
# 形狀/特徵偵測器
detector_shape = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

for face in faces:
    face = face.rect  # if gpu
    # x1 = face.left()
    # y1 = face.top()
    # x2 = face.right()
    # y2 = face.bottom()
    # # print(x1, y1, x2, y2)
    # img = cv2.rectangle(img, (x1, y1), (x2, y2), color=(255,0,0), thickness=10)

    shape = detector_shape(img, face)
    # shape.num_parts 特徵數
    for i in range(shape.num_parts):
        x = shape.part(i).x
        y = shape.part(i).y
        cv2.circle(img, (x,y), 5, (0,0,255), -1)

plt.imshow(img[:,:,::-1])
plt.axis('off')
plt.show()