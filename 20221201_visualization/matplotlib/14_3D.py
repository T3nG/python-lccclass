import pylab as plt
import numpy as np

# 底下的套件雖未用到, 但一定要import , 否則無法使用 3d projection
# 使用 OpenGL (調用GPU高速顯圖) 的投影技術, http://mahaljsp.asuscomm.com/index.php/2020/12/30/pyopengl/
from mpl_toolkits.mplot3d import Axes3D

ax = plt.subplot(111, projection='3d')  # 寫法1, 1 ,1等同, 但只能9以下 991

x = np.linspace(1, 10, 10)
y = [5, 6, 7, 8, 2, 5, 6, 3, 7, 2]
z = np.zeros(10)

dx = np.ones(10)
dy = np.ones(10)
dz = np.linspace(1, 10, 10)

ax.bar3d(x, y, z, dx, dy, dz, shade=True, color='b')
plt.show()
