# http://mahaljsp.asuscomm.com/index.php/2022/10/08/%e6%b3%a2%e5%a3%ab%e9%a0%93%e6%88%bf%e5%83%b9%e9%a0%90%e6%b8%ac/
# 皮爾森積差 = 共變異數，又稱為協方差(Convariance) / 不是標準差, 因為沒有除以 n 再開根號 (X 偽標準差 * Y 偽標準差)
import numpy as np
np.random.seed(1)
x = np.random.randint(1, 100, 10)
y = np.random.randint(1, 100, 10)
x_mean = x.mean()
y_mean = y.mean()
print('x: ', x)
print('y: ', y)
print('x_mean: ', x_mean)
print('y_mean: ', y_mean)

convariance = np.sum((x - x_mean)*(y - y_mean))
xd = np.sqrt(np.sum(np.square(x-x_mean)))
yd = np.sqrt(np.sum(np.square(y-y_mean)))

pearson = convariance / (xd*yd)
print(f'皮爾森積差: {pearson}')

import pandas as pd
df = pd.DataFrame(data={'x': x, 'y': y})
print('df自動計算皮爾森積差: ')
print(df.corr())
