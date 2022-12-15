import time

from PyQt5.QtCore import QThread, pyqtSignal


# QThread 的 sleep 比預設的 time 有優化過, 而且還有 msleep

class CountThread(QThread):
    # 老闆給秘書的一支電話
    phone=pyqtSignal(int)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.runFlag=True
    # def __del__(self):
    #     self.wait()
    def run(self):
        index=0
        while self.runFlag:
            index+=1
            # 打電話給老闆, 並回報目前的數字
            self.phone.emit(index)
            #self.msleep(100) # msleep 單位為毫秒
            self.msleep(100) # 單位為秒