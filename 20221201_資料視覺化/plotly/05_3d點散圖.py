import plotly.graph_objects as go
import numpy as np
'''
np.eye(3) 斜方差, 共異變數
x = [1, 2, 3]
y = [4, 5, 6]
xm = x.mean() 平均數
斜方差: (1-xm)(4-ym) + (2-xm)(5-ym) + (3-xm)(6-ym)
'''
# x, y, z = np.random.multivariate_normal(np.array([0, 0, 0]), np.eye(3), 20).transpose()
# x = np.random.random([20])
# print(x)
size = 200

# 測試
# tt = np.random.multivariate_normal(np.array([0, 0, 0]), np.eye(3), 10)
# print(tt)

# transpose() , 切分給三份分給 x, y, z
x, y, z = np.random.multivariate_normal(np.array([0, 0, 0]), np.eye(3), size).transpose()
trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    # 點旁邊的線條, a = 透明度 alpha
    line=dict(color='rgba(217,0,0,0.14)', width=0.5),
    # 圓點球體的透明度
    marker=dict(
        # color='rgba(255,0,0,0.5)',
        color=z,  # 不同高度給不同顏色
        colorscale='Viridis',  # 單色深淺, ctrl+左鍵點 Scatter3d, 搜尋 Viridis, 以找尋不同顏色
        size=3,
        symbol='circle',
        opacity=0.5
    ),
    # opacity=0.5  # 整體的透明度, 會影響上述單獨設定好的透明度
)
data = [trace1]
fig = go.Figure(data=data)
fig.show()
