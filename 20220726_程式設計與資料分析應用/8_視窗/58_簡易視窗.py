#視窗套件 :
# tkinter : 玩具而已, 無法商業化 (而且很醜)
# wxWidget : 精美(但不是很精美), 免費, 但離商業化還差一大步
# pyQt5 : 精美, 要錢 GPL 模式, 可商業化, GPL: 要嘛付錢, 不然就公布原始碼
#pip install pyQt5 : 有安裝 Anaconda的人會出錯, 一定要移除

# 視窗設計請使用
# qtdesigner
'''
QT Designer
Main Window -> create

目前用不到
Object Inspector ->
remove menubar
remove statusbar

加入元件(左側 Widget Box)
拖移兩個 frame (Containers) 到 main window 視窗內
點選 frame , 右下角 Property Editor -> QFrame 更改參數, 更明顯
在兩個 frame 外按右鍵, Lay Out -> Vertically

加入元件(左側 Widget Box)
拖移 Label (Display Widgets) 到上面的 frame
拖移 Push Button (Buttons) 到下面的 frame

分別點選兩個 frame -> Lay Out Horizontally

右下方更改物件名稱
objectName (Property Editor)
點選 上面的 frame ->  lbl
點選下方的 Push Button -> btn
點選兩下 Push Button -> 更改為 開始

Save as: 在 fcu_0726下新建資料夾 ui, 檔名ui_mainwindow.ui
==================
設定 pyuic : 將 ui 檔轉成 python 檔

File/Settings/Tools/External Tools
按下 +
Name : pyuic
Program : 專案下 venv/Scrips/pyuic5.exe
Argument : $FileName$ -o $FileNameWithoutExtension$.py
Working directory : $ProjectFileDir$\ui
--上述參數及詳細步驟能在MahalJSP找到

下堂課繼續
'''

# 20220906
'''
複習一下
Java, C#, Visual C++, Python : 
基本語法, 資料結構(list, set), 技巧

視窗設計- 向客戶展現誠品的地方 PyQT5
網頁設計- Django (尖狗 D不發音)

視窗設計
1. qtdesigner 設計整個視窗布局
2. 設定編譯程式 pyuic5.exe
3. 將 *.ui檔編譯成 *.py檔
4. 左側目錄ui_mainwindows.ui(XML語法)點選右鍵/External tools/pyuic
5. 會建立新檔案ui_mainwindows.py
6. 開啟ui_mainwindows.py
   若沒有透過pyuic轉檔, 會非常痛苦, 要打50幾行
   
'''