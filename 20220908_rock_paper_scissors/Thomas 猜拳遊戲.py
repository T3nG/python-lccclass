'''
"這是一個萬用教學, 若能自行撰寫出猜拳遊戲, 那就學會了90%"
剩下的10%是執行序
Property Editor : PE
1. 開啟 qtdesigner / Main Window / create
2. 依範例拖移 4 個 frame 到視窗內, 於空白處按右鍵 Lay Out / Vertically
3. 選取 4 個 frame (ctrl + 左鍵) ,
   Property Editor / QFrame / frameShadow 自行更改, 讓 frame 更顯眼
4. 加入一個 label 到最上面的 frame, 雙擊左鍵改名, 空白處右鍵 Lay Out / Horizontally
5. Property Editor/ QWidget / font size / 20
                  / QLabel / alignment / Horizontal / Center
6. Object Inspector / 左鍵點選最上方的 frame, Property Editor / QWidget / sizePolicy / Vertical Policy / change to Fixed
7. 拖移 4 個 frame 到第二個 frame, Lay Out / Horizontally
8. 選取中間的兩個 frame , PE/ frameShape Panel ; frameShadow Sunken
9. 2 個 frame 各加入 2 個 label, Lay Out / Vertically
10.上方的 label 由左至右分別改名為 電腦/玩家
11.sizePolicy Vertical fixed / alignment vertical center / font size 12
...
12. Label name 電腦: lblCmp / 玩家: lblPlayer


'''

# User Interface : 使用者介面, 視窗表皮, 由美工人員設計
# 美工與程式設計師是敵對的