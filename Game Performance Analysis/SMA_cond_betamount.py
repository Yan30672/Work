import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
from pylab import *

zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\kaiu.ttf')
pd.set_option('display.max_columns', None)
df = pd.read_csv('BetPayOff_WithCode.csv')
data = df.drop(['rawdatatype', 'gametype', 'website'], axis=1)
data.loc[:, 'payoff'] = round(data.loc[:, 'payoff'], 1)

gamelist = data.code.unique().tolist()
gamedict = {5901:'BB連環奪寶', 1514:'MG擺脫PC', 155:'MG擺脫Mobile', 8003:'JDB變臉', 5902:'BB糖果派對', 1389:'MG幸運雙星', 22923:'CQ9跳高高',\
            5908:'BB糖果派對2', 21:'GPK糖果嘉年華', 22416:'PT三倍猴子', 35:'GPK寶石糖果派對', 14030:'JDB三倍金剛', 22495:'PT龍龍龍'}
print(gamedict)

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)


#plot
fig, axes = plt.subplots(nrows=2, ncols=3)
plt.suptitle('Probability of Loss-LDW-Win conditioned on betamount')


#在限制payoff的情況下，每一筆betamount的可能情況不太一樣，所以必須要先列出所有可能的betamount之後merge
data1 = data[data['code'] == 5901].sort_values(by = ['betamount', 'payoff']).drop(columns=['code'])
bet1 = data1.groupby(['betamount'])['ct'].sum().reset_index(name='ct')
total1 = bet1['ct'].sum()

