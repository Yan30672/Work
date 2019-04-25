import pandas as pd
import datetime as DT
import numpy as np


def DatetoNum(x, today):
  delta = today - x
  return delta.days

def mask_6(x):
  result = np.ones_like(x)
  for k in range(6):
    result[k]=0
  return result

today = DT.datetime(2019, 1, 9)
df = pd.read_csv('Wagers.csv')
data = df.loc[:, ['memberid', 'activity', 'wagerscount']]
data.loc[:, 'activity'] = pd.to_datetime(data.loc[:,'activity'], format='%Y/%m/%d')
data.loc[:, 'time'] = data.loc[:, 'activity'].apply(lambda x: -DatetoNum(x, today))
print(data.head())