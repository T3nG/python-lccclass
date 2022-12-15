import numpy as np
# 32位元的意思
a=np.array([1,2,3,4,5], dtype=np.float32)
print(a)

b=np.zeros([10], dtype=np.int32)
print(b)

c=np.zeros([10], dtype=np.int8)*200
# print 的時候自動轉換成合適的範圍
print(c.dtype)

'''
numpy 型別
np.int8  : -128 ~ 127     (-2^7 ~ 2^7-1)
np.int16 : -32768 ~ 32767 (-2^15 ~ 2^15-1) 
np.int32 : -2^31 ~ 2^31-1
np.int64 : -2^63 ~ 2^63-1

np.uint8  : 0 ~ 255   (0 ~ 2^8-1)
np.uint16 : 0 ~ 65536 (0 ~ 2^16-1)
np.uint32 : 0 ~ 2^32-1
np.uint64 : 0 ~ 2^64-1
沒有負數(unsigned)

np.float16
np.float32(精準到小數第7位)
np.float64(精準到小數第15數)
bool, string
'''