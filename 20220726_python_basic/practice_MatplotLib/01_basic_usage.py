import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np

# A simple example
# fig, ax = plt.subplots() # create a figure containing a single axes
# ax.plot([1,2,3],[1,4,2]) # plot some data on the axes
# plt.show()

# figure
# fig = plt.figure()           # an empty figure with no Axes
# fig, ax = plt.subplots()     # a figure with a single Axes
# fig, axs = plt.subplots(2,2) # a figure with a 2x2 grid of Axes
# plt.show()

# fig, ax = plt.subplots()
# ax.set_title("Sin Function")
# ax.set_xlabel("Degree")
# ax.set_ylabel("Radian")
# plt.show()

# np.random.seed(19680801)  # seed the random number generator.
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.scatter('a', 'b', c='c', s='d', data=data)
# ax.set_xlabel('entry a')
# ax.set_ylabel('entry b')
# plt.show()

# Object-oriented coding style
# x = np.linspace(0, 2, 100)  # Sample data.
# # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.plot(x, x, label='linear')  # Plot some data on the axes.
# ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
# ax.set_xlabel('x label')  # Add an x-label to the axes.
# ax.set_ylabel('y label')  # Add a y-label to the axes.
# ax.set_title("Simple Plot")  # Add a title to the axes.
# ax.legend();  # Add a legend.
# plt.show()

# pyplot-style
# x = np.linspace(0, 2, 100)  # Sample data.
# plt.figure(figsize=(5, 2.7), layout='constrained')
# plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
# plt.plot(x, x**2, label='quadratic')  # etc.
# plt.plot(x, x**3, label='cubic')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("Simple Plot")
# plt.legend();
# plt.show()

#to be continued...