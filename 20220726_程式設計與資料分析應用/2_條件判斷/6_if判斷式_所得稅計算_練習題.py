'''
1. 輸入薪資 salary
2. 0    <salary<=20000 : 6%
3. 20000<salary<=40000 : 7%
4. 40000<salary<=60000 : 8%
5. 60000<salary<=80000 : 9%
6. 80000以上 : 13%
請列出薪資，所得稅，實領
'''
# salary=eval(input("請輸入薪資: "))
# if salary<=20000:
#     print(f"薪資:{salary} ,所得稅:{salary*0.06} ,實領:{(salary-salary*0.06)}")
# elif salary<=40000:
#     print(f"薪資:{salary} ,所得稅:{salary*0.07} ,實領:{(salary-salary*0.07)}")
# elif salary<=60000:
#     print(f"薪資:{salary} ,所得稅:{salary*0.08} ,實領:{(salary-salary*0.08)}")
# elif salary<=80000:
#     print(f"薪資:{salary} ,所得稅:{salary*0.09} ,實領:{(salary-salary*0.09)}")
# else:
#     print(f"薪資:{salary} ,所得稅:{(salary*0.13)} ,實領:{(salary-salary*0.13)}")

#精簡，抓出變數，固定出現的放下面就好
# salary=eval(input("請輸入薪資: "))
# tax=float()
# if salary<=20000:
#     tax=0.06
# elif salary<=40000:
#     tax=0.07
# elif salary<=60000:
#     tax=0.08
# elif salary<=80000:
#     tax=0.09
# else:
#     tax=0.13
# print(f"薪資:{salary} ,所得稅:{(salary*tax)},實領:{(salary-salary*tax)}")

#看別人的程式碼，是學程式最快的方法
#只對一半，因為必須看高手的程式碼
#如果看了智障的程式碼，會變得更智障

#pass 就是 todo : 改天再寫
#底下的寫法在 Python 可以，但嚴格禁止，在業界直接 fire
#if 0<salary<=20000:  判斷兩次，效能有差異
#    pass
#pass 什麼都不做，要謝的人太多所以只好謝天，要改的程式太多了，所以只好改天（被老闆知道，那我薪水改天再發） todo:改天有空時再寫


#老師的寫法
salary=eval(input("請輸入薪資: "))
tax=0 #可以不加嗎? 可以啊! 但是，在傳統語言裡，使用變數前一定要先宣告（習慣性）
      #或可以預設 tax=0.13　， else就去掉
if salary <= 20000:
    tax=0.06
elif salary <= 40000:
    tax=0.07
elif salary <= 60000:
    tax = 0.08
elif salary <= 80000:
    tax=0.09
else:
    tax=0.13
print(f"薪資:{salary} , 所得稅:{salary*tax} , 實領:{salary*(1-tax)}")