#def: define 定義
#def 函數名(參數1,參數2,參數3):
#    pass要內縮
def add(x,y):
    print(x+y)
def bubble_sort(x,y):
    pass


#程式的進入點, 由此開始
#當程式碼太長的時候, 方便維護用的 if 這行
#馬上就可以知道程式進入點在哪裡
if __name__=="__main__":
    add(1,5)
    print("函數外")

