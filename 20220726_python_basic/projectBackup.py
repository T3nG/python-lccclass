import datetime
import shutil
import os

src = "E:\\project"
dst_dir = "c:\\users\\user\\onedrive\\圖片"
dst="c:\\users\\user\\onedrive\\圖片\\code_backup"

now=datetime.datetime.now()
timeToString=now.strftime("%Y%m%d%H%M%S")
newName="code_backup_"+timeToString
dst_new=os.path.join(dst_dir,newName)

if os.path.exists(dst):
   shutil.move(dst,dst_new)

copysrc=shutil.copytree(src,dst)

# run after each class to backup files to
# D:\User\user\Pictures
# then OneDrive backup

# 資料庫備份
# cmd cd onedrive\圖片\serverbackup
# mysqldump -u dengfixanros -p --routines cloud > cloud202209XX.sql
