# 安裝 graphviz app https://graphviz.org/download/
# 安裝時, Add Graphviz to system path for all user
# 安裝好時重開 pycharm
# 安裝套件
# pip install ann-visualizer graphviz tensorflow==2.10.1
# tensorflow 2.11.0 無法再windows 啟動gpc
# 電腦未安裝 CUDA也無法啟動GPU

from keras.models import Sequential
from keras.layers import Dense
from ann_visualizer.visualize import ann_viz

model = Sequential()
# 第一層
model.add(Dense(
    units=6,  # 輸出筆數
    activation='relu',  # 線性整合
    kernel_initializer='uniform',  # 初始捲積核
    input_dim=11  # 輸入資料筆數
))
# 第二層
model.add(Dense(
    units=6,
    activation='relu',
    kernel_initializer='uniform'
))
# 第三層
model.add(Dense(
    units=2,
    activation='softmax',
    kernel_initializer='uniform'
))
# 繪製模型
ann_viz(model, view=True, title='CNN', filename='ann.gv')

# 開啟 pdf時錯誤, 此檔案已打開, 可能是 pdf的錯誤
# 解決方案, 把所有的.gv檔案刪除, 用 try except