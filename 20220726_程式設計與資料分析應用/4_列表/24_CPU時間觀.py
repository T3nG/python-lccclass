'''
時間的微觀
1s  = 1,000 (毫秒ms)          thousand (千)   k
    = 1,000,000 (微秒us)      million  (百萬) m (大陸用語 兆)
    = 1,000,000,000 (奈秒ns)  billion  (十億) g
大陸 : 100M : 100兆
CPU : 1GHZ : 表示 1 秒鐘會執行 10 億個指令
        mov ax, 1
        mov bx, 2
        inc cx, ax, bx
        mov a, cx

        1個指令需花費 : 1/10億(秒) = 1奈秒

'''
import time

t1=time.time()
for i in range(1_000_000):
    pass
t2=time.time()
print(f"總花費 : {t2-t1}秒") #跑一百萬次迴圈, 花費幾秒?

#初學者迴圈: 知道要跑幾圈用for , 不確定則用while