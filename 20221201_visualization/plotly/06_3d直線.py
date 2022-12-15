import plotly.graph_objects as go
import numpy as np
x = np.zeros(20)
y = np.zeros(20)
z = list(range(20))
fig = go.Figure()
fig.add_trace(
    go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='lines+markers'
    )
)
fig.show()
