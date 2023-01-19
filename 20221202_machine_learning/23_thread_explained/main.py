# pip install pyqt5
# 執行緒的 msleep不能當計時器
# 1. 所有執行緒都在 '等待區' 等待
# 2. 只能有一個執行緒進入 '執行區', 執行到一半可能就被退出回 '等待區'
# 3. 下次進入執行區的人, 有可能是上次退出的那個人(執行緒)
# 4. 執行區要執行哪一個執行緒, 沒人知道, 神也不知道
# 5. msleep 是執行緒退到 'block區'
# 6. 在 block區睡足 1 秒後, 會回到等待區等待被召喚
import sys
import time

from PyQt5.QtWidgets import QMainWindow, QApplication

from CountThread import CountThread
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn.clicked.connect(self.btn_click)

    def btn_click(self):
        # 錯誤的寫法 1
        # for i in range(100):
        #     self.lbl.setText(str(i))
        #     time.sleep(1)

        # 錯誤的寫法 2
        # self.thread = CountThread(self.lbl)
        # self.thread.start()

        self.thread = CountThread()
        self.thread.callback.connect(self.count_thread_callback)
        self.thread.start()

    def count_thread_callback(self, msg):
        self.lbl.setText(msg)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
