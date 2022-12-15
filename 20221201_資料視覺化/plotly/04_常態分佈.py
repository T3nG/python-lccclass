# pip install matplotlib seaborn
# SAS
import pylab as plt
import seaborn as sns
import numpy as np
batch = 1000
x = np.random.normal(size=batch)
y = np.random.normal(size=batch)
# x = np.random.uniform(size=batch)
# y = np.random.uniform(size=batch)
sd = np.std(x)
plt.plot([-5, 5], [sd, sd])
plt.scatter(x, y, s=0.5)
# sns.histplot(x)
plt.show()
