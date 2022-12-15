# pip install pyqt5 plotly plotly-express pyqtwebengine mysql-connector-python
# PyQtWebEngine為一個瀏覽器, 可以內嵌到 QT中
# 它並不是 PyQt的產品, 所以需另外 install, 且它只是一個實驗性質的瀏覽器(由webkit改良而來), 很多功能不支援 比如 html5
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QApplication

from Gold import Gold
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.vlayout = QVBoxLayout(self.frame)
        self.browser = QWebEngineView()
        self.vlayout.addWidget(self.browser)
        self.browser.load(QUrl("https://www.google.com"))
        self.btn.clicked.connect(self.btn_click)

    def btn_click(self, event):
        # 開始上網連線, 取得資料
        # 這是一個很不好的習慣
        self.thread = Gold()
        self.thread.callback.connect(self.draw_fig)
        self.thread.start()

    def draw_fig(self, fig):
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    app.exec()
