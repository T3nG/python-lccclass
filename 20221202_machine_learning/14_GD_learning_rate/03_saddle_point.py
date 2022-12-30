import numpy as np
import pylab as plt

shrink_y = 1e6
ax = plt.subplot()
x = np.linspace(-30, 60, 100)
y = (np.power(x, 4) - 60 * pow(x, 3) - x + 1) / shrink_y
plt.plot(x, y)
plt.show()
