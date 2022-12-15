# import random
# # 0<=random.random()<1
# for i in range(100):
#     #password=random.random() #alt+enter
#     password=random.randint(2,99)
#     #某些函數有包含前後數, 有的沒有, 可以先測試
#     #password=random.randint(2,3) 測試
#     print(password)

import random
password=random.randint(2,99)
print("password : ", password)
max=100
min=1
while True:
    a=eval(input(f"請輸入{min}~{max}之間的數 :"))
    if a==password:
        print("bingo")
        break
    elif a<password:
        min=a
    else:
        max=a
