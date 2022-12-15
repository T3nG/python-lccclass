class Pokemon():
    count=0
    def __init__(self):
        Pokemon.count+=1
p1=Pokemon()
p2=Pokemon()
p3=Pokemon()
print(f"目前共有{Pokemon.count}隻神奇寶貝")
# 類別變數 : 存在類別之中, 並不會下降到物件之中
# 寫於類別之內, 方法之外
# 取用類別變數, 前面須加類別名稱 Pokemon.count
# 類別變數是所有類別下的物件共用的
# 可以使用物件名.類別變數 => p1.count 但嚴格禁止
# 此為Java, Python早期物件導向的 bug, 但年代久遠, 為了相容性, 所以無法更改
# 但 C# 就真的無法使用　p1.count
# 類別變數是在程式載入時, 尚未執行前就存在的,
# 類別變數好比太陽, 當人類還沒出現時就存在著
# p1.count 的寫法就好比, 我的太陽, 你的太陽