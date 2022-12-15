#問題: 還沒輸入前，price是多少?
#就好像達摩祖師求道時的問題，未曾生我誰是我，生我之時我是誰 => None
#程式設計學到最後，會發現跟佛學哲學會有連結
#學完程式不一定比別人聰明，但絕對不會比別人笨，對世間的看法會不一樣
#visual basic (vb)老師雖然會寫，但他覺得這是很爛的程式語言，都不敢講自己會呢
#print(price*qty)
#can't multiply sequence by non-int of type 'str'
#字串轉乘整數才可以進行計算
#(waiting for input等待輸入)

price=input('請輸入單價 :')
#str(): 將數字轉成字串，但input進來的資料為字串所以不用加str(price)
print("你輸入的單價為 :"+price)
qty=input('請輸入數量 :')
print("你輸入的數量為 :" +qty)

print(eval(price)*eval(qty))
print(eval(price)) #print是我們除錯變數的好幫手
print(eval(qty))

a="5+6/2-3"
print(eval(a)) #4. eval(price) 將裡面的字串，轉成公式，再加以計算

#1. input進來的資料為字串
#2. int(price)轉成整數
#3. float(price)轉成小數
#4. eval(price) 將裡面的字串，轉成公式，再加以計算
#5. "" 及 '' 目前都是一樣的，包含長駐解使用的''''''一直到資料庫才有強制性規定

'''
2016-2022 6年聯成，主要職位為顧問（正式員工）立向營造，月薪五萬，不用上班
2008-2016 8年台北
9年 巨匠，前六年在聲寶，外勞聽不懂thousand，念刀山反而聽懂了

一般來說程式設計不適合線上課程，在巨匠時，許多老師不能適應線上教程式，
走了許多人，只有老師成功轉型

以前在立向的程式是成大碩士生寫的，他幫老闆改善程式，老闆從3W把他加薪到5W（不用上班，當顧問）
以前在台北當主管的經驗，用google翻譯不可能錄取(log除錯經常需要用到英文)
'''