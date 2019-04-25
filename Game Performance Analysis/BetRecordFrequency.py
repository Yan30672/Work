import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Users_BetCt.csv')
memberlist = df.member.unique().tolist()
print('本紀錄總共有{}位會員'.format(len(memberlist)))

try:
  num = int(input('請輸入你要求的第幾位:'))
  print('現在顯示第{}位會員{}的交易紀錄'.format(num, memberlist[num-1]))
  df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
  data1 = df[df.loc[:, "member"] == memberlist[num-1]]
  data = pd.pivot_table(data1, index='date', values='Betcount', aggfunc=sum)
  data.plot(kind = 'line', title='The Bet Record of the memberid {}'.format(num))
  plt.show()
except IndexError:
  print('請輸入小於{}的數字'.format(len(memberlist)))
