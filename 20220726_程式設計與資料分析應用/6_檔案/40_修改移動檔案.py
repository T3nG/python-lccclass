import os
import shutil
path="e:/test"
files=os.listdir(path)
#Windows 檔案其實不分大小寫
#Linux & Mac 大小寫是不同的
#改檔名, 或是移動(剪下, 貼上), 都是shutil.move
for file in files:
    original=os.path.join(path, file)
    target=os.path.join(path, file).lower().replace("\\", "/") # 檔名改成小寫字母
    shutil.move(original, target)
