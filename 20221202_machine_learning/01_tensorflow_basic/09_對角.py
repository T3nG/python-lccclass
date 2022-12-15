import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

# 產生 5*5 陣列, 從左上到右下給1
# 動態規劃使用, 5*5 總共有 70 種走法
a = tf.eye(5)
print(a)
