import torch
from PyQt5.QtCore import QThread, pyqtSignal
from torch.backends import cudnn

from data import set_cfg
from yolact import Yolact


class LoadModelThread(QThread):
    callback = pyqtSignal(object)
    def __init__(self, weights, config, parent=None):
        super().__init__(parent)
        self.weights = weights
        self.config = config

    def run(self):
        set_cfg(self.config)
        cudnn.fastest = True
        torch.set_default_tensor_type('torch.cuda.FloatTensor')
        model = Yolact()
        model.load_weights(self.weights)
        model.train(False)
        model = model.cuda()
        self.callback.emit(model)
