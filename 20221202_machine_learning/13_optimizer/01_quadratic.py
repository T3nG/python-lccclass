# pip install matplotlib
# ref: http://mahaljsp.asuscomm.com/index.php/2022/12/23/optimizer/
import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0, 100, 100)  # 時間, x軸的資料
a = 2  # 2 m/s, 加速度
v = a * t  # 速度
S = (1/2) * a * t ** 2  # 距離, y軸的資料

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].plot(t, v)
ax[0].set_ylabel('speed(m/s)')
ax[0].set_xlabel('time(s)')
ax[0].set_title('Speed')

ax[1].plot(t, S)
ax[1].set_ylabel('distance(m)')
ax[1].set_xlabel('time(s)')
ax[1].set_title('Distance')

plt.show()

'''
S = 1/2 at^2  微分後  v = at  再微分  a=a
y=1/2 9.8x^2  =>  y'=9.8x  =>  y''=9.8  斜率
'''