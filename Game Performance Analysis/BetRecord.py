import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv('Users_BetCt.csv')
memberlist = df.member.unique().tolist()
print('本紀錄總共有{}位會員'.format(len(memberlist)))
df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
sample = list(random.sample(memberlist, 3))
print('隨機顯示3位會員{}的投注紀錄'.format(sample))
data1 = df[df["member"].isin(sample)]
data = pd.pivot_table(data1, index='date', values='Betcount', columns='member', aggfunc=sum)
data.plot(kind = 'line', title='The Bet Record of random members')
plt.show()
