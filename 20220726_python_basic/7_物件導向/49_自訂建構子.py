# 建構子沒有參數時(self除外), 稱為預設建構子
# 若建構子有參數, 稱為自訂建構子
# 用於初始化物件的屬性
# 自訂建構子產生物件時, 一定要傳入參數
# 若不傳入, 則自訂建構子需要有預設值
class Pokemon():
    def __init__(self, level=1):
        # level : 區域變數
        # self.level : 物件變數
        # java : this.level : 林北
        self.level=level
p1=Pokemon(10)
#p1.level=10
print(p1.level)
p2=Pokemon()
print(p2.level)