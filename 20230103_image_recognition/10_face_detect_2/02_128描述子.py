import cv2
import dlib
import numpy as np
import pylab as plt
# 只能有一張臉
path_img = 'E:\project\data\img\jpg\\arina1.jpg'
img = cv2.imdecode(np.fromfile(path_img, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
# 人臉偵測器
detector_face = dlib.get_frontal_face_detector()
faces = detector_face(img, 1)

# http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
# 形狀/特徵偵測器
detector_shape = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2
# 人臉辨識模型, 將 68特徵轉成 128描述子
detector_recognition = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

for face in faces:
    shape = detector_shape(img, face)
    descriptor = detector_recognition.compute_face_descriptor(img, shape)
    a = np.asarray(descriptor)
    print(a)

    # shape.num_parts 特徵數
    # for i in range(shape.num_parts):
    #     x = shape.part(i).x
    #     y = shape.part(i).y
    #     cv2.circle(img, (x,y), 5, (0,0,255), -1)

plt.imshow(img[:,:,::-1])
plt.axis('off')
plt.show()