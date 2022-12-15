import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf


a = tf.constant(10)  # 整數預設為 int32
b = tf.constant(10.)  # 小數預設為 float32
'''
整數: tf.int8(-128~127), tf.int16(-32768~32767), tf.int32(-21億~21億), tf.int64(-2^64~2^64)
     tf.uint8, tf.uint16, tf.uint32, tf.uint64 , 沒有負值, 只有正值(unsigned)
小數: tf.float16(幾乎沒有在用), tf.float32(精準到小數第7位, 包含'.'), tf.float64(精準到小數第15位, 包含'.')
100.123456789 (1234156可信, 7不可信)
另外還有 string 型態
'''

# c = tf.constant(129, dtype=tf.int8)  # 會溢位
c = tf.constant(129, dtype=tf.uint8)
d = tf.constant("abcdef", dtype=tf.string)  # 字串會自己指定tf.string

print(a)
print(b)
print(c)
# 使用tensorflow時, 如果GPU, 則會直接啟動GPU計算
# 為什麼要限制只使用CPU? 因為GPU運算時, 需進行切換, 非常耗時, 簡單的運算, 反而CPU比較快
