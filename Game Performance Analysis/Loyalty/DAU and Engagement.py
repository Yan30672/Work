import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


gamedict = {5901:'BB連環奪寶', 1514:'MG擺脫PC', 155:'MG擺脫Mobile', 8003:'JDB變臉', 5902:'BB糖果派對', 1389:'MG幸運雙星', 22923:'CQ9跳高高',\
            5908:'BB糖果派對2', 21:'GPK糖果嘉年華', 22416:'PT三倍猴子', 35:'GPK寶石糖果派對', 14030:'JDB三倍金剛', 22495:'PT龍龍龍'}

pd.set_option('display.max_columns', None)
df = pd.read_csv('data.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['RegisterTime'] = pd.to_datetime(df['RegisterTime'], format = '%Y-%m-%d %H:%M:%S.%f')
df['FirstPlay'] = pd.to_datetime(df['FirstPlay'], format = '%Y-%m-%d')
df['code'] = df['code'].astype(int)

print(df)
max = df.date.max()
min = df.date.min()
print(max, min)

df.loc[:, 'date'] = (df.loc[:, 'date'] - max).astype('timedelta64[D]')

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
fig, axes = plt.subplots(nrows=2,ncols=3)



rawdata1 = df[df['code'] == 5901].drop(columns=['code', 'RegisterTime', 'FirstPlay'])
DAUdata1 = rawdata1.groupby(['date'])['memberid'].count().reset_index(name='DAU')
betcountdata1 = rawdata1.groupby(['date'])['ct'].sum().reset_index(name='betcount')
engagement1 = DAUdata1.merge(betcountdata1, on = 'date')
engagement1['Eng'] = engagement1['betcount'] / engagement1['DAU']
print(engagement1['Eng'].describe())
engagement1.plot.line(x = 'date', y = 'Eng', ax = axes[0,0])
engagement1.plot.line(x = 'date', y = 'DAU', ax = axes[0,0])
axes[0,0].set_xlabel('days ago')
axes[0,0].set_ylabel('betcount/DAU')
axes[0,0].set_title('Engagement of {}'.format(gamedict[5901]), fontproperties=font)

rawdata2 = df[df['code'] == 5902].drop(columns=['code', 'RegisterTime', 'FirstPlay'])
DAUdata2 = rawdata2.groupby(['date'])['memberid'].count().reset_index(name='DAU')
betcountdata2 = rawdata2.groupby(['date'])['ct'].sum().reset_index(name='betcount')
engagement2 = DAUdata2.merge(betcountdata2, on = 'date')
engagement2['Eng'] = engagement2['betcount'] / engagement2['DAU']
print(engagement2['Eng'].describe())
engagement2.plot.line(x = 'date', y = 'Eng', ax = axes[0,1])
engagement2.plot.line(x = 'date', y = 'DAU', ax = axes[0,1])
axes[0,1].set_xlabel('days ago')
axes[0,1].set_ylabel('betcount/DAU')
axes[0,1].set_title('Engagement of {}'.format(gamedict[5902]), fontproperties=font)

rawdata3 = df[df['code'] == 5908].drop(columns=['code', 'RegisterTime', 'FirstPlay'])
DAUdata3 = rawdata3.groupby(['date'])['memberid'].count().reset_index(name='DAU')
betcountdata3 = rawdata3.groupby(['date'])['ct'].sum().reset_index(name='betcount')
engagement3 = DAUdata3.merge(betcountdata3, on = 'date')
engagement3['Eng'] = engagement3['betcount'] / engagement3['DAU']
print(engagement3['Eng'].describe())
engagement3.plot.line(x = 'date', y = 'Eng', ax = axes[0,2])
engagement3.plot.line(x = 'date', y = 'DAU', ax = axes[0,2])
axes[0,2].set_xlabel('days ago')
axes[0,2].set_ylabel('betcount/DAU')
axes[0,2].set_title('Engagement of {}'.format(gamedict[5908]), fontproperties=font)

rawdata4 = df[df['code'] == 21].drop(columns=['code', 'RegisterTime', 'FirstPlay'])
DAUdata4 = rawdata4.groupby(['date'])['memberid'].count().reset_index(name='DAU')
betcountdata4 = rawdata4.groupby(['date'])['ct'].sum().reset_index(name='betcount')
engagement4 = DAUdata4.merge(betcountdata4, on = 'date')
engagement4['Eng'] = engagement4['betcount'] / engagement4['DAU']
print(engagement4['Eng'].describe())
engagement4.plot.line(x = 'date', y = 'Eng', ax = axes[1,0])
engagement4.plot.line(x = 'date', y = 'DAU', ax = axes[1,0])
axes[1,0].set_xlabel('days ago')
axes[1,0].set_ylabel('betcount/DAU')
axes[1,0].set_title('Engagement of {}'.format(gamedict[21]), fontproperties=font)

rawdata5 = df[df['code'] == 35].drop(columns=['code', 'RegisterTime', 'FirstPlay'])
DAUdata5 = rawdata5.groupby(['date'])['memberid'].count().reset_index(name='DAU')
betcountdata5 = rawdata5.groupby(['date'])['ct'].sum().reset_index(name='betcount')
engagement5 = DAUdata5.merge(betcountdata5, on = 'date')
engagement5['Eng'] = engagement5['betcount'] / engagement5['DAU']
print(engagement5['Eng'].describe())
engagement5.plot.line(x = 'date', y = 'Eng', ax = axes[1,1])
engagement5.plot.line(x = 'date', y = 'DAU', ax = axes[1,1])
axes[1,1].set_xlabel('days ago')
axes[1,1].set_ylabel('betcount/DAU')
axes[1,1].set_title('Engagement of {}'.format(gamedict[35]), fontproperties=font)

engagement1.to_csv('eng{}.csv'.format(5901))
engagement2.to_csv('eng{}.csv'.format(5902))
engagement3.to_csv('eng{}.csv'.format(5908))
engagement4.to_csv('eng{}.csv'.format(21))
engagement5.to_csv('eng{}.csv'.format(35))
engagement = engagement3.merge(engagement4, on = 'date').drop(columns=['date', 'DAU_x', 'DAU_y', 'betcount_x', 'betcount_y'])
engagement.to_csv('t-test34.csv')
plt.show()