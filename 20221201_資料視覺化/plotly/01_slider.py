# http://mahaljsp.asuscomm.com/index.php/2019/10/22/plotly-3d/
# pip install plotly plotly-express
import plotly.graph_objects as go
import numpy as np
import plotly
# 產生繪圖物件
fig = go.Figure()
# 增加軌跡(trace), np.arrange(初值, 尾值, 步進值) 每0.1加一個
for step in np.arange(0, 5, 0.1):
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color='#00ced1', width=6),
            name='v='+str(step),
            x=np.arange(0, 10, 0.01),
            y=np.sin(step*np.arange(0, 10, 0.01))
        )
    )
fig.data[10].visible=True
steps = []
for i in range(len(fig.data)):
    step=dict(
        method='restyle',
        args=['visible', [False]*len(fig.data)]
    )
    step['args'][1][i]=True
    steps.append(step)
sliders = [
    dict(
        active=10,
        currentvalue={'prefix': 'Frequency :'},
        pad={'t': 50},
        steps=steps
    )
]
fig.update_layout(
    sliders=sliders
)
fig.show()
