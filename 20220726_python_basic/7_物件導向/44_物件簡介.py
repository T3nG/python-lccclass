class Student():
    # 在物件導向中, 不稱函數, 改稱方法 method
    # def __init__ : 建構子 Constructor
    # 產生物件時, 會自動執行的方法
    def __init__(self): # initialize
        print("產生物件了喔")
for i in range(10):
    Student() # 匿名物件(沒有指派名字)
s1=Student() # 產生一個學生(物件)
s2=Student()
# 物件 : 宇宙中, 只要能想得到的, 都叫物件
# 只要能描述其特性的, 都叫物件
# 何謂物件?? 舉例
# 鬼 : 長髮, 會飄