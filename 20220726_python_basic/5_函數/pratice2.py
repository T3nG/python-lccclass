from ChrisLib import *
import pylab as plt

plt.figure(figsize=(8,8))
plt.xlim(-90,540,90)
plt.ylim(-3*math.pi,3*math.pi)
plt.plot([-90,540],[0,0])
plt.plot([0,0],[-3*math.pi,3*math.pi])
plt.show()