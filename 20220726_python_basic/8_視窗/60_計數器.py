# 本程式旨在說明執行緒
# 行程 : Process
# 執行緒 : Thread
import sys
import time

from RightCountThread import RightCountThread
from CountThread import CountThread
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
            # 這樣設計會使程式當機
            # for i in range(100):
            #     self.lbl1.setText(str(i))
            #     time.sleep(1) # 單位是秒
            # 主執行緒太忙了, 沒辦法偵測鍵鼠等事件

            # 開始聘請一位秘書self.t1來工作, 做什麼事, 還不知道
            # 詳細內容由CountThread.py去設計 => def run(self)
            # 一定要用物件變數 self.
            # 若沒有加 self, t1會變成區域變數,
            # 主執行緒一離開此區塊, 立刻摧毀這個變數,
            # 但新執行緒還沒跑完, 就會出錯

            #self.t1=CountThread(self.lbl1)
            # 此種寫法是錯誤的, 把老闆的UI元素交給秘書處理, 那為什麼可以執行呢?
            # 因為QLabel是有經過特殊設計的(Thread Safe), 但是會拖慢系統速度

            self.t1 = CountThread() # 新執行緒不可以操作任何UI元件
            #當秘書打電話來時, 要執行的方法(self.draw)
            self.t1.phone.connect(self.draw)

            # 命令這位秘書開始工作
            self.t1.start()

            self.t2=RightCountThread()
            self.t2.callback.connect(self.drawRight)
            self.t2.start()
        else:
            self.btn.setText("開始")
            self.t1.runFlag=False
            self.t2.runFlag=False

    def draw(self, num):
        #UI主執行緒自己顯示
        self.lbl1.setText(str(num))

    def drawRight(self, num):
        self.lbl2.setText(str(num))

    # 養成習慣, 每次視窗結束前, 都要做一些死亡前的準備
    def closeEvent(self, event):
        self.t1.runFlag = False
        self.t2.runFlag = False
        print("t1,t2死掉了")

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

# 千萬不可以用 self.sleep(1) 來當計時器
# Runnable - Running - Blocked - Dead
# 在blocked區睡眠, 結束後到runnable等待, 等待下次被呼叫,
# 產生時間誤差導致不準時