import os
# path="E:\Steam\steamapps\common"
# files=os.listdir(path)
# for file in files:
#     print(file)

# 列出子目錄, 及底下所有檔案
path="C:/Users/User/OneDrive/KG"
tree=os.walk(path)
#dirs格式 : 當前目錄絕對路徑, [當前目錄下的子目錄], [當前目錄下的檔案]
# for dirs in tree:
#     print(dirs)

# 1. 把所有的目錄印出
# for root, subdirs, files in tree:
#     print(root)

# 2. 把所有的檔案印出
count=0
for root, subdirs, files in tree:
    for file in files:
        file_lower=file.lower()
        #if file_lower.endswith(".jpg") or file_lower.endswith(".png"):
        if file_lower.endswith(".doc") or file_lower.endswith(".pdf"):
            count+=1
            #print(os.path.join(root, file))
            abs=os.path.join(root,file)
            # 把單一路徑分開顯示, 子目錄os.path.dirname() , 檔案os.path.basename()
            print(os.path.dirname(abs),os.path.basename(abs))
print(f"總共有{count:,d}個pdf,doc檔案")

