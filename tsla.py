import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pylab as pl
import datetime as dt

ts = pd.read_csv('C:\\Users\\user\\.spyder-py3\\TSLA\\TSLA.csv')

import warnings
warnings.filterwarnings('ignore')

#SEE IF NaN VALUES EXISTS
print(ts.isna().any())

#THIS ONE ADDS UP ALL THE NULL VALUES
print(ts.isnull().sum())

#FILLS THE NaN WITH ZERO
ts.fillna(0)

print(ts.describe(include="all"))
print(ts.shape)
print(ts.info())
print(ts.head())
print(ts.dtypes)

#PRINTS CORRELATION
print(ts.corr())


#TO SEE IF THERE A SPIKE OF VARIANCE OF THE VOLUME BEFORE THE RISE
ts['Volume'].rolling(50).var().plot()
plt.show()


#DATE BREAKDOWN

#FIRST CONVERT THE DATE COLUMN TO A DATETIME OBJECT
ts['Date'] = pd.to_datetime(ts['Date'])
print(ts.Date.describe())

#BAR GRAPH OF VOLUME BY DATES
vol_count = ts.Volume.count()
ax = ts.plot.bar(x='Date', y='Volume', rot=0)

#SCATTERPLOT OF ADJUSTED CLOSE BY DATE
ax = sns.scatterplot(x="Date", y="Adj Close", data=ts)

#%%

#DATE, OPEN, HIGH, LOW, CLOSE, ADJ CLOSE, VOLUME


























