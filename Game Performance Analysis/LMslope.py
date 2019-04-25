import pandas as pd
import datetime as DT
import numpy as np
from sklearn.linear_model import LinearRegression

def DatetoNum(x, today):
  delta = today - x
  return delta.days

def mask_6(x):
  result = np.ones_like(x)
  for k in range(6):
    result[k]=0
  return result

def LRcoef(A):
  X = np.array([A[i][0] for i in range(len(A))])
  Y = np.array([A[i][1] for i in range(len(A))])
  X = X.reshape(len(X),1)
  Y = Y.reshape(len(Y),1)
  model = LinearRegression()
  model.fit(X,Y)
  return model.coef_[0][0]

today = DT.datetime(2019, 1, 9)
df = pd.read_csv('Users_BetCt.csv')
df.loc[:, 'date'] = pd.to_datetime(df.loc[:,'date'], format='%Y/%m/%d')
df.loc[:, 'time'] = df.loc[:, 'date'].apply(lambda x: -DatetoNum(x, today))
df.loc[:, 'data_point'] = df.apply(lambda row: [row.time, row.Betcount], axis=1)
df.loc[:, 'data1d'] = df.data_point.shift(1)
df.loc[:, 'data2d'] = df.data_point.shift(2)
df.loc[:, 'data3d'] = df.data_point.shift(3)
df.loc[:, 'data4d'] = df.data_point.shift(4)
df.loc[:, 'data5d'] = df.data_point.shift(5)
df.loc[:, 'data6d'] = df.data_point.shift(6)
df['recent_data'] = df[['data_point', 'data1d', 'data2d', 'data3d', 'data4d', 'data5d', 'data6d']].values.tolist()
mask = df.groupby(['member'])['member'].transform(mask_6).astype(bool)
data = df.loc[mask].drop(columns = ['data1d', 'data2d', 'data3d', 'data4d', 'data5d', 'data6d'])
data.loc[:, 'coef'] = data.apply(lambda row: LRcoef(row.recent_data), axis=1)
data.to_csv('Result.csv')