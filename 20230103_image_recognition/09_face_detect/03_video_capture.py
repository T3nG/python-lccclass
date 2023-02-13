import cv2
import dlib
# VideoCapture('0')  讀取相機
video_path = 'E:\project\data\\video\gemsky_2.mp4'
video = cv2.VideoCapture(video_path)
detector = dlib.get_frontal_face_detector()
while True:
    success, img = video.read()
    h, w, _ = img.shape
    w1 = 1024
    h1 = int(w1*h/w)
    img = cv2.resize(img, (w1, h1), interpolation=cv2.INTER_LINEAR)

    faces, scores, indexes = detector.run(img, 1, 0.5)

    for i, face in enumerate(faces):
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        txt = f'{indexes[i]}({scores[i]:2.2f})'
        # 0.4 => 縮放比例, 1 => 粗細
        cv2.putText(img, txt, (x1, y1 - 2), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow('video', img)
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break