#20220802 if判斷式
#tab 縮排
'''
基本語法
if 條件:
    pass
else:
    pass

程式定義: 有人寫了二三十年, 不知道什麼叫程式
1. 一行一行往下執行
2. 具有 if判斷式
    當某條件成立: 就執行, 或不執行
    就是為了要跳行(跳出一行一行往下執行)
3. 必須具有迴圈的功能: 因為懶
額外註明: html, css 並不是程式, 只是區塊標籤
JavaScript也是一種程式語言
95%的工程師寫不出東西
http://lishiang.asuscomm.com/
立向營造網站
引擎售30萬左右: 利潤30%=9萬
要站在巨人的肩膀上: htc, 有可能翻船的


#1
print(1)
print(2)
print(3)
print(4)
print(5)

#2
print("便當")
print("雞腿")
if 有獎金: #自然語言法
    print("龍蝦")
else:
    print("香蕉")
'''
#3
'''
第一種變形
salary=eval(input("請輸入薪水: "))
if salary>=30000:
    print("龍蝦")
else:
    print("香蕉") 
'''
#else就一定要有if, else只能有一個或零個
#第二種變形
#為組合語言的寫法, 不易用人類的邏輯去思考
# ctrl + / : 將所選區域全部註解

salary=eval(input("請輸入薪水: "))

# if salary<=30000:
#     print("香蕉")
# else:
#     if salary<=60000:
#         print("蘋果")
#     else:
#         if salary<=90000:
#             print("雞")
#         else:
#             print("龍蝦")
# if salary<=30000:
#     print("真是個窮光蛋") # if判斷式 一定要搭配else嗎? 不一定


#第三種變形: 四選一, 一行一行判斷, 滿足條件則執行, 不滿足則跳下一行elif, 直到else
if salary<=30000:
    print("香蕉")
elif salary<=60000:
    print("蘋果")
elif salary<=90000:
    print("雞")
else:
    print("龍蝦")




#eval不要常用嗎? 可能會變得死板板
'''
try:
    salary=int(input("請輸入薪水: "))
except:
    print("輸入錯誤")
'''