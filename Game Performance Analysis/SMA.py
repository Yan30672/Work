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

def SMA(x0, x1, x2, x3, x4):
    if x1 == 0:
        return x0
    elif x2 == 0 and x1 != 0:
        return (x0 + x1) / 2
    elif x3 == 0 and x2 != 0:
        return (x0 + x1 + x2) / 3
    elif x4 == 0 and x3 != 0:
        return (x0 + x1 + x2 + x3) / 4
    else:
        return (x0 + x1 + x2 + x3 + x4) / 5


#SMA with N=5
fig, axes = plt.subplots(nrows=2, ncols=3)
plt.suptitle('Smoothed densities of payoff')

rawdata1 = data[data.loc[:, "code"] == 5901].dropna().groupby('payoff')['ct'].sum().reset_index(name='Count')
rawdata1.loc[:, 'shift1'] = rawdata1['Count'].transform(lambda x: x.shift(1)).fillna(0)
rawdata1.loc[:, 'shift2'] = rawdata1['Count'].transform(lambda x: x.shift(2)).fillna(0)
rawdata1.loc[:, 'shift3'] = rawdata1['Count'].transform(lambda x: x.shift(3)).fillna(0)
rawdata1.loc[:, 'shift4'] = rawdata1['Count'].transform(lambda x: x.shift(4)).fillna(0)
rawdata1['smooth'] = rawdata1.apply(lambda row: SMA(row.Count, row.shift1, row.shift2, row.shift3, row.shift4), axis = 1)
total1 = rawdata1['Count'].sum()

#Losses, LDW, Win
rawdata1['ratio'] = rawdata1.loc[:, 'Count'] / total1
Win1 = rawdata1[rawdata1.payoff >= 0]['ratio'].sum()
LDW1 = rawdata1[(rawdata1.payoff < 0) & (rawdata1.payoff > -1)]['ratio'].sum()
Lose1 = rawdata1[rawdata1.payoff == -1]['ratio'].sum()
group1 = [Lose1, LDW1, Win1]
axes[1,2].plot(group1, color = 'r', label = '{}'.format(gamedict[5901], fontproperties=font))
rawdata1 = rawdata1.drop(rawdata1[rawdata1.payoff > 5].index, axis = 0)
axes[0,0].hist(x = rawdata1['payoff'], weights = rawdata1['ratio'], bins = 61)
axes[0,0].set_xlabel('Payoff')
axes[0,0].set_ylabel('ratio')
axes[0,0].set_title('Density of {}'.format(gamedict[5901]), fontproperties=font)


rawdata2 = data[data.loc[:, "code"] == 5902].dropna().groupby('payoff')['ct'].sum().reset_index(name='Count')
rawdata2.loc[:, 'shift1'] = rawdata2['Count'].transform(lambda x: x.shift(1)).fillna(0)
rawdata2.loc[:, 'shift2'] = rawdata2['Count'].transform(lambda x: x.shift(2)).fillna(0)
rawdata2.loc[:, 'shift3'] = rawdata2['Count'].transform(lambda x: x.shift(3)).fillna(0)
rawdata2.loc[:, 'shift4'] = rawdata2['Count'].transform(lambda x: x.shift(4)).fillna(0)
rawdata2['smooth'] = rawdata2.apply(lambda row: SMA(row.Count, row.shift1, row.shift2, row.shift3, row.shift4), axis = 1)
total2 = rawdata2['Count'].sum()


#Losses, LDW, Win
rawdata2['ratio'] = rawdata2.loc[:, 'Count'] / total2
Win2 = rawdata2[rawdata2.payoff >= 0]['ratio'].sum()
LDW2 = rawdata2[(rawdata2.payoff < 0) & (rawdata2.payoff > -1)]['ratio'].sum()
Lose2 = rawdata2[rawdata2.payoff == -1]['ratio'].sum()
group2 = [Lose2, LDW2, Win2]
axes[1,2].plot(group2, color = 'g', label = '{}'.format(gamedict[5902], fontproperties=font))
rawdata2 = rawdata2.drop(rawdata2[rawdata2.payoff > 5].index, axis = 0)
axes[0,1].hist(x = rawdata2['payoff'], weights = rawdata2['ratio'], bins = 61)
axes[0,1].set_xlabel('Payoff')
axes[0,1].set_ylabel('ratio')
axes[0,1].set_title('Density of {}'.format(gamedict[5902]), fontproperties=font)



rawdata3 = data[data.loc[:, "code"] == 5908].dropna().groupby('payoff')['ct'].sum().reset_index(name='Count')
rawdata3.loc[:, 'shift1'] = rawdata3['Count'].transform(lambda x: x.shift(1)).fillna(0)
rawdata3.loc[:, 'shift2'] = rawdata3['Count'].transform(lambda x: x.shift(2)).fillna(0)
rawdata3.loc[:, 'shift3'] = rawdata3['Count'].transform(lambda x: x.shift(3)).fillna(0)
rawdata3.loc[:, 'shift4'] = rawdata3['Count'].transform(lambda x: x.shift(4)).fillna(0)
rawdata3['smooth'] = rawdata3.apply(lambda row: SMA(row.Count, row.shift1, row.shift2, row.shift3, row.shift4), axis = 1)
total3 = rawdata3['Count'].sum()


