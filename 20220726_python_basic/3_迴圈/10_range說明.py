#list 會強迫惰性函數執行 next()，直到最後
print(range(1,11))
print(list(range(1,11)))
print(list(range(11)))            #起始值為 0 時，可以省略不寫 print(list(range(0,11)))
print(list(range(1,10,2)))        #range(起始值, 結束值, 步進值)
print(list(range(10,1,-2)))       #步進值為負值時，起始值要比結束值大
print("第一列", "第二列", "第三列")  #使用 ","都會出現空白
print("%s%s%s" % ("第一列","第二列","第三列"))  #若不想要有空白，就要用格式化列印
print("第二列", end="") #end=""表示讓其沒有結束字元，雖然也可以加字元進去啦...預設結束字元是"\n"(換行)
print("第三列")