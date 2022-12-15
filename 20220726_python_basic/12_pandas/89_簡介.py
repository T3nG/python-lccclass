# pip install pandas
# 安裝 pyqt5時, 就會自動安裝了
# pandas 是模擬 Excel 的資料格式
# pandas 有兩種資料格式, Series / DataFrame

import pandas as pd
import numpy as np

# 傳入Series的格式, 可以是list
s1=pd.Series([10,20,30,40,50])
print(s1[0])
for s in s1:
    print(s)
for i in range(len(s1)):
    print(s1[i])

# 傳入Series的格式, 可以是numpy陣列


'''
print(s1)
results:
0    10
1    20
2    30
3    40
4    50
dtype: int64
前面的0 1 2 3 4稱為索引
'''

'''
List
ls=[1,2,3,4,5]
ls.append(10)

Numpy Array
a=np.array([1,2,3,4,5])

Pandas Series
'''
s2=pd.Series(np.array([22,33,44,55,66]))
print(s2)
# 以上為多此一舉嗎?
s3=pd.Series([22,33,44,55,66])

import cv2
img=cv2.imdecode(np.fromfile('../Edgerunners-Lucy.jpg',dtype=np.uint8),cv2.IMREAD_UNCHANGED)

# DataFrame只能用二維, img進來的是三維
# s4=pd.DataFrame(img)

# 三維的參數轉成一維,
# for the sake of showing numpy list's incredible speed,
# (compared to default python list)
h, w, c=img.shape
img=img.reshape(h*w*c)
s4=pd.Series(img)
print(s4)