import os
import shutil

path="e:/test"
# 刪除檔案
abs=os.path.join(path, "20210526_034003542_ios.jpg")
if os.path.exists(abs):
    os.remove(abs)

# 底下必須是空目錄, 才有辦法刪除, 幾乎沒啥用處
#os.removedirs(path)

# 底下的方式很恐怖, 一定要確認路徑是否正確
# 不論是否為空目錄, 都會砍
# 此方法很常用
shutil.rmtree(path) # 等同於 shift + del 的方式(?) 不進垃圾桶
