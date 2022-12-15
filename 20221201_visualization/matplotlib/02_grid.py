import pylab as plt

plt.xlim(-10, 10)
plt.ylim(-10, 10)
# 畫X軸, 第一點(-10, 0), 第二點(10, 0)
# x = [-10, 10]
# y = [0, 0]
# plot, args: color='', linewidth=

plt.plot([-10, 10],[0, 0], color='k', linewidth=0.5)  # X軸
plt.plot([0, 0],[-10, 10], color='k', linewidth=0.5)  # Y軸

# X軸, Y軸格線
for i in range(-10, 11):
    plt.plot([i, i], [-10, 10], color='g')
for i in range(-10, 11):
    plt.plot([-10, 10], [i, i], color='g')

plt.show()
