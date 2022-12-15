import random
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui.ui_mainwindow import Ui_MainWindow


class Game(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self) # 繪製視窗

        # 從硬碟載入圖片
        self.imgScissors=QImage("img/scissors.png")
        self.imgRock = QImage("img/rock.png")
        self.imgPaper = QImage("img/paper.png")

        # 預設的大小是 64x64
        self.btnScissors.setIconSize(QSize(200, 200))
        self.btnRock.setIconSize(QSize(200, 200))
        self.btnPaper.setIconSize(QSize(200, 200))

        # QImage => QPixmap => QIcon 每個視窗設計程式處理圖片的機制不同, 只能記起來
        # 要放在 QPushButton 上面的圖片得轉成 QIcon, 顯示於TextLabel的圖片只需轉成QPixmap
        self.btnScissors.setIcon(QIcon(QPixmap(self.imgScissors)))
        self.btnRock.setIcon(QIcon(QPixmap(self.imgRock)))
        self.btnPaper.setIcon(QIcon(QPixmap(self.imgPaper)))

        # test QPixmap
        # self.btnScissors.setPixmap(QPixmap(self.imgScissors))
        # self.btnRock.setPixmap(QPixmap(self.imgRock))
        # self.btnPaper.setPixmap(QPixmap(self.imgPaper))

        # 事件設定 : 連結按紐與程式
        # UI主執行緒會進行迴圈偵測
        self.btnScissors.clicked.connect(self.onBtnClick)
        self.btnRock.clicked.connect(self.onBtnClick)
        self.btnPaper.clicked.connect(self.onBtnClick)

        #self.resize(1024,728)

    # 定義按下按鈕後要執行的程式
    def onBtnClick(self, event):
        player=0
        btn=self.sender() # 是誰傳送出來的呢? 哪個按鈕?
        # QImage => QPixmap => QLabel
        if btn==self.btnScissors:
            player=0
            self.lblPlayer.setPixmap(QPixmap(self.imgScissors))
        elif btn==self.btnRock:
            player=1
            self.lblPlayer.setPixmap(QPixmap(self.imgRock))
        else:
            player=2
            self.lblPlayer.setPixmap(QPixmap(self.imgPaper))

        # 電腦出拳
        # cmp=random.randint(0,2)
        # 無法操控隨機變數, 不行哦, 老闆怎麼會給過呢484
        # 作弊程式, 但其實是正確的寫法
        r=random.random()
        if r<0.2: # 20% 平手
            cmp=player
        elif r<0.4: # 20% 讓你贏
            if player==0:cmp=2
            elif player==1:cmp=0
            else: cmp=1
        else: # 60% 讓你輸
            if player==0:cmp=1
            elif player==1:cmp=2
            else: cmp=0

        if cmp==0:
            self.lblCmp.setPixmap(QPixmap(self.imgScissors))
        elif cmp==1:
            self.lblCmp.setPixmap(QPixmap(self.imgRock))
        else:
            self.lblCmp.setPixmap(QPixmap(self.imgPaper))

        # 判定輸贏
        '''
        演算法
        cmp - player = result
        0     0        0  平手
        0     1       -1  贏
        0     2       -2  輸
        1     0        1  輸
        1     1        0  平手
        1     2       -1  贏
        2     0        2  贏
        2     1        1  輸
        2     2        0  平手
        0 平手  1 -2輸 -1 2贏
        '''
        result=cmp-player
        if result==0:
            self.lblResult.setText("平手")
        elif result==-1 or result==2:
            self.lblResult.setText("你贏了")
        else:
            self.lblResult.setText("輸了")
if __name__=='__main__':
    app=QApplication(sys.argv) # 產生一個UI主執行緒
    w=Game() # 產生視窗物件
    w.show() # 顯示視窗
    app.exec() # 叫執行緒進入idle, 開始偵測鍵盤滑鼠

# 28理論
# 所看到的世界只有 20%
# 80% 的黑暗世界看不到