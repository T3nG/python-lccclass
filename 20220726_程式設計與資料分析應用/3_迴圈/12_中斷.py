# for i in range(100):
#     print(i)
#     if i>=50:
#         break #到此為止
# 老師說 break 是一個很沒有用的東西
# 因為多此一舉, 直接設定 range到 51就好了

# for i in range(100):
#     a=input("請輸入一個數字: ")
#     print(a)
#     if a=="q":
#         break

# break 退出整個迴圈
# continue: 後面的事不做

for i in range(100):
    if i %5==0:
        continue #碰到 5的倍數, 不執行下列print, 繼續執行迴圈
    print(i)

