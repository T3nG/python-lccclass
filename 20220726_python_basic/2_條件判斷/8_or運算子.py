#疫苗優先施打
#kind : 第一類
#age >= 65

kind=eval(input("請輸入第幾類 : "))
age=eval(input("請輸入年紀 : "))
if kind==1 or age>=65:
    print("優先施打")
else:
    print("放生")

'''
kind   age   結果
1      70    v
1      25    v
9      70    v
9      25    x
----------------------------
魔術數字 : IE : 工業工程
    or 真值表: 一項為真，即為真
       True  False
True   True  True
False  True  False

'''