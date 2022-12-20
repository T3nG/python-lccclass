# pip install igraph matplotlib
# 早期 igraph使用 cairo顯示圖形, 所以要連同 cairo一併安裝, 但用pip卻又裝不起來
# 裝不起來的原因, 是否跟 Python 3.7.9有關, 不知道
# 近來改用 matplotlib(TkInter) 顯示圖形, 所以要連同 matplotlib一併安裝
import pylab as plt
import igraph as ig
'''
Chvatal graph, the Petersen graph or the Tutte graph. This method
generates one of them based on its name (case insensitive). See the
documentation of the C interface of C{igraph} for the names available:
U{https://igraph.org/c/doc}.
'''
ax = plt.subplot()
g = ig.Graph()
g.add_vertices(['X', 'Y', 'Z', 'N'])  # 端點, 頂點, 設定端點數量
visual_style = {}
visual_style['vertex_size'] = 0.5
visual_style['vertex_label'] = g.vs['name']
g.add_edge(0, 1)
g.add_edge('X', 'Y')
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 2)

# **把內容解開
ig.plot(g, target=ax, **visual_style)
plt.show()

# g = ig.Graph.Famous("petersen")
# ig.plot(g, target=ax)
# plt.show()
