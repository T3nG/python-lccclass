import plotly_express as px
import numpy as np
import pandas as pd

x = []
y = []
z = []
r = 100

for i in range(360*10):
    x.append(r * np.cos(np.pi * i / 180))
    y.append(r * np.sin(np.pi * i / 180))
    z.append(i / 100)

df = pd.DataFrame(data={'x': x, 'y': y, 'z': z})
fig = px.scatter_3d(df, x='x', y='y', z='z')
fig.show()
