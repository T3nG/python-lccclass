class Pokemon():
    def __init__(self, level):
        self.level=level
    @staticmethod
    def setSpeed(speed):
        #self.speed=speed 不能在類別方法中使用物件變數
        print(f"傳入的速度為{speed}")

# 不需要產生物件, 直接由類別名稱去調用
Pokemon.setSpeed(10)
