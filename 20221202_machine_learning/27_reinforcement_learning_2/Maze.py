import random
import threading
import time
import tkinter as tk

import numpy as np

cols = 4
rows = 4
unit = 40  # 每格 40像素
gap = 5

class Maze(tk.Tk):
    def __init__(self):
        super().__init__()
        # 產生畫布
        self.canvas = tk.Canvas(
            self,
            bg='white',
            width=cols * unit,
            height=rows * unit,
        )
        self.center = np.array([unit//2, unit//2])
        # 垂直線
        for x in range(0, cols*unit, unit):
            self.canvas.create_line(x, 0, x, rows*unit)
        # 水平線
        for y in range(0, rows*unit, unit):
            self.canvas.create_line(0, y, cols*unit, y)

        # 坑洞與目標
        self.hole_1 = self.rectangle(2, 1, 'black')
        self.hole_2 = self.rectangle(1, 2, 'black')
        self.target = self.oval(2, 2, 'yellow')
        # 初值
        self.rect = self.rectangle(0, 0, 'red')

        self.canvas.pack()  # pack() 才會顯示圖形
        self.reset()
        # 動畫
        # self.thread = threading.Thread(target=self.rnd)
        # self.thread.start()

    def reset(self):
        time.sleep(0.05)
        self.canvas.delete(self.rect)
        self.rect = self.rectangle(0, 0, 'red')
        self.update()
        return 0, 0

    def step(self, action):
        rect_x, rect_y, _, _ = self.canvas.coords(self.rect)  # 取得 初值矩形的左上右下座標
        move_x, move_y = np.array([0,0])
        if action == 0:  # up
            if rect_y > unit:  # 若上面還有空間, 則往上
                move_y -= unit
        elif action == 1:  # down
            if rect_y < (rows - 1)*unit:  # 若下面還有空間, 則往下
                move_y += unit
        elif action == 2:  # left
            if rect_x > unit:  # 若左邊還有空間, 則往左
                move_x -= unit
        elif action == 3:  # right
            if rect_x < (cols - 1)*unit:  # 若右邊還有空間, 則往右
                move_x += unit
        self.canvas.move(self.rect, move_x, move_y)

        s_next = self.canvas.coords(self.rect)
        if s_next == self.canvas.coords(self.target):
            reward = 1
            done = True
            s_next = 'terminal'
        elif s_next in [self.canvas.coords(self.hole_1), self.canvas.coords(self.hole_2)]:
            reward = -1
            done = True
            s_next = 'terminal'
        else:
            reward = 0
            done = False
            # s_next = (行, 列)
            s_next = (int(s_next[0]/unit), int(s_next[1]/unit))
        time.sleep(0.01)
        return s_next, reward, done

    def render(self):
        time.sleep(0.01)
        self.update()

    def coordinate(self, x, y):
        t = unit//2 - gap
        c = self.center + np.array([x*unit, y*unit])
        return c[0]-t, c[1]-t, c[0]+t, c[1]+t
        # 0,0  1,0  2,0  3,0
        # 0,1  1,1  2,1  3,1
        # 0,2  1,2  2,2  3,2
        # 0,3  1,3  2,3  3,3

    def rectangle(self, x, y, color):
        x1, y1, x2, y2 = self.coordinate(x, y)
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def oval(self, x, y, color):
        x1, y1, x2, y2 = self.coordinate(x, y)
        return self.canvas.create_oval(x1, y1, x2, y2, fill=color)

    # 動畫
    def rnd(self):
        while True:
            x = random.randint(0, cols - 1)
            y = random.randint(0, rows - 1)
            self.canvas.delete(self.rectangle_1)
            self.rectangle_1 = self.rectangle(x, y, 'red')
            self.update()
            time.sleep(0.2)
