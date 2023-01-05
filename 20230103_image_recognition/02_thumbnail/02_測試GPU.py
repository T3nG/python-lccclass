# pip install tensorflow==2.10.1
# 2.11.0以上有bug, 無法在windows啟動GPU
# 網路上的教學大都是 tf 1.0的版本, 不要學, 有 session就是 1.0
# tf 2.1 開始
# tensorflow 支援 GPU/CPU的版本, 會依有無顯卡自動切換
# tensorflow-cpu 僅支援 CPU
# tensorflow-gpu 僅支援 GPU
import tensorflow as tf
gpus = tf.config.list_physical_devices(device_type='GPU')
cpus = tf.config.list_physical_devices(device_type='CPU')
print(gpus)
print(cpus)
