# 任天堂, 每年花了一億美金, 共研發了十年
# 2008年, 英業達到台中設分公司
# 繼承, 懶, 不想重新寫
# 父類別的所有方法都會被繼承
# 物件變數都是要由物件方法觸發而產生, 所以沒有繼承問題
# 創造出大致上一樣, 但其實有些微不同的類別
# 謹記原則, 每個子類別相同的功能, 都會集中在父類別中統一保管

class Pokemon():         # 父類別
    def __init__(self, level):
        self.level=level
    def setSpeed(self, speed):
        self.speed=speed
class Pikachu(Pokemon):  # 子類別
    def Lightning(self): # 子類別擴充功能
        print("十萬伏特閃電攻擊")
class Eve(Pokemon):      # 子類別
    pass

p1=Pikachu(10)
p1.setSpeed(100)
print(p1.level)
print(p1.speed) # 不能沒有 p1.setSpeed(100)
p1.Lightning()

e1=Eve(15)
e1.setSpeed(90)
#e1.Lightning() 無法執行