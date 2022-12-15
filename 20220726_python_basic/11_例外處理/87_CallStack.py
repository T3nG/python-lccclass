# Call Stack : 調用棧(大陸用語)

# 0. 出錯的寫法
# def mymath(x,y):
#     return x/y
# def main():
#     print(mymath(10,0))
# if __name__ == '__main__':
#     main()

# 1. 在mymath處理例外
# def mymath(x,y):
#     try:
#         z=x/y
#         return z
#     except:
#         print("error")
# def main():
#     print(mymath(10,0))
# if __name__ == '__main__':
#     main()

# 2. 在mymath不處理則會丟給上一層(stack)處理, 稱為 call stack
# def mymath(x,y):
#         z=x/y
#         return z
# def main():
#     try:
#         print(mymath(10,0))
#     except:
#         print("error")
# if __name__ == '__main__':
#     main()
'''
public static void mymath(int x, int y) throws ArithmeticException{}
public static void main(){}
'''
# 3. 或在主程式裡處理
def mymath(x, y):
    z = x / y
    return z
def main():
    mymath(10, 0)
if __name__ == '__main__':
    try:
        main()
    except:
        print("error")

# 4. 若所有層都不處理, 則交由系統處理, 此時就是閃退GG