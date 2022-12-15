# "a" : append 附加
# file=open("e:/test.txt", "a", encoding="utf-8")
# file.write("第一行\n")
# file.write("第二行\n")
# file.close() #如果沒有close, 整個檔案會壞掉無法讀取

# with-as : 離開區塊後, 會自動close file
with open("e:/test.txt", "a", encoding="utf-8") as file:
    file.write("第一行\n")
    file.write("第二行\n")
# 沒有file.close()也沒關係
