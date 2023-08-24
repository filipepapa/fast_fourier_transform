#%%
import yfinance as yf
import pandas as pd
import numpy as np

import cufflinks as cf
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
# plt.style.use('seaborn')
plt.style.use('default')
mpl.rcParams['figure.figsize'] = [10.0, 6.0]
mpl.rcParams['font.size'] = 10
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['axes.grid'] = True

#%%
df = yf.download('SPY',start='2005-01-01',end='2023-08-18')
df.to_csv('data/SPY_D1.csv')

df['Close'].plot()

ar_fft = np.fft.fft(df['Close'])

ar_fft