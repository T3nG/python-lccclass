'''
* * * * *  第0列
* * * *    第1列
* * *      ...
* *
*
'''

# for i in range(5,0,-1):
#     for j in range(i):
#         print("* ",end="")
#     print()

for i in range(5):
    for j in range(5-i):  # i=0 時, j in range(5)
        print("* ", end="")
    print()
