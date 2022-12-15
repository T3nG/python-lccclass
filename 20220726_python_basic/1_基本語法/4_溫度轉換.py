c=eval(input("請輸入攝氏: "))
f = c*9/5+32
print(f"攝氏:{c}, 華式:{f:.0f}")

f=eval(input("請輸入華式: "))
c = (f-32)*5/9
print(f"華式:{f}, 攝氏:{c:.2f}")