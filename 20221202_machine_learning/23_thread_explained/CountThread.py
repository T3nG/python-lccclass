from PyQt5.QtCore import QThread, pyqtSignal


class CountThread(QThread):
    callback = pyqtSignal(object)
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.lbl = lbl

    def run(self):
        # 新執行緒不可以操作 UI元件, 否則會引起共競
        # QLabel 是經過特殊設計過的元件(thread safe), 所以才能由新執行緒來操作
        # 其他元件都不能用新執行緒控制
        # for i in range(100):
        #     self.lbl.setText(str(i))
        #     self.sleep(1)
        for i in range(100):
            self.callback.emit(str(i))
            self.msleep(1000)
