price=50.2
qty=10
print("單價:"+str(price)+", 數量:"+str(qty)+", 總價:"+str(price*qty)) #一長串很容易打錯
# 第一種格式化列印 : 字串歸字串，數字歸數字
# () : tuple 元組
# 使用 % 分隔文字及後面的數字
# %f : 小數 fraction
# %d : 整數
# %s : 字串 string
# %c : 字元 character
# %.2f : 只印2位小數
# %6.2f : 小數2位數, "." 1位, 整數: 6-2-1=3位, 印出來變成 空格 5 0 . 2 0 共六位
print("單價: %f, 數量: %d, 總價: %f, %s, %c, %c" % (price, qty, price*qty, "恭喜你被貴了", 'a', 97))
print("test: %.2f, %6.2f" % (price, price))

'''
為什麼97印出來會是a
ASCII碼 :
A: 65, B: 66, ...
a: 97, b: 98, ...
0: 48, 1: 49, ...
空格: 32
ESC: 27 
'''

#第二種格式化列印，模仿 C#的寫法，但當變數很多的時候，一一比對很花時間會很亂
print("第二種")
print("單價:{0}, 數量:{1}, 總價:{2}".format(price,qty,price*qty))
print("單價:{}, 數量:{}, 總價:{}".format(price,qty,price*qty))    #或保持空白
print("test:{0:6.2f}".format(price))
print("test:{:6.2f}".format(price))

'''
C# (C sharp) 微軟推出要比拚Java的語言，語法如同Java，非常好用，但有很多的誤解，為什麼呢？
並不是只能寫電動玩具，比如立向營造的管理系統是老師用 C#寫的，反而沒人用 C#寫電玩
ASP.NET 政府單位最喜歡用，業界沒人在用，也屬於 Visual Studio 裡的一種，但非常爛，不要用
但是巨匠一直在推這個
'''

#第三種格式化列印
# MTA不會考，但超常用的（Python的認證 Microsoft Technology Associate）
# MTA 現在已經沒辦法考了，因為他是垃圾，沒有鑑別度
# Java 的 OCP很難考，但有國際認證
# Linux 的 LPIC 也是

# f: format
print("第三種")
print(f"單價:{price}, 數量:{qty}, 總價:{price*qty}")
print(f"test:{price:.2f}, test2:{price:6.2f}")


