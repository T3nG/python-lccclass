import pylab as plt
import numpy as np
from matplotlib import animation

# x = np.random.randint(1, 10, 10)
# y = np.random.randint(1, 10, 10)
# 以上兩者可以用zip結合, 底下用python迴圈產生資料, 速度較慢
d = [(np.random.randint(1, 10), np.random.randint(1, 10)) for i in range(10)]
fig, ax = plt.subplots()  # 先產生 figure畫布 ax子繪圖區

# 動畫的函數, 必須要有一個參數, 接收外部傳進來的 frames的值
def run(data):
    ax.clear()
    # ax.axis("off")
    ax.set_xlim(1, 10)
    ax.set_ylim(1, 10)
    ax.scatter(data[0], data[1])


plt.axis('off')

# update every 500ms, 每一點的座標傳到 frames
ani = animation.FuncAnimation(fig, run, frames=d, interval=300)
# 儲存成 gif
# ani.save('animation.gif', fps=10)
plt.show()
