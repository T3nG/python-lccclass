# 變數使用中文的時機
# 1. 應付英文不好的人
# 2. 專業用詞時(比如 : 人孔蓋)
class Pokemon():
    # 寫在 init 裡的物件變數是先天的, 物件生成就有
    # 寫在 init 外的(def setSpeed), 就是要先執行才會生成
    def __init__(self):
        print("神奇寶貝出生了")
        # self.等級=1
        self.level=1
    def setSpeed(self):
        self.speed=100
p1=Pokemon()
# p1.等級=5000 # . : 的 => p1的等級
p1.level=4000
# print(p1.等級)
print(p1.level)
p2=Pokemon()
p2.level=500
print("p1.level : ",p1.level)
print("p2.level : ",p2.level)
p1.setSpeed() # 要先執行才會生成
print("p1.speed : ",p1.speed)

# 1. 物件變數會由類別 copy 一份到每個物件中
# 2. 每個物件變數都獨立存在，不會相互影響
# 3. 物件變數前面要加 self, 若在方法中沒有加self, 則為區域變數
# 4. attribute : 屬性, 也就是物件變數
# 5. 凡是能被描述的特性，都叫物件，所以特性，屬性，物件變數，都是指同一個東西
# 6. Java, C# 物件變數定義在類別內, 只要一new物件, 變數就存在
#    但 Python 一定要執行才會生成
#    kotlin 取代 java