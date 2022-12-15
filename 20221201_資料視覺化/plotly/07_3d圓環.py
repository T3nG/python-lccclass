import plotly.graph_objects as go
import numpy as np

angles = 360
r = 100
x = []
y = []
z = []
for a in range(angles*10):
    x.append(r * np.cos(a * np.pi/180))
    y.append(r * np.sin(a * np.pi/180))
# 圓環
# z = np.zeros(angles)
# 彈簧, z軸 0~8 之間 繞 10圈
z = np.linspace(0, 8, angles*10)

fig = go.Figure()
fig.add_trace(
    go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers'
    )
)
fig.show()