#Losses, LDW, Win
rawdata3['ratio'] = rawdata3.loc[:, 'Count'] / total3
Win3 = rawdata3[rawdata3.payoff >= 0]['ratio'].sum()
LDW3 = rawdata3[(rawdata3.payoff < 0) & (rawdata3.payoff > -1)]['ratio'].sum()
Lose3 = rawdata3[rawdata3.payoff == -1]['ratio'].sum()
group3 = [Lose3, LDW3, Win3]
axes[1,2].plot(group3, color = 'b', label = '{}'.format(gamedict[5908], fontproperties=font))
rawdata3 = rawdata3.drop(rawdata3[rawdata3.payoff > 5].index, axis = 0)
axes[0,2].hist(x = rawdata3['payoff'], weights = rawdata3['ratio'], bins = 61)
axes[0,2].set_xlabel('Payoff')
axes[0,2].set_ylabel('ratio')
axes[0,2].set_title('Density of {}'.format(gamedict[5908]), fontproperties=font)



rawdata4 = data[data.loc[:, "code"] == 21].dropna().groupby('payoff')['ct'].sum().reset_index(name='Count')
rawdata4.loc[:, 'shift1'] = rawdata4['Count'].transform(lambda x: x.shift(1)).fillna(0)
rawdata4.loc[:, 'shift2'] = rawdata4['Count'].transform(lambda x: x.shift(2)).fillna(0)
rawdata4.loc[:, 'shift3'] = rawdata4['Count'].transform(lambda x: x.shift(3)).fillna(0)
rawdata4.loc[:, 'shift4'] = rawdata4['Count'].transform(lambda x: x.shift(4)).fillna(0)
rawdata4['smooth'] = rawdata4.apply(lambda row: SMA(row.Count, row.shift1, row.shift2, row.shift3, row.shift4), axis = 1)
total4 = rawdata4['Count'].sum()


#Losses, LDW, Win
rawdata4['ratio'] = rawdata4.loc[:, 'Count'] / total4
Win4 = rawdata4[rawdata4.payoff >= 0]['ratio'].sum()
LDW4 = rawdata4[(rawdata4.payoff < 0) & (rawdata4.payoff > -1)]['ratio'].sum()
Lose4 = rawdata4[rawdata4.payoff == -1]['ratio'].sum()
group4 = [Lose4, LDW4, Win4]
axes[1,2].plot(group4, color = 'k', label = '{}'.format(gamedict[21], fontproperties=font))
rawdata4 = rawdata4.drop(rawdata4[rawdata4.payoff > 5].index, axis = 0)
axes[1,0].hist(x = rawdata4['payoff'], weights = rawdata4['ratio'], bins = 61)
axes[1,0].set_xlabel('Payoff')
axes[1,0].set_ylabel('ratio')
axes[1,0].set_title('Density of {}'.format(gamedict[21]), fontproperties=font)



rawdata5 = data[data.loc[:, "code"] == 35].dropna().groupby('payoff')['ct'].sum().reset_index(name='Count')
rawdata5.loc[:, 'shift1'] = rawdata5['Count'].transform(lambda x: x.shift(1)).fillna(0)
rawdata5.loc[:, 'shift2'] = rawdata5['Count'].transform(lambda x: x.shift(2)).fillna(0)
rawdata5.loc[:, 'shift3'] = rawdata5['Count'].transform(lambda x: x.shift(3)).fillna(0)
rawdata5.loc[:, 'shift4'] = rawdata5['Count'].transform(lambda x: x.shift(4)).fillna(0)
rawdata5['smooth'] = rawdata5.apply(lambda row: SMA(row.Count, row.shift1, row.shift2, row.shift3, row.shift4), axis = 1)
total5 = rawdata5['Count'].sum()


#Losses, LDW, Win
rawdata5['ratio'] = rawdata5.loc[:, 'Count'] / total5
Win5 = rawdata5[rawdata5.payoff >= 0]['ratio'].sum()
LDW5 = rawdata5[(rawdata5.payoff < 0) & (rawdata5.payoff > -1)]['ratio'].sum()
Lose5 = rawdata5[rawdata5.payoff == -1]['ratio'].sum()
group5 = [Lose5, LDW5, Win5]
axes[1,2].plot(group5, 'y',  label = '{}'.format(gamedict[35], fontproperties=font))
rawdata5 = rawdata5.drop(rawdata5[rawdata5.payoff > 5].index, axis = 0)
axes[1,1].hist(x = rawdata5['payoff'], weights = rawdata5['ratio'], bins = 61)
axes[1,1].set_xlabel('Payoff')
axes[1,1].set_ylabel('ratio')
axes[1,1].set_title('Density of {}'.format(gamedict[35]), fontproperties=font)


axes[1,2].set_xlabel('Loss-LDW-Win')
axes[1,2].set_xticks(np.arange(3))
axes[1,2].set_xticklabels(['Lose', 'LDW', 'Win'])
plt.legend(prop=zhfont1)
plt.show()