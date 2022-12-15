class Mouse():
    def __init__(self):
        print("生出一隻老鼠了")
for i in range(100000):
    # 匿名物件, 會被垃圾回收機制回收
    # Garbage Collection
    # GC 何時啟動回收, 神也不知道,
    # 但保證在記憶體用光之前會啟動回收
    Mouse() # 匿名, 使用完即丟的特性
