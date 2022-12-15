# i=0
# while i<100:
#     print(i)
# 若沒有改變 i 值的機制, 將會變成無窮迴圈
# 無窮迴圈, 無止盡執行下去
'''
當 "=" 的左右二邊都一樣時，可以簡化如下
i=i+5  # "i=i" -5 +6 ...
i+=5 : i=i+5
i-=5 : i=i-5
i*=5 : i=i*5
i/=5 : i=i/5
i%=5 : i=i%5
'''

# i=0
# while i<100:
#     print(i)
#     i=i+1 #每次進1


# for i in range(1,100):
#     print(i)

# i=100
# while i>0:
#     print(i)
#     i-=5
#     #i=i-5 # 100往下數, 每次減5

'''
"." : 的
pikachu.level=20
pikachu.level=pikachu.level+10
pikachu.level+=10
'''

while True: # 無窮迴圈
    a=input("請輸入數字: ")
    if a=="q":
        break
    print(a)



