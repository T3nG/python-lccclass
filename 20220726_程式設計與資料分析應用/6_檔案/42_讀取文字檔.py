# "r" : read only
# "w" : write only
# 有中文字, encoding="utf-8"
file=open("e:/test.txt","r",encoding="utf-8")
# 讀取整個檔案, 如果檔案非常大, 可能記憶體不足
#l=file.read()
#print(l)

# 讀取指定的大小
# while True:
#     l=file.read(20) # 讀取20個字
#     if not l:break
#     print(l,end="")

# 讀取整行
while True:
    # .strip() : 刪除 "\n" 換行, 或如上所寫, 在print加入(end="")
    # 但是碰到換行會退出迴圈, 因為連換行的\n也被刪掉了, 下堂課解決
    # line=file.readline().strip() # 刪除 "\n"
    # if not line:break
    # print(line)
    line=file.readline()
    if not line:break
    line=line.strip()
    print(line)