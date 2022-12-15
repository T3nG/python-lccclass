# SDK : Software Development Kit
# 軟體開發套件
# sdk 的寫法
class ChrisSdk():
    @staticmethod
    def triangle(x, y):
        return (x**2+y**2)**0.5
    @staticmethod
    def tp(v):
        c=299_792_458
        return 1/(1-(c/v)**2)**0.5

# 諸如此類, 分門別類
class MathSdk():
    pass

class PhysicSdk():
    pass


# 函數庫的寫法
def tp(v):
    c=299_792_458
    return 1/(1-(c/v)**2)**0.5

def triangle(x, y):
    return (x**2+y**2)**0.5

# 有用 class 包起來的稱為 Sdk
# 只有 def 定義函數的稱為 Lib 函數庫


m=ChrisSdk()
x=m.triangle(3,4) # 可以, 但禁止(物件調用類別方法)
print(x)

z=ChrisSdk.triangle(3,4)
print(z)