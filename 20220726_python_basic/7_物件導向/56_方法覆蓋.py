# 方法覆蓋 Override
# Python 沒有方法重載(overload)
# 方法覆蓋發生在父子繼承時, 子類別的方法跟父類別的方法同名稱
# 子類別覆蓋父類別方法時, 父類別方法屍骨無存
# 若想在子類別覆蓋的方法中調用父類別的方法, 就要使用觀落陰法 - super()
# super()只能在子類別方法中調用

class Pokemon():               # 父類別
    def __init__(self, level):
        self.level=level
    def setSpeed(self, speed):
        self.speed=speed
class Pikachu(Pokemon):        # 子類別
    def setSpeed(self, speed):
        print("現在開始設定速度")

p1=Pikachu(10)
p1.setSpeed(100)
# print(p1.speed)
# 若子類別的方法名稱與父類別完全一樣, 會覆蓋掉