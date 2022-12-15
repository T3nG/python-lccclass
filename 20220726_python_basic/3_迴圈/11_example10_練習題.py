'''
a a a a a
b b b b b
c c c c c
a a a a a
b b b b b
'''

for i in range(5):
    for j in range(5):
        if i%3==0:
            print("a ",end="")
        elif i%3==1:
            print("b ",end="")
        elif i%3==2:
            print("c ",end="")
    print()