# http://mahaljsp.asuscomm.com/index.php/2020/12/24/tf2-%e5%9f%ba%e6%9c%ac%e8%aa%9e%e6%b3%95/
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

# Tensor: 張量
# 常數類別, 使用constant()建立Tensor物件
# constant會自動產生 operation, value_index等資料
a = tf.constant(10)
a = tf.constant(100)  # 產生新物件, 上面的物件會被消滅, 不是裡面的值變了, 可能需要花費 1us, 產生太多會消耗非常多資源
# 變數類別, 直接使用類別建立Variable物件
b = tf.Variable(20)

# a.assign(100)  # 不可變更
b.assign(100)  # 可以變更, 不產生新物件, 所以效能比較高, 因為產生一個物件, 需消耗大量的cpu資源
b = 200  # 此時是產生一個 python int32物件

print(a)
# print(a.numpy()) 抓取值
# print(a.shape)
# print(a.dtype)
print(b)
