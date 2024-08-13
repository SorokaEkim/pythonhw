import os
import numpy as np
import pandas as pd

import plotly as py
import plotly.io as pio
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


df = pd.read_csv("./lesson8/task4/SBER.csv", sep=';')
ma_size = 20
bol_size = 2

df['DATE'] = pd.to_datetime(df['DATE'], format='%Y%m%d')

SMA = df['CLOSE'].rolling(ma_size).mean()
BB_UP = SMA + df['CLOSE'].rolling(ma_size).std() * bol_size
BB_DOWN = SMA - df['CLOSE'].rolling(ma_size).std() * bol_size

fig = go.Figure()
fig.add_scatter(x=df['DATE'], y=SMA, name='SMA')
fig.add_scatter(x=df['DATE'], y=BB_UP, name='BB_UP')
fig.add_scatter(x=df['DATE'], y=BB_DOWN, name='BB_DOWN')
fig.add_scatter(x=df['DATE'], y=df['CLOSE'], name='CLOSE;', opacity=0.3)
fig.show()
