#yhtLib 函數庫
#程式設計師的價值在此呈現, 定下名字很重要
import math
def c2f(c):
    f=c*9/5+32
    #print(f)
    return f
    #return None 預設return值
def f2c(f):
    c=(f-32)*5/9
    return c #返回值, 把計算完的c值丟回去f2c(f)

#angle to radian 角度轉弧度
#角度 * pi/180 = 弧度
#弧度 * 180/pi = 角度
#改名稱, 為了日後方便維護
#一個專案如果寫10天, 有可能2天是在改名字

def circle(r, angle):
    x = r * math.cos(angle * math.pi / 180)
    y = r * math.sin(angle * math.pi / 180)
    #多值返回, 其實只返回一個值
    #reture (x,y) 傳回的值是一個tuple
    #任何程式語言, 最多只能傳回一個值
    return x,y #多值返回

#Radian to degree
def rad2deg(r):
    d=r*180/math.pi
    return d

#degree to radian
def deg2rad(d):
    r=d*math.pi/180
    return r

