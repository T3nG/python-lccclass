import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import time

batch = 100_000_000
epoch = 500_000
incircle = 0

# tf.function 改由 graph計算(圖計算), 模擬 tf1的session 可以加速計算的效能, 但不支援某些功能
# 比如把 incircle與pi放進cal()時, 會顯示錯誤, 不支援+
# 加上 tf.function 有什麼差異呢?
# O: 每個世代 0.015~0.018秒, 總耗時 17.7468秒
# X: 每個世代 0.015~0.019秒, 總耗時 19.2135秒


@tf.function
def cal():
    # [2, batch]: 產生兩組數字, x, y
    points = tf.random.uniform([2, batch], dtype=tf.float64)
    dist = tf.sqrt(tf.square(points[0]) + tf.square(points[1]))
    return dist


t1 = time.time()
for e in range(epoch):
    t3 = time.time()
    dist = cal()
    incircle += tf.where(dist < 1).shape[0]
    pi = incircle / ((e + 1) * batch) * 4
    t4 = time.time()
    print(f'\rEpoch: {e+1:07d}: {t4-t3:.5f}秒, pi={pi}', end='')
t2 = time.time()
print(f'\n共耗時: {t2 - t1}秒')

# 準確率受到限制, uniform其實也不是很平均, 老師測試結果(epoch 500_000, 3小時), 3.1415926 5 突破不了小數第八位
# 500_000世代 3.1415925594976  7930.885339秒
