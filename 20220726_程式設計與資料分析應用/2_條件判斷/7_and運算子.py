#空姐錄取標準
#1. height >= 160  放行李
#2. age <= 45      心臟病等高危險因子
#二者缺一不可

height=eval(input("請輸入身高 : "))
age=eval(input("請輸入年紀 : "))
if height>=160 and age <=45:
    print("錄取")
else:
    print("不符合資格")


'''
height   age   結果
180      30     v
180      50     x
150      30     x
150      30     x
-----------------------
    and 真值表：二者皆為真，才為真
       True   False
True   True   False
False  False  False
-----------------------
'''