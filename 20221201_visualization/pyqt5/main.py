# pip install pyqt5 matplotlib
import sys
import numpy as np

from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout

from Gps import Gps
from ui.ui_mainwindow import Ui_MainWindow
from PlotBar import PlotBar


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # frame 裡有一個 layout, 再將物件加入 layout中
        self.vlayout = QVBoxLayout(self.frame)
        self.bar = PlotBar(parent=self)
        self.vlayout.addWidget(self.bar)
        data = np.random.randint(1, 20, 10)
        self.bar.refresh(data)
        self.flag = False  # 表示還沒開始執行, 抽象化, 用一個不相干的東西來表達另一個東西的狀況
        self.btn.clicked.connect(self.btn_click)

    def btn_click(self, event):
        self.flag = not self.flag
        if self.flag:
            self.btn.setText("停止")
            self.thread = Gps()
            self.thread.callback.connect(self.draw_fig)
            self.thread.start()
        else:
            self.btn.setText("開始")
            self.thread.runFlag = False

    def draw_fig(self, data):
        self.bar.refresh(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
