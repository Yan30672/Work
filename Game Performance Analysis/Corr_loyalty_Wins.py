import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('loyaldata3m_Wins.csv')
pd.set_option('display.max_columns', None)

data1 = df[df['code'] == 5901]
data2 = df[df['code'] == 5902]
data3 = df[df['code'] == 5908]
data4 = df[df['code'] == 21]
data5 = df[df['code'] == 35]

print(data1['loyalty'].corr(data1['wins']))
print(data2['loyalty'].corr(data2['wins']))
print(data3['loyalty'].corr(data3['wins']))
print(data4['loyalty'].corr(data4['wins']))
print(data5['loyalty'].corr(data5['wins']))

fig, axes = plt.subplots(2,3)
data1.plot(x = 'loyalty', y = 'wins', kind = 'scatter', ax = axes[0,0])
data2.plot(x = 'loyalty', y = 'wins', kind = 'scatter', ax = axes[0,1])
data3.plot(x = 'loyalty', y = 'wins', kind = 'scatter', ax = axes[0,2])
data4.plot(x = 'loyalty', y = 'wins', kind = 'scatter', ax = axes[1,0])
data5.plot(x = 'loyalty', y = 'wins', kind = 'scatter', ax = axes[1,1])
plt.show()