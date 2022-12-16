# http://mahaljsp.asuscomm.com/index.php/2022/10/07/ai%E7%B9%AA%E5%9C%96/
# pip install matplotlib Pillow opencv-python tensorflow==2.10.1
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import cv2
import keras
import numpy as np
import pylab as plt
from keras.applications import VGG19
from keras.applications.vgg19 import preprocess_input
'''
向量內積
m = [a1, b1, c1, d1, e1, f1]
n = [a2, b2, c2, d2, e2, f2]
m.n = a1*a2 + b1*b2 + c1*c2 + d1*d2 + e1*e2 + f1*f2
m.n > 0 : 方向大致相同, 夾角在 0~89度之間
m.n = 0 : 正交, 夾角等於90度
m.n < 0 : 方向相反, 夾角介於 91~?

====================================================

格拉姆矩陣(Gram Matrix)
G(x1, x2, x3) = 
x1x1, x1x2, x1x3
x2x1, x2x2, x2x3
x3x1, x3x2, x3x3
若有n個元素, 計算結果就是 n*n的陣列
'''
# a = np.array([1, 2, 3, 4, 5, 7, 8, 9])
# print(np.outer(a, a))  # Gram Matrix
'''
二維格拉姆
假設 a = [3*5], 先將 a 轉置成 b[5*3], 再把 b扁平化
a的第一個值跟 b相乘, 形成第一列
a的第二個值跟 b相乘, 形成第二列
G([n1*n2]) => n1*n2 * n2*n1 的陣列
'''
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
b = np.transpose(a)
print(f'a陣列: \n', a)
print(f'b轉置: \n', b)  # b.reshape(15) 顯示扁平化的結果
print(f'gram matrix: \n', np.outer(a, b))
# 結果: [(3*5), (5*3)] 的二維陣列
# 格拉姆在取得每個特徵跟其他特徵之間的關聯性, 這個關聯性是在取得某個空間中, 要使用哪個紋理,
# 相同的紋理就會重複出現在不同的位置

# 假設一張圖是 1024*768 產生格拉姆的陣列是多少
# 1024*768, 1024*768 => (786432, 786432) 786432^2 * 3(rgb)
