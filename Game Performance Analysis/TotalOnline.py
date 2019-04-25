import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Users_BetCt.csv')
daylist = df.date.unique().tolist()
print('本紀錄總共涵蓋{}天的紀錄'.format(len(daylist)))
df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
data = pd.pivot_table(df, index= 'date', values= 'Betcount', aggfunc= sum)
print(data.tail(3))
lastdaydropped = data.drop(data.index[-1])
lastdaydropped.plot(kind='line')
print(lastdaydropped.describe())
plt.show()