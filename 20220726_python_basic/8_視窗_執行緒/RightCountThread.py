from PyQt5.QtCore import QThread, pyqtSignal

class RightCountThread(QThread):
    callback=pyqtSignal(int)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.runFlag=True
    def run(self):
        index=0
        while self.runFlag:
            index+=1
            self.callback.emit(index)
            self.sleep(1)