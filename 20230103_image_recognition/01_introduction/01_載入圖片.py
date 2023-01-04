# pip install opencv-python matplotlib
# ref: http://mahaljsp.asuscomm.com/index.php/2020/11/22/%e6%a9%9f%e5%99%a8%e8%be%a8%e5%88%a5%e7%b8%bd%e8%a6%bd/
# ref: http://mahaljsp.asuscomm.com/index.php/2020/11/18/opencv_brief/
# AI 圖片辨識: 比較著重在步驟, VGG19 到現在都還在改版
# AI 深度學習: 比較重視演算法
# AI 強化學習: 深度學習的另一個大分支
# CPU 只有一台計算機
# GPU 顯卡, 有上千或上萬台計算機
# TPU 由 google開發的晶片, 不須跟記憶體交換資料, 速度更快
# AI 手機: SOC(約相當於單晶片的CPU)裡加入TPU晶片, 也會很耗電, 所以可行性很低
# 浮點運算器: 計算小數用的晶片, 目前都加入到CPU中
import cv2

# cv2.imread() 讀進來的為numpy的陣列格式, 圖形顏色為 BGR
img = cv2.imread('tiger.jpg')
# print(img.shape)  # (3000, 4000, 3)
# 原始圖檔的高及寬, 作為resize維持原比例的參考
h, w, _ = img.shape
# 長寬要用tuple()
# 1024 * h / w = x
new_width = 1024
new_height = int(new_width * h / w)
img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)  # 內部線性差值
cv2.imshow('tiger', img)
cv2.waitKey(0)
