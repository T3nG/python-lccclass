import mysql.connector as mysql
import numpy as np
import plotly.graph_objects as go
from PyQt5.QtCore import QThread, pyqtSignal
from Gfile.G import G


class Gold(QThread):
    callback = pyqtSignal(object)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        conn = mysql.connect(host=G.host,
                             user=G.user,
                             password=G.password,
                             database=G.database)
        cur = conn.cursor()
        cmd = "select * from 台銀黃金 order by 日期"
        cur.execute(cmd)
        rows = cur.fetchall()
        conn.close()
        cur.close()
        x = list(range(len(rows)))
        buy = [row[2] for row in rows]
        sell = [row[3] for row in rows]
        f = np.poly1d(np.polyfit(x, sell, 10))
        reg = f(x)
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=x,
                y=sell,
                mode='lines',
                line=dict(color='royalblue', width=2)
            )
        )
        self.callback.emit(fig)
