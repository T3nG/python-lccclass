# pip install tensorflow==2.10.1 matplotlib seaborn
# normal: 常態分布, 為統計學名詞
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import pylab as plt
import seaborn as sns
import numpy as np

# 一次要存取或計算的量, 太大的話會造成顯卡記憶體不足, 需要進行測試
batch = 10000
# x = np.linspace(1, batch, batch)
x = tf.random.normal([batch])
y = tf.random.normal([batch])
# 常態分布的意義, 以圖像表達, matplotlib實際描繪點的位置, seaborn統計每個區域的次數
# plt.scatter(x, y, s=0.1)  # s: 改變點點的大小
# sns.histplot(x)
# plt.savefig('xxx.jpg') 可將畫好的圖存下來, 上傳到自己的網站, 作為筆記
plt.show()
# print(y.numpy())

