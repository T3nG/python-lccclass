import numpy as np
import pylab as plt

# mgrid使用整數, 表示步進值
# 若使用虛數, 則表示要切割的等份
# x, y = np.mgrid[1:10:3j, 1:10:3j]
'''
x, y = np.mgrid[1:10:1, 1:10:1]
x
[[1 1 1 1 1 1 1 1 1]
 [2 2 2 2 2 2 2 2 2]
 [3 3 3 3 3 3 3 3 3]
 [4 4 4 4 4 4 4 4 4]
 [5 5 5 5 5 5 5 5 5]
 [6 6 6 6 6 6 6 6 6]
 [7 7 7 7 7 7 7 7 7]
 [8 8 8 8 8 8 8 8 8]
 [9 9 9 9 9 9 9 9 9]]
y
[[1 2 3 4 5 6 7 8 9]
 [1 2 3 4 5 6 7 8 9]
 [1 2 3 4 5 6 7 8 9]
 [1 2 3 4 5 6 7 8 9]
 [1 2 3 4 5 6 7 8 9]
 [1 2 3 4 5 6 7 8 9]
 [1 2 3 4 5 6 7 8 9]
 [1 2 3 4 5 6 7 8 9]
 [1 2 3 4 5 6 7 8 9]]
 
x, y = np.mgrid[1:10:3j, 1:10:3j]
x
 [[ 1.   1.   1. ]
 [ 5.5  5.5  5.5]
 [10.  10.  10. ]]
y
[[ 1.   5.5 10. ]
 [ 1.   5.5 10. ]
 [ 1.   5.5 10. ]]
'''
ax = plt.subplot(111, projection='3d')
x, y = np.mgrid[-1:1:40j, -1:1:40j]
z = x ** 2 - y ** 2
args = dict(
    cmap='Blues_r',
    linewidth=0.4,
    alpha=1,
    vmin=-1,
    vmax=1
)
ax.plot_surface(x, y, z, **args)
ax.view_init(azim=-30, elev=10)
plt.show()
