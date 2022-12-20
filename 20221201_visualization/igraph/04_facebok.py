import random
import igraph as ig
import pylab as plt
n = 26
persons = {}
for i in range(n):
    friends = set([])
    for j in range (n):
        rng = random.randint(1, n-1)
        if i != rng:
            friends.add(rng)
    persons[i] = friends
for person in persons:
    print(person, persons[person])
print("=========以下是單向關係=========")
# 變成單向關係
single = {}
for i in range(n):
    single[i] = set([])
for person in persons:
    for x in persons[person]:
        single[min(x, person)].add(max(x, person))
for key in single:
    print(key, single[key])

g = ig.Graph()
# 多重關係, 圖很複雜
# g.add_vertices([f'{i+97:c}' for i in persons.keys()])
# for person in persons:
#     for x in persons[person]:
#         g.add_edge(person, x)
g.add_vertices([f'{i+97:c}' for i in single.keys()])
for key in single:
    for x in single[key]:
        g.add_edge(key, x)
s = dict(
    edge_width=0.5,
    vertex_size=0.3,
    vertex_label=g.vs['name']
)
ax = plt.subplot()
ig.plot(g, target=ax, **s)
plt.show()
