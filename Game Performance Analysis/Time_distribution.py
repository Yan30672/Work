import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('timedist.csv')
df['timediff'] = df['timediff'] / 1000
data = df.groupby(['timediff'])['count'].sum().reset_index(name='count')
total = data['count'].sum()
data.loc[:,'cumsum'] = data.loc[:,'count'].cumsum() / total
print(data)

fig, axes = plt.subplots(nrows=2,ncols=2)

data.plot(x = 'timediff', y = 'cumsum', kind = 'line',  ax = axes[0,0])
axes[0,0].set_title('Distribution of time difference')
data.plot(x = 'timediff', y = 'count', kind = 'line', ax = axes[0,1])
axes[0,1].set_title('Density of time difference')

plt.show()