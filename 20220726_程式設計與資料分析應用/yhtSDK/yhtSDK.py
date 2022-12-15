class yhtSDK():
    # 最大公因數, 輾轉相除法
    def gcd(a,b):
        if a % b:
            return yhtSDK.gcd(b, a % b)
        else:
            return b

