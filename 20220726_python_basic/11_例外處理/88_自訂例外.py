# just as an example
class DivZero(ArithmeticError):
    pass
def mymath(x,y):
    if y==0:
        raise DivZero("被除數為0") # raise 丟出 (java的throw)
    return x/y
def main():
    try:
        z=mymath(10,0)
    except DivZero as e:
        raise # 重丟
      # raise e 也可以
    # 等同在此不處理呀, 給主程式處理

if __name__ == '__main__':
    try:
        main()
    except DivZero as e:
        print(e)