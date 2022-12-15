
# 如何取得以下資料呢? 有不同程度的難題需要克服, 以下是老師直接給的
import os.path

ls=["http://mahaljsp.asuscomm.com/lcc/pictures/976519.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/976520.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/976521.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/993512.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/993513.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/993514.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/993515.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/IMG_20211003_172815.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/IMG_20211003_172828.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/IMG_20211003_172831.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/IMG_20211003_172833.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/IMG_20211003_172837.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/IMG_20211003_172855.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/IMG_20211003_172857.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/IMG_20211003_172957.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/IMG_20211003_173001.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/IMG_20211003_173004.jpg",
"http://mahaljsp.asuscomm.com/lcc/pictures/IMG_20211003_173015.jpg"]

import requests

# 前後拆開來分成兩部分
# print(os.path.dirname(l), os.path.basename(l))

path="images"
if not os.path.exists(path):
    os.makedirs(path)
for l in ls:
    print(f"目前正在處理 {l}...")
    filename=os.path.basename(l)
    page=requests.get(l)
    with open(os.path.join(path,filename),'wb') as file:
        file.write(page.content)