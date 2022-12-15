import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from ui.ui_mainwindow import Ui_MainWindow


class SimpleWindow(QMainWindow, Ui_MainWindow): # 多重繼承; alt+enter import
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self) # 繪製視窗

if __name__=='__main__': # 主程式的名字
    app=QApplication(sys.argv) # alt+enter import
    w=SimpleWindow()
    w.show()
    app.exec() # 進入idle等待狀態, 開始偵測滑鼠, 按鍵

# 以上是視窗基本款, 得背起來
# 開啟錯誤訊息Debug模式
# PyQT只是顯示錯誤代碼(一連串數字, 例 -15784587), 想顯示錯誤訊息需如下設定
# 工具列/Run/Edit Configurations/Emulate terminal in output console 打勾