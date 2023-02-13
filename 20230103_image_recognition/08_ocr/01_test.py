import cv2
import pytesseract
import numpy as np
from urllib.request import urlopen

url = 'http://mahaljsp.asuscomm.com/wp-content/uploads/2020/12/scikt_data.jpg'
conn = urlopen(url)
img = np.asarray(bytearray(conn.read()), dtype=np.uint8)
img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)

#lang: chi_sim 簡體, chi_tra 繁體, eng 英文, fra 法文, 詳細支援的語言請參照官網
# pytesseract 吃的圖片格式為 numpy
result = pytesseract.image_to_string(img, lang='eng')
print(result)


# OCR辨識時, 最好將圖片轉成256灰階, 若不行, 再轉成 二值化
img2 = cv2.imdecode(np.fromfile('1.jpg', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# img2 = cv2.imdecode(np.fromfile('1.jpg', dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
result2 = pytesseract.image_to_string(img2, lang='chi_tra')
print(result2)

cv2.imshow('test', img)
cv2.imshow('test2', img2)
cv2.waitKey(0)
