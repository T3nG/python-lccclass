import os
path="e:/test"
if not os.path.exists(path): #如果該目錄不存在, 則
    os.mkdir(path) #make dir 建造一個目錄(新建資料夾)
    print("已建立完成")
else:
    print("目錄已存在")