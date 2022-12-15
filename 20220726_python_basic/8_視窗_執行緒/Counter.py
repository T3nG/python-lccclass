import sys

from RightCountThread import RightCountThread
from LeftCountThread import LeftCountThread
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui.ui_count import Ui_MainWindow

class Count(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.btn.clicked.connect(self.btnClick)
        self.startFlag=False

    def btnClick(self, event):
        self.startFlag=not self.startFlag
        if self.startFlag:
            self.btn.setText("結束")

            self.t1=LeftCountThread()
            self.t1.callback.connect(self.drawLeft)
            self.t1.start()

            self.t2=RightCountThread()
            self.t2.callback.connect(self.drawRight)
            self.t2.start()
        else:
            self.btn.setText("開始")
            self.t1.runFlag = False
            self.t2.runFlag = False

    def drawLeft(self, num):
        self.lbl1.setText(str(num))

    def drawRight(self, num):
        self.lbl2.setText(str(num))

    def closeEvent(self, event):
        self.t1.runFlag = False
        self.t2.runFlag = False

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=Count()
    w.show()
    app.exec()

# Java : => kotlin 卡特琳
# 物件觀念相近, 但目前還是Java的資源最多,
# 雖可能在不遠的將來被取代
# 認證通過率(全英文) 4000-5000元考試費
# OCA : 70% (都熟悉的話)
# OCP : 50% (必須在業界待個二三年)
# 考過的話可以申請技術移民(綠卡)

# 每一個行程都至少會有一個執行緒
# 主執行緒不可以作太過費時的工作
# 新執行緒不可以操作UI畫面
# 為什麼新執行緒可以更改 QLabel, 因為QLabel有經過特殊設計(Thread Safe)

# 當主執行緒結束, self.t2 一併跟著死亡, 所以RightCountThread物件
# 無法變成主物件(匿名物件), 會被垃圾回收機制收回
# 但在Java/Android裡, 主執行緒死亡, 新執行緒還在背後努力工作, 持續耗電
# 必須使用menu清除所有程式, 才會結束
# UI主執行緒只負責生新執行緒, 無權殺死新執行緒
# callback本身為類別變數, 為什麼使用 t2.callback
# 因為 super().__init__(parent)去執行父類別建構子時
# 會依類別變數 callback, 再產生一個 self.callback
# 然後給予 commit()的功能 : qt 的官網說的