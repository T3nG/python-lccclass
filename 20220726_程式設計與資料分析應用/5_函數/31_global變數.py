def add(x,y):
    # global 變數宣告要放在第一行
    global z # 宣告變數z為global, 下方的z變為外面的z, 而不是產生出來的z
    z=100    # 若無宣告global z, 則為新產生出來的, 不是main的z
    print(f"函數中的z : {z}")
    return z

z=50
k=add(10,20)
print(f"main中的z : {z}")