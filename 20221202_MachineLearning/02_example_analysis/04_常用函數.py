# http://mahaljsp.asuscomm.com/index.php/2022/11/14/tf2-%e5%b8%b8%e7%94%a8%e5%87%bd%e6%95%b8/
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
import time


# a = np.random.randint(1, 100, 10)
# print('a: ', a)
# # print(tf.sqrt(a))  # 整數無法開根號, 需轉成小數
# print('a根號: ', tf.sqrt(tf.cast(a, tf.float32)))
# print('a平方: ', tf.square(a))
# print()
#
# b = np.random.random([10])
# print('b: ', b)
# print('b根號: ', tf.sqrt(b))
# print('b平方: ', tf.square(b))

batch = 100_000

# 找出陣列中符合條件的值
tf.random.set_seed(1)
c = tf.random.uniform([batch])
# print('c: ', c)
# print()


print('以下為使用where的時間差異')

# tensorflow: where
t1t = time.time()
t = tf.where(c <= 0.5)  # # 輸出為索引值
t2t = time.time()
print(f'GPU耗時: {t2t - t1t}秒')
print(len(t))

print()

# numpy: where
# numpy 也有 where, 使用CPU去執行C語言, 但還是比GPU慢
t1n = time.time()
n = np.where(c <= 0.5)
t2n = time.time()
print(f'CPU耗時: {t2n - t1n}秒')
print(len(n[0]))

print()

# 若沒有where的功能, 要怎麼找到符合條件的值呢? (一樣輸出索引值)
# 因為使用python迴圈, 非常緩慢
len = 0
t1p = time.time()
for i, x in enumerate(c):
    if x <= 0.5:
        len += 1
t2p = time.time()
print(f'python for耗時: {t2p - t1p}秒')
print(len)

# 導數, 偏導數
# http://mahaljsp.asuscomm.com/index.php/2021/01/09/%e5%be%ae%e5%88%86/
# 下堂課講解