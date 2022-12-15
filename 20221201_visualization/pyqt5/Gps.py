import random

import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal


class Gps(QThread):
    callback = pyqtSignal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.runFlag = True

    def run(self):
        while self.runFlag:
            count = random.randint(2, 20)  # 抓到幾顆衛星的訊號
            data = np.random.randint(1, 20, count)  # 衛星強度(其實是介於 0~1)
            self.callback.emit(data)
            self.sleep(1)


