import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Users_BetCt.csv')
daylist = df.date.unique().tolist()
print('本紀錄總共涵蓋{}天的紀錄'.format(len(daylist)))

#選取第一天count的分布
datedf = df[df['date'] == daylist[20]].drop(['member'], axis = 1)
print(datedf.describe())
datedf.plot(kind = 'box', title = 'Distribution of Count')
plt.show()