# 旗標(flag): 使用不具任何意義的數字，代表某一件事
# 在月球插上美國國旗: 何意?? 月球是美國的
# 吳家家訓：不准賭博，不替人家擔保，不借人家車子
# 數位化: 同樣使用某個數，代表某件事
'''
0: 單身
1: 已婚
2: 離婚
3: 同居
4: 同性戀
'''
sex=eval(input("請輸入性別 (0~4) : "))
status=""
if sex == 0:
    status="單身"
    print("允許聯誼")
elif sex==1:
    status="已婚"
    print("拒收會員")
elif sex==2:
    status="離婚"
    print("第二春聯誼會")
elif sex==3:
    status="同居"
    print("別亂搞")
elif sex==4:
    status="同性戀"
else:
    status="輸入錯誤"
print(status)
