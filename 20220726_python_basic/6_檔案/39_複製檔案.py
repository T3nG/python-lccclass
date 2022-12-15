from datetime import datetime
from pathlib import Path
import os
import shutil
path="C:\\Users\\User\OneDrive\圖片\相機相簿\\2021\\05"
target="e:/test"
if not os.path.exists(target):
    os.mkdir(target)
files=os.listdir(path) # 先測試路徑是否正確
for file in files:
    abs_path=os.path.join(path, file)
    if os.path.isfile(abs_path):
        abs_target=os.path.join(target, file)
        print(abs_path, abs_target) # 再次檢查
        shutil.copyfile(abs_path, abs_target) # import shutil
        timestamp=os.path.getmtime(abs_path)
        date_time=datetime.fromtimestamp(timestamp)
        print(date_time.strftime("%Y-%m-%d %H:%M:%S"))
        # 將直接覆蓋舊有的檔案(若已存在)

