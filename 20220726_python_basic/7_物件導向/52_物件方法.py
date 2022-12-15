class Pokemon():
    def __init__(self, level):
        self.level=level
    def setSpeed(self, s):  # 物件方法
        self.speed=s

p1=Pokemon(1)   # 必須先產生物件
p1.setSpeed(60) # 必須使用物件名稱調用物件方法
print(p1.speed)
