# pip install opencv-python Pillow matplotlib
# ref: http://mahaljsp.asuscomm.com/index.php/2020/11/25/%e5%b9%be%e4%bd%95%e8%ae%8a%e6%8f%9b/
import time
import cv2

# cam = cv2.VideoCapture(0)  # 抓取第一台 web cam 的影像
path = 'E:\\project\\data\\video\\gemsky.mp4'
cam = cv2.VideoCapture(path)  # 路徑自己改
# 必須 web cam有支援才有效
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# used to record the time when we processed last frame
prev_frame_time = 0
# used to record the time at which we processed current frame
new_frame_time = 0
while True:
    t1 = time.time()
    ret, frame = cam.read()  # ret:True 抓取成功
    frame = cv2.resize(frame, (1024,768), interpolation=cv2.INTER_LINEAR)
    font = cv2.FONT_HERSHEY_SIMPLEX
    new_frame_time = time.time()
    # Calculating the fps
    # fps will be number of frame processed in given time frame
    # since their will be most of time error of 0.001 second
    # we will be subtracting it to get more accurate result
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    # converting the fps into integer
    fps = int(fps)

    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = str(fps)

    # putting the FPS count on the frame
    cv2.putText(frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('video', frame)
    # waitKey(ms) 等待鍵盤輸入
    if cv2.waitKey(1) & 0xFF == 27:  # 0xFF == 27 當 ESC鍵被按下
        break
    t2 = time.time()
    total = t2 - t1
    # 修正播放速度
    # if total < 0.033:
    #     time.sleep(0.033 - total)
cam.release()
cv2.destroyAllWindows()