#LDW和W需要將相同betamount但不同payoff作合併
L1 = data1[data1['payoff'] == -1].sort_values(by = ['betamount']).drop(columns = ['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
LDW1 = data1[(data1['payoff'] > -1) & (data1['payoff'] <= 0)].sort_values(by = ['betamount']).drop(columns = ['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
W1 = data1[data1['payoff'] > 0].sort_values(by = ['betamount']).drop(columns=['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
PL1 = L1['ct'].sum() / total1
PLDW1 = LDW1['ct'].sum() / total1
PW1 = W1['ct'].sum() / total1


All1 = pd.merge(pd.merge(pd.merge(bet1, L1, on = 'betamount').rename(index = str, columns = {"ct_x":"Total", "ct_y":"Loss"}).fillna(0), LDW1, on = 'betamount')\
             .rename(index = str, columns = {"ct":"LDW"}).fillna(0), W1, on = 'betamount').rename(index=str, columns = {"ct":"Win"}).fillna(0)
All1['Check'] = All1['Loss'] + All1['LDW'] + All1['Win'] - All1['Total']
All1['loss'] = All1['Loss'] / All1['Total']
All1['ldw'] = All1['LDW'] / All1['Total']
All1['win'] = All1['Win'] / All1['Total']

axes[0,0].axhline(y = PL1, color = '#1f77b4')
axes[0,0].axhline(y = PLDW1, color = '#ff7f0e')
axes[0,0].axhline(y = PW1, color = '#2ca02c')
All1.plot(x = 'betamount', y = 'loss', kind = 'line', ax = axes[0,0], label = 'Loss')
All1.plot(x = 'betamount', y = 'ldw', kind = 'line', ax = axes[0,0], label = 'LDW')
All1.plot(x = 'betamount', y = 'win', kind = 'line', ax = axes[0,0], label = 'Win')
axes[0,0].set_xlabel('betamount')
axes[0,0].set_ylabel('probability')
axes[0,0].set_title('Conditional density of Loss of {}'.format(gamedict[5901]), fontproperties=font)


#在限制payoff的情況下，每一筆betamount的可能情況不太一樣，所以必須要先列出所有可能的betamount之後merge
data2 = data[data['code'] == 5902].sort_values(by = ['betamount', 'payoff']).drop(columns=['code'])
bet2 = data2.groupby(['betamount'])['ct'].sum().reset_index(name='ct')
total2 = bet2['ct'].sum()

#LDW和W需要將相同betamount但不同payoff作合併
L2 = data2[data2['payoff'] == -1].sort_values(by = ['betamount']).drop(columns = ['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
LDW2 = data2[(data2['payoff'] > -1) & (data2['payoff'] <= 0)].sort_values(by = ['betamount']).drop(columns = ['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
W2 = data2[data2['payoff'] > 0].sort_values(by = ['betamount']).drop(columns=['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
PL2 = L2['ct'].sum() / total2
PLDW2 = LDW2['ct'].sum() / total2
PW2 = W2['ct'].sum() / total2

All2 = pd.merge(pd.merge(pd.merge(bet2, L2, on = 'betamount').rename(index = str, columns = {"ct_x":"Total", "ct_y":"Loss"}).fillna(0), LDW2, on = 'betamount')\
             .rename(index = str, columns = {"ct":"LDW"}).fillna(0), W2, on = 'betamount').rename(index=str, columns = {"ct":"Win"}).fillna(0)
All2['Check'] = All2['Loss'] + All2['LDW'] + All2['Win'] - All2['Total']
All2['loss'] = All2['Loss'] / All2['Total']
All2['ldw'] = All2['LDW'] / All2['Total']
All2['win'] = All2['Win'] / All2['Total']


axes[0,1].axhline(y = PL2, color = '#1f77b4')
axes[0,1].axhline(y = PLDW2, color = '#ff7f0e')
axes[0,1].axhline(y = PW2, color = '#2ca02c')
All2.plot(x = 'betamount', y = 'loss', kind = 'line', ax = axes[0,1], label = 'Loss')
All2.plot(x = 'betamount', y = 'ldw', kind = 'line', ax = axes[0,1], label = 'LDW')
All2.plot(x = 'betamount', y = 'win', kind = 'line', ax = axes[0,1], label = 'Win')
axes[0,1].set_xlabel('betamount')
axes[0,1].set_ylabel('probability')
axes[0,1].set_title('Conditional density of Loss of {}'.format(gamedict[5901]), fontproperties=font)


#在限制payoff的情況下，每一筆betamount的可能情況不太一樣，所以必須要先列出所有可能的betamount之後merge
data3 = data[data['code'] == 5908].sort_values(by = ['betamount', 'payoff']).drop(columns=['code'])
bet3 = data3.groupby(['betamount'])['ct'].sum().reset_index(name='ct')
total3 = bet3['ct'].sum()

#LDW和W需要將相同betamount但不同payoff作合併
L3 = data3[data3['payoff'] == -1].sort_values(by = ['betamount']).drop(columns = ['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
LDW3 = data3[(data3['payoff'] > -1) & (data3['payoff'] <= 0)].sort_values(by = ['betamount']).drop(columns = ['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
W3 = data3[data3['payoff'] > 0].sort_values(by = ['betamount']).drop(columns=['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
PL3 = L3['ct'].sum() / total3
PLDW3 = LDW3['ct'].sum() / total3
PW3 = W3['ct'].sum() / total3
All3 = pd.merge(pd.merge(pd.merge(bet3, L3, on = 'betamount').rename(index = str, columns = {"ct_x":"Total", "ct_y":"Loss"}).fillna(0), LDW3, on = 'betamount')\
             .rename(index = str, columns = {"ct":"LDW"}).fillna(0), W3, on = 'betamount').rename(index=str, columns = {"ct":"Win"}).fillna(0)
All3['Check'] = All3['Loss'] + All3['LDW'] + All3['Win'] - All3['Total']
All3['loss'] = All3['Loss'] / All3['Total']
All3['ldw'] = All3['LDW'] / All3['Total']
All3['win'] = All3['Win'] / All3['Total']


axes[0,2].axhline(y = PL3, color = '#1f77b4')
axes[0,2].axhline(y = PLDW3, color = '#ff7f0e')
axes[0,2].axhline(y = PW3, color = '#2ca02c')
All3.plot(x = 'betamount', y = 'loss', kind = 'line', ax = axes[0,2], label = 'Loss')
All3.plot(x = 'betamount', y = 'ldw', kind = 'line', ax = axes[0,2], label = 'LDW')
All3.plot(x = 'betamount', y = 'win', kind = 'line', ax = axes[0,2], label = 'Win')
axes[0,2].set_xlabel('betamount')
axes[0,2].set_ylabel('probability')
axes[0,2].set_title('Conditional density of Loss of {}'.format(gamedict[5908]), fontproperties=font)


#在限制payoff的情況下，每一筆betamount的可能情況不太一樣，所以必須要先列出所有可能的betamount之後merge
data4 = data[data['code'] == 21].sort_values(by = ['betamount', 'payoff']).drop(columns=['code'])
bet4 = data4.groupby(['betamount'])['ct'].sum().reset_index(name='ct')
total4 = bet4['ct'].sum()

#LDW和W需要將相同betamount但不同payoff作合併
L4 = data4[data4['payoff'] == -1].sort_values(by = ['betamount']).drop(columns = ['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
LDW4 = data4[(data4['payoff'] > -1) & (data4['payoff'] <= 0)].sort_values(by = ['betamount']).drop(columns = ['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
W4 = data4[data4['payoff'] > 0].sort_values(by = ['betamount']).drop(columns=['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
PL4 = L4['ct'].sum() / total4
PLDW4 = LDW4['ct'].sum() / total4
PW4 = W4['ct'].sum() / total4

All4 = pd.merge(pd.merge(pd.merge(bet4, L4, on = 'betamount').rename(index = str, columns = {"ct_x":"Total", "ct_y":"Loss"}).fillna(0), LDW4, on = 'betamount')\
             .rename(index = str, columns = {"ct":"LDW"}).fillna(0), W4, on = 'betamount').rename(index=str, columns = {"ct":"Win"}).fillna(0)

All4['Check'] = All4['Loss'] + All4['LDW'] + All4['Win'] - All4['Total']
All4['loss'] = All4['Loss'] / All4['Total']
All4['ldw'] = All4['LDW'] / All4['Total']
All4['win'] = All4['Win'] / All4['Total']

axes[1,0].axhline(y = PL4, color = '#1f77b4')
axes[1,0].axhline(y = PLDW4, color = '#ff7f0e')
axes[1,0].axhline(y = PW4, color = '#2ca02c')
All4.plot(x = 'betamount', y = 'loss', kind = 'line', ax = axes[1,0], label = 'Loss')
All4.plot(x = 'betamount', y = 'ldw', kind = 'line', ax = axes[1,0], label = 'LDW')
All4.plot(x = 'betamount', y = 'win', kind = 'line', ax = axes[1,0], label = 'Win')
axes[1,0].set_xlabel('betamount')
axes[1,0].set_ylabel('probability')
axes[1,0].set_title('Conditional density of Loss of {}'.format(gamedict[21]), fontproperties=font)

#在限制payoff的情況下，每一筆betamount的可能情況不太一樣，所以必須要先列出所有可能的betamount之後merge
data5 = data[data['code'] == 35].sort_values(by = ['betamount', 'payoff']).drop(columns=['code'])
bet5 = data5.groupby(['betamount'])['ct'].sum().reset_index(name='ct')
total5 = bet5['ct'].sum()

#LDW和W需要將相同betamount但不同payoff作合併
L5 = data5[data5['payoff'] == -1].sort_values(by = ['betamount']).drop(columns = ['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
LDW5 = data5[(data5['payoff'] > -1) & (data5['payoff'] <= 0)].sort_values(by = ['betamount']).drop(columns = ['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
W5 = data5[data5['payoff'] > 0].sort_values(by = ['betamount']).drop(columns=['payoff']).groupby('betamount')['ct'].sum().reset_index(name = 'ct')
PL5 = L5['ct'].sum() / total5
PLDW5 = LDW5['ct'].sum() / total5
PW5 = W5['ct'].sum() / total5

All5 = pd.merge(pd.merge(pd.merge(bet5, L5, on = 'betamount').rename(index = str, columns = {"ct_x":"Total", "ct_y":"Loss"}).fillna(0), LDW5, on = 'betamount')\
             .rename(index = str, columns = {"ct":"LDW"}).fillna(0), W5, on = 'betamount').rename(index=str, columns = {"ct":"Win"}).fillna(0)
All5['Check'] = All5['Loss'] + All5['LDW'] + All5['Win'] - All5['Total']
All5['loss'] = All5['Loss'] / All5['Total']
All5['ldw'] = All5['LDW'] / All5['Total']
All5['win'] = All5['Win'] / All5['Total']
print(PL5,PLDW5,PW5)

axes[1,1].axhline(y = PL5, color = '#1f77b4')
axes[1,1].axhline(y = PLDW5, color = '#ff7f0e')
axes[1,1].axhline(y = PW5, color = '#2ca02c')
All5.plot(x = 'betamount', y = 'loss', kind = 'line', ax = axes[1,1], label = 'Loss')
All5.plot(x = 'betamount', y = 'ldw', kind = 'line', ax = axes[1,1], label = 'LDW')
All5.plot(x = 'betamount', y = 'win', kind = 'line', ax = axes[1,1], label = 'Win')
axes[1,1].set_xlabel('betamount')
axes[1,1].set_ylabel('probability')
axes[1,1].set_title('Conditional density of Loss of {}'.format(gamedict[35]), fontproperties=font)

plt.show()