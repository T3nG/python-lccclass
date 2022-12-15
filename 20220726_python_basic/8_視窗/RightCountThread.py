from PyQt5.QtCore import QThread, pyqtSignal


class RightCountThread(QThread):
    callback=pyqtSignal(int) # 回調
    # phone2=pyqtSignal(object)
    def __init__(self, parent=None):
        super().__init__(parent)
        # 旗標: 使用沒有意義的數字來代表有意義的事情
        self.runFlag=True # 旗標, 目前正在執行
    # t2.start() : 會直接啟動新執行緒, 自動執行run()
    # 所以一定要複寫run()方法
    def run(self):
        index=0
        while self.runFlag:
            index+=1
            self.callback.emit(index)
            self.sleep(1)