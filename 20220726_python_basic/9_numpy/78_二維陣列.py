import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.mean())
print(a.shape)  # (2,3) => (列, 行)

# 三維陣列
b = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18], [19, 20, 21],[22, 23, 24]]
])
print(b)
print(b.mean()) # 算術平均數
print(b.shape)

# 四維陣列 : 並不是四度空間, 空間只有三度, 沒有四度, 別那麼沒水準
# 四維 : 比如加上時間, 那麼四維就是指速度
# 五維 : 就變成了加速度

c=np.zeros([3,5]) # 3列5行
c2=np.zeros([3,5,3]) #? 3元素(3行?)5列 3組?
print(c)
print(c2)