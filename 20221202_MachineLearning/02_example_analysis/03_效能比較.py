import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
import time
import pylab as plt
import seaborn as sns

# time.time(): time stamp, 1970/01/10 ~ now 所經過的秒數
# 為什麼tensorflow要做跟numpy一樣的事呢? 兩者的差異性為何?
# 顯卡12G的RAM, 10億會發生 failed to allocate memory 錯誤, OOM: out ot memory, 記憶體不足
batch = 500_000_000

# numpy
t1n = time.time()
#　plt.subplot(1, 2, 1)
n = np.random.normal(size=batch)
t2n = time.time()
# sns.histplot(n)
print(f'numpy(CPU):\n總共花費 {t2n - t1n}秒')

# tensorflow
t1t = time.time()
# plt.subplot(1, 2, 2)
t = tf.random.normal([batch])
t2t = time.time()
# sns.histplot(t)
print(f'tensorflow(GPU):\n總共花費 {t2t - t1t}秒')

# plt.show()

