# Exception 物件是最大的範圍(父類別), ZeroDivisionError 的範圍比較小(子類別)

# try:
#     print(10/0)
# except Exception as e:
#     print(f"其他錯誤: {e}")
# except ZeroDivisionError as e:
#     print("被除數為0")
# result: 其他錯誤: division by zero


# 範圍比較大的要放在後面, 不然前面放的就沒有意義呀
try:
    print(10/0)
except ZeroDivisionError as e: # press ctrl + 滑鼠指標hover over Zero..
    print("被除數為0")
except Exception as e:
    print(f"其他錯誤: {e}")


'''
class Exception(BaseException):
    pass
class ArithmeticError(Exception)
    pass
class ZeroDivisionError(ArithmeticError):
    pass
'''