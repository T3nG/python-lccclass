from urllib.request import urlopen
from sdk.IvanCv import IvanCv as cv
import numpy as np
import cv2

# blocked access
# url = 'https://static.javatpoint.com/tutorial/tensorflow/images/tensorflow-vs-pytorch.png'
# url = 'https://www.springboard.com/blog/wp-content/uploads/2021/01/pytorch-vs-tensorflow-how-do-they-compare.png'
# url = 'https://intellipaat.com/blog/wp-content/uploads/2020/09/PyTorch-vs-TensorFlow-Big-793x270.jpg'

# access granted
# url = 'https://img-blog.csdnimg.cn/img_convert/2b9316b9e525582b285fe868d788521b.png'
url = 'https://149695847.v2.pressablecdn.com/wp-content/uploads/2020/08/create-machine-learning-and-deep-learning-models-using-pytorch-and-tensorflow.jpg'
# url="http://mahaljsp.asuscomm.com/tomcat/pictures/primitive/2023/20230117_Philippines_day4_Coron/IMG_20230117_143441.jpg"

conn = urlopen(url)
img = np.asarray(bytearray(conn.read()), dtype=np.uint8)  # 讀進來的為壓縮過的圖檔
img = cv2.imdecode(img, cv2.IMREAD_COLOR)  # 解壓縮
img = cv.resize(img, scale=0.8)
cv2.imshow('img', img)
cv2.waitKey(0)
