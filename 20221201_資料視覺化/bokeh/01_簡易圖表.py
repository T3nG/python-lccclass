# http://mahaljsp.asuscomm.com/index.php/2019/10/04/bokeh/
# pip install bokeh
# matplotlib: 使用 tkinter sdk產生視窗
# bokeh: 利用javascript去寫出來的, 產生出來的圖可以拖移(互動), 以html顯示
import numpy as np

from bokeh.plotting import figure, show, output_file
p = figure(width=800, height=400, title='簡易圖表')

# x = list(range(1, 11))
x = np.linspace(1, 10, 10)
y = np.random.randint(100, 600, 10)

# alpha: 透明度
circle = p.circle(x, y, size=11, color='purple', alpha=0.6)
# glyph: 取得產生的圖, 做額外修改
g = circle.glyph
g.size = 30
g.fill_alpha = 0.2
g.line_dash = [6, 3]
g.line_width = 2
# 為什麼要存檔? 可以由Django執行此.py檔, 儲存.html後再由Django轉向到html網頁
# php也可以執行此.py檔
# system('python PATH/XXX.PY ' (params));  //由php去啟動
output_file('bokeh_sample.html')
show(p)
