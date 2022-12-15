# 父子類別的建構子都是同名稱 __init__ , 所以一定會覆蓋,
# 除非子類別不寫建構子
'''
Java 語法
public class Pokemon{
   public Pokemon(){
   }
}
class Pikachu extends Pokemon{
    public Pikachu(){
        super(): 自動加
    }
}
'''

# 因為 Java會自動在子類別加上 super, 所以建議在Python中,
# 最好在子類別手動加入 super(), 讓父子有關連
class Pokemon():
    def __init__(self, level=1):
        self.level=level
class Pikachu(Pokemon):
    def __init__(self):
        print("皮卡丘出生了")
        super().__init__(10)
p1=Pikachu()
print(p1.level)

# 以上說明, 每次看的時候, 感覺都不一樣, 大概會經過3~4次才會定型