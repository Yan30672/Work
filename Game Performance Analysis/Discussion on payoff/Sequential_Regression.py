import pandas as pd
import matplotlib.pyplot as plt
import datetime as DT
from datetime import timedelta
import numpy as np
from sklearn.linear_model import LinearRegression

def DatetoNum(x, today):
  delta = today - x
  return delta.days

df = pd.read_csv('Users_BetCt.csv')
memberlist = df.member.unique().tolist()
print('本紀錄總共有{}位會員'.format(len(memberlist)))

today = DT.datetime(2019, 1, 9)
df.loc[:,'date'] = pd.to_datetime(df.loc[:,'date'], format='%Y/%m/%d')
df.loc[:,'day'] = df.loc[:,'date'].apply(lambda x: -DatetoNum(x, today))



def sliding_windows(x, window):
    """Create rolling/sliding windows of length ~window~.

    Given an array of shape (y, z), it will return "blocks" of shape
    (x - window + 1, window, z)."""

    return np.array([x[i:i + window] for i 
                    in range(0, x.shape[0] - window + 1)])

def test(x):
    return bet_amts[x,:]




try:
  num = int(input('請輸入你要求的第幾位會員:'))
  print('現在顯示第{}位會員{}的交易紀錄'.format(num, memberlist[num-1]))
  data = df[df.loc[:, "member"] == memberlist[num-1]]
  #轉換時間成datetime格式
  #增加一個column以2019,1,7為0，往前推為負數
  X = data['day'].values
  Y = data['count'].values
  X = X.reshape(len(X), 1)
  Y = Y.reshape(len(X), 1)
  x = X[-8:-1]
  y = Y[-8:-1]
  model = LinearRegression()
  model.fit(x,y)
  print(model.coef_)
  plt.scatter(x,y, color='black')
  plt.plot(x, model.predict(x), color='blue', linewidth =3)
  plt.xticks()
  plt.yticks()
  plt.show()
except IndexError:
  print('請輸入小於{}的數字'.format(len(memberlist)))

wdow = 7
alldays = pd.DataFrame(data = np.unique(df.day), columns = ['day'])
fill_blanks = pd.concat([data,alldays], join='outer')
fill_blanks.sort_values( by=['day'])
fill_blanks.reindex
fill_blanks.loc[pd.isnull(fill_blanks.loc[:,'count_']),'count_'] = 0
fill_blanks.loc[pd.isnull(fill_blanks.loc[:,'member']),'member'] = memberlist[num-1]
fill_blanks.loc[fill_blanks.loc[:,'count_'] > 0 ,'idd'] = 1
fill_blanks.loc[pd.isnull(fill_blanks.loc[:,'idd']),'idd'] = 0
fill_blanks.loc[:,'7d'] = fill_blanks.rolling(7,min_periods = 1).idd.sum()
bet_amts = sliding_windows(fill_blanks.loc[:,'count_'], window=wdow)
tot_vals = sliding_windows(fill_blanks.loc[:,'day'], window=wdow)





  
  
