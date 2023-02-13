import sys

import cv2
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QListWidgetItem, QPushButton

from LoadModelThread import LoadModelThread
from PictureThread import PictureThread
from detect import detect
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.defaultPath = 'E:\project\data\img\jpg'
        # weightPath = 'weights/yolact_resnet50_54_800000.pth'
        weightPath = 'weights/yolact_base_1999_8000.pth'
        # config = 'yolact_resnet50_config'
        config = 'animal_config'

        self.lblStatus.setText('載入模型中, 請稍後 ...')
        self.loadModelThread = LoadModelThread(weightPath, config)
        self.loadModelThread.callback.connect(self.loadModelThreadCallback)
        self.loadModelThread.start()

        self.btnPath.clicked.connect(self.btnPathClick)

    def loadModelThreadCallback(self, model):
        self.model = model
        self.lblPath.setText(self.defaultPath)
        self.path = self.lblPath.text()
        self.lblStatus.setText('')
        self.picThread = PictureThread(self.path)
        self.picThread.callback.connect(self.showPicture)
        self.picThread.start()

    def showPicture(self, picture):
        btn = QPushButton()
        btn.setIcon(QIcon(picture))
        btn.setIconSize(QSize(400, 300))
        btn.tag = picture.tag.replace('\\', '/')
        btn.clicked.connect(self.btnPictureClick)
        item = QListWidgetItem()
        item.setSizeHint(QSize(400, 300))
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, btn)

    def btnPictureClick(self, tag):
        btn = self.sender()
        # self.detect請參照官網的程式碼
        file = btn.tag.replace('\\', '/')
        img, result = detect(self.model, file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # 將 cv2格式轉成 QImage, 再轉成 QPixmap才可放入 QLabel中, 寬 高 RGB, 8bit顏色值
        pix = QPixmap(QImage(
            img, img.shape[1], img.shape[0], img.shape[1]*3, QImage.Format_RGB888)
        )
        # 圖片縮放
        # w = pix.width()
        # h = pix.height()
        # r = w / h
        # lbl_w = self.lblImg.width()
        # lbl_h = self.lblImg.height()
        # lbl_r = lbl_w / lbl_h
        # # 原圖若比例過大, 則縮小, 反之放大, 使得以放入標籤lblShow中
        # if r > lbl_r:
        #     pix = pix.scaled(lbl_w, int(lbl_w / r))
        # else:
        #     pix = pix.scaled(int(lbl_h * r), lbl_h)
        self.lblImg.setPixmap(pix)

    def btnPathClick(self):
        self.path = QFileDialog.getExistingDirectory()
        if self.path != '':
            self.path = self.path.replace('\\', '/')
            self.picThread.runFlag = False
            self.picThread = None
            self.lblPath.setText(self.path)
            self.listWidget.clear()
            self.picThread = PictureThread(self.path)
            self.picThread.callback.connect(self.showPicture)
            self.picThread.start()

    def closeEvent(self, event):
        self.picThread.runFlag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
