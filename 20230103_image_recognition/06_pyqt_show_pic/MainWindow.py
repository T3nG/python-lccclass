# pip install pyqt5 opencv-python Pillow
import sys

import cv2
import numpy as np
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QPushButton, QListWidgetItem

from PictureThread import PictureThread
from ui.ui_mainwindow import Ui_MainWindow
from sdk.IvanCv import IvanCv as cv


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.resize(1920, 1080)

        path = 'E:\project\data\img\jpg'
        defaultPath = path.replace('\\', '/')
        self.btnPath.clicked.connect(self.btnPathClick)
        self.lblPath.setText(defaultPath)
        self.picThread = PictureThread(defaultPath)
        self.picThread.callback.connect(self.showPicture)
        self.picThread.start()

    def btnPathClick(self):
        path = QFileDialog.getExistingDirectory()
        if path != '':
            path = path.replace('\\', '/')
            self.picThread.runFlag = False
            self.picThread = None
            self.lblPath.setText(path)
            self.listWidget.clear()
            self.picThread = PictureThread(path)
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
        file = btn.tag.replace('\\', '/')
        img = cv2.imdecode(np.fromfile(file, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        img = img[:, :, ::-1].copy()

        # 圖片縮放
        h, w, _ = img.shape
        r = w / h
        lbl_w = self.lblShow.width()
        lbl_h = self.lblShow.height()
        lbl_r = lbl_w / lbl_h

        # 原圖若比例過大, 則縮小, 反之放大, 使得以放入標籤lblShow中
        if r > lbl_r:
            img = cv.resize(img, lbl_w, int(lbl_w / r))
        else:
            img = cv.resize(img, int(lbl_h * r), lbl_h)

        # 將 cv2格式轉成 QImage, 再轉成 QPixmap才可放入 QLabel中, 寬 高 RGB, 8bit顏色值
        pix = QPixmap(QImage(
            img, img.shape[1], img.shape[0], img.shape[1]*3, QImage.Format_RGB888)
        )
        self.lblShow.setPixmap(pix)

    def closeEvent(self, event):
        self.picThread.runFlag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
