from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure


# Canvas: 畫布
# PyQt 支援將 TkInter製成的matplotlib嵌入


class PlotBar(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # dpi: dot per inch 每英吋的點數, 解析度的意思
        # super().__init__(parent)
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(1, 1, 1)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)  # 設定 PlotBar 的老爸為 MainWindow
        FigureCanvas.setSizePolicy(
            self,
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        FigureCanvas.updateGeometry(self)

    def plot(self):
        self.ax.clear()
        x = list(range(1, len(self.data)+1))
        self.ax.set_xlim(0, len(self.data)+1)
        self.ax.bar(x, self.data)
        self.draw()

    def refresh(self, data):
        self.data = data
        self.plot()