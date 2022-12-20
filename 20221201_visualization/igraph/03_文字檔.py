import igraph as ig
import pylab as plt
import numpy as np
g = ig.Graph.Read_Edgelist('data.txt', directed=True)

label = [f'{i:c} ' for i in range(97, 97+11+1)]
s = dict(
    vertex_label=label,
    vertex_size=np.random.randint(1, 10, 11)*0.1)
ax = plt.subplot()
ig.plot(g, target=ax, **s)
plt.show()
