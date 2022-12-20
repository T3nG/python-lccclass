import igraph as ig
import pylab as plt

g = ig.Graph(directed=True)  # 可以顯示箭頭, 比如 a->b
v = [f'{i:c}' for i in range(97, 106)]  # ASCII
print(v)

c = ["#ffff00" for i in range(9)]
c[2] = '#ff0000'
c[3] = '#0000ff'
c[5] = '#ff00ff'
c[8] = '#00ff00'

g.add_vertices(v)
g.add_edge('a', 'b')
g.add_edge('b', 'c')
g.add_edge('c', 'd')
g.add_edge('e', 'f')
g.add_edge('f', 'g')
g.add_edge('g', 'h')
g.add_edge('h', 'i')
visual_style = dict(
    vertex_size=0.4,
    vertex_color=c,
    vertex_label=g.vs['name'],
    edge_width=0.8,
    edge_color=c
)
ax = plt.subplot()
ig.plot(g, target=ax, **visual_style)
plt.show()
