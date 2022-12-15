import pylab as plt
import pandas as pd
import plotly_express as px

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = px.data.gapminder().query('year==2007')
df = df.groupby('continent')['pop'].sum()
print(df)

df.plot(kind='pie', figsize=(6, 6), autopct='%.2f%%')

plt.show()
