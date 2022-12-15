import os
# "\" 為跳脫字元: \n:換行, \t:tab鍵, \\:純文字"\"
#Windows 路徑表示法 d:\pictures\2022  使用 反斜線
#Linux 路徑表示法 /home/thomas/pictures/2022 使用 除號
#Linux是目前世界上, 伺服器使用最多的系統
path="C:\\Users\\User\\OneDrive\\圖片\\CCUT-圖"
path2="C:\\Users\\User\\OneDrive\\CCUT"
path3="C://Users//User//OneDrive//CCUT"
path4="C:\\Users\\User\\OneDrive\\鯨鯨"
#在Windows之下, 會自動將 / 除號轉成 \\ 兩個反斜線
#反斜線vs除號, 因為商業考量才更改, 不成文規定 統一用 \\ 或 // ,用兩條
#可以把資料夾內的子目錄下的資料也印出來嗎? 可以, 用遞迴函數 Recursive, 後續會提到
files=os.listdir(path4) #files為list的格式
fs={} #創建一個字典
for file in files:
    fs[file]="" #把files裡的值變成key, 給予""空字串為value

#第一種
if "Increasing dominance.pdf" in files: #非常耗時
    print("已經有了")
else:
    print("無此檔案")

#第二種
if "Increasing dominance.pdf" in fs:    #秒殺, 速度很快
    print("已經有了")
else:
    print("無此檔案")

#為什麼要轉成字典? 因為 hashcode , 資料查找更迅速

