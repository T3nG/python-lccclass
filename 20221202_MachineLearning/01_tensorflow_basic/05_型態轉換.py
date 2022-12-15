import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

a_int32 = tf.constant(100)
b_float32 = tf.constant(10.)
b_to_int32 = tf.cast(b_float32, tf.int32)
print(a_int32 + b_to_int32)

a_to_float32 = tf.cast(a_int32, tf.float32)
print(b_float32 + a_to_float32)

# 轉換後, 是產生一個新的 Tensor物件, 不是更改a_int32, 所以 a_int32還是整數
print(tf.cast(a_int32, tf.float32) + b_float32)
# print(a_int32 + b_float32)  # error
