# pip install TensorFlow
# TensorFlow 有 1.0 及 2.0版本, 網路上大都是 1.0教學, 須注意
# 若有看到 tf.session 就是 1.0, 請直接跳過
# TensorFlow 又分僅支援CPU 或 支援CPU/GPU 的版本, 預設是都支援
# tensorflow 2.11.0有bug, 無法抓到gpu, 降版本到2.10.1即刻
# File\close project\關閉pycharm, 到專案目錄下刪除venv, .idea, 重新啟動pycharm, 新專案, 選原目錄 create from existing source
# 1. File\Setting\專案\python interpreter\+\tensorflow 2.10.1
# 2. pip install tensorflow==2.10.1

# TensorFlow 的訊息輸出機制, 分成 4 個等級
# 0. INFO 通知
# 1. WARNING 警告
# 2. ERROR 錯誤
# 3. FATAL 穩死的

import os
# 必須寫在 import tensorflow 之前, 否則無效, 只顯示 error, fatal 訊息, 在colab環境不須設定, 只有出錯才會顯示log
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 只顯示 info, warning

# 顯示硬體狀況
gpus = tf.config.list_physical_devices(device_type='GPU')
print(gpus)
cpus = tf.config.list_physical_devices(device_type='CPU')
print(cpus)

# 限定硬體使用, 只能擇一使用
# 如果沒有設定的話, 有GPU時, 預設啟動GPU, 若沒有則啟動CPU
# tf.config.set_visible_devices(gpus[0], device_type='GPU')
# tf.config.set_visible_devices(cpus[0], device_type='CPU')  # device_type預設是 CPU, 可以去掉

# 常數類別 / 常數張量 tf.Tensor
s = tf.constant(10)  # 常數張量
print('常數類別: \n', s)
# print(s.numpy())
# print(s.shape)
# print(s.dtype)

# 變數類別 tf.Variable
x = tf.Variable(10)
print('變數類別: \n', x)

'''
class Pokemon():
    pass
p1 = Pokemon()  # 由類別名稱去產生出一個物件

class Variable():
    def __init__(self, value):
        self.value = value
x = Variable(10)

class Tensor():
    def __init__(self, value):
        self.value = value
s = Tensor(10)  # ?
# Tensor() 不可以產生物件, 須由 tf.constant()這個方法來建立 Tensor物件
'''