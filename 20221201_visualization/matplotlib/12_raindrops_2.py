import pylab as plt
import numpy as np
import threading
import time

fig, ax = plt.subplots()
x = np.random.randint(1, 50, 50)
y = np.random.randint(40, 50, 50)


def run():
    while y.sum() > 0:
        for i in range(len(y)):
            if y[i] > 0:
                y[i] -=1
        ax.clear()
        ax.axis('off')
        ax.set_xlim(0, 50)
        ax.set_ylim(0, 50)
        ax.scatter(x, y, s=80, c=x+y)
        plt.draw()  # 重新渲染plt, 就是重新更新圖例
        # 16~ms, 60fps, 30ms, 33~fps, 沒有sleep的話, 程式跑太快, 還來不及draw, 就會出錯
        time.sleep(0.016666)
        # 手機晶片: soc cpu/gpu/南北橋, 比較有名的, 高通: 驍龍, 聯發科: 天璣
        # 手機電量保持: 40~80%


# C語言並沒有Thread, 是由intel開發pThread的套件才有執行緒的功能
t = threading.Thread(target=run)
t.start()
plt.show()
