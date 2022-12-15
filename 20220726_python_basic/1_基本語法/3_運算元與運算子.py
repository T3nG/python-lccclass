#運算元與運算子
'''
a=b+3
a, b, 3 : 運算元
=, + : 運算子(operator)

一. 指定運算子 : =
     a=10 : 右邊的值放到左邊
二. 算式運算子 : +-*/, //, %
     print(5//2) #求商數
     print(6%10) #求餘數
三. ++, -- : 加一，減一，Python不支援
     需使用 a=a+1
四. 比較運算子 : >, >=, <, <=, ==, !=
五. 邏輯運算子
     and : 左右兩個條件都要 True，結果才會是 True
     or  : 左右只要一個條件為 True，結果就為 True
'''
print(5//2) #求商數
print(6%10) #求餘數

a=10
a=a+1
print(a)
'''
沒有++是一個遺憾，效能差很多

ax, bx, cx CPU上的暫存器(Register)
a 為RAM上的暫存器
mov : 將後面的資料，搬到前面
inc : 相加
a=a+1 vs a++
==================================
a=a+1                  a++
==================================
底下為組合語言碼
mov ax, a              mov ax, a
mov bx, 1              xinc ax (直接在ax +1)
inc cx, ax, bx         mov a, ax
mov a, cx

差一行，效能差異
經計算 Python 比 C 差了十萬倍速度(比較慢)
因為 Python 為直譯語言，之後也不太可能新增++
那 Python 在紅什麼?
因為Google和nVidia使用他來發展人工智慧
  在老師的網站上有
  IO密集型也適合用他來寫
  計算密集型則適合C
'''
#四. 比較運算子 : >, >=, <, <=, ==, !=
a=10
b=20
print(a>b)  #大於嗎?
print(a<b)  #小於嗎?
print(a==b) #有相等嗎?
print(a!=b) #不相等嗎?

print("")
#五. 邏輯運算子
#    and : 左右兩個條件都要 True，結果才會是 True
#    or  : 左右只要一個條件為 True，結果就為 True
print( True and False)
print( True or False)
print( False and False)
print( False or False)