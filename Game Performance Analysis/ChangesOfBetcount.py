import pandas as pd
import matplotlib.pyplot as plt
import datetime as DT
from sklearn.linear_model import LinearRegression

def DatetoNum(x, today):
  delta = today - x
  return delta.days


df = pd.read_csv('Users_BetCt.csv')
memberlist = df.member.unique().tolist()
print('本紀錄總共有{}位會員'.format(len(memberlist)))


try:
  num = int(input('請輸入你要求的第幾位會員:'))
  print('現在顯示第{}位會員{}的交易紀錄'.format(num, memberlist[num-1]))
  #轉換時間成datetime格式
  df.loc[:,'date'] = pd.to_datetime(df.loc[:,'date'], format='%Y/%m/%d')
  #增加一個column以2019,1,7為0，往前推為負數
  today = DT.datetime(2019, 1, 9)
  df.loc[:, 'day'] = df.loc[:, 'date'].apply(lambda x: -DatetoNum(x, today))
  data = df[df.loc[:, "member"] == memberlist[num-1]]
  X = data['day'].values
  Y = data['Betcount'].values
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
