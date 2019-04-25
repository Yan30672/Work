import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

df = pd.read_csv('BetPayOff_WithCode.csv')
data = df.drop(['rawdatatype', 'gametype', 'website'], axis=1)
gamelist = data.code.unique().tolist()
gamedict = {5901:'BB連環奪寶', 1514:'MG擺脫PC', 155:'MG擺脫Mobile', 8003:'JDB變臉', 5902:'BB糖果派對', 1389:'MG幸運雙星', 22923:'CQ9跳高高',\
            5908:'糖果派對2', 21:'GPK糖果嘉年華', 22416:'PT三倍猴子', 35:'GPK寶石糖果派對', 14030:'JDB三倍金剛', 22495:'PT龍龍龍'}
print(gamedict)

try:
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
    #資料整理
    rawdata1 = data[data.loc[:, "code"] == 5901].dropna().groupby('payoff')['ct'].sum().reset_index(name = 'count')
    total1 = rawdata1['count'].sum()
    rawdata1.loc[:, 'ratio'] = rawdata1.loc[:, 'count']/total1
    rawdata2 = data[data.loc[:, "code"] == 5902].dropna().groupby('payoff')['ct'].sum().reset_index(name='count')
    total2 = rawdata2['count'].sum()
    rawdata2.loc[:, 'ratio'] = rawdata2.loc[:, 'count']/total2
    rawdata3 = data[data.loc[:, "code"] == 5908].dropna().groupby('payoff')['ct'].sum().reset_index(name='count')
    total3 = rawdata3['count'].sum()
    rawdata3.loc[:, 'ratio'] = rawdata3.loc[:, 'count']/total3
    rawdata4 = data[data.loc[:, "code"] == 21].dropna().groupby('payoff')['ct'].sum().reset_index(name='count')
    total4 = rawdata4['count'].sum()
    rawdata4.loc[:, 'ratio'] = rawdata4.loc[:, 'count']/total4
    rawdata5 = data[data.loc[:, "code"] == 35].dropna().groupby('payoff')['ct'].sum().reset_index(name='count')
    total5 = rawdata5['count'].sum()
    rawdata5.loc[:, 'ratio'] = rawdata5.loc[:, 'count']/total5
    #擷取需要片段
    payoff1 = rawdata1[(rawdata1.loc[:, "payoff"] <= 5) & (rawdata1.loc[:, "payoff"] > 0)]
    payoff2 = rawdata2[(rawdata2.loc[:, "payoff"] <= 5) & (rawdata2.loc[:, "payoff"] > 0)]
    payoff3 = rawdata3[(rawdata3.loc[:, "payoff"] <= 5) & (rawdata3.loc[:, "payoff"] > 0)]
    payoff4 = rawdata4[(rawdata4.loc[:, "payoff"] <= 5) & (rawdata4.loc[:, "payoff"] > 0)]
    payoff5 = rawdata5[(rawdata5.loc[:, "payoff"] <= 5) & (rawdata5.loc[:, "payoff"] > 0)]
    #plot
    fig, axes = plt.subplots(nrows=2, ncols=3)
    plt.suptitle('Probability Densities on (0, 5]')

    payoff1.plot(x = 'payoff', y = 'ratio', kind = 'line', ax = axes[0,0])
    axes[0,0].set_xlabel('payoff')
    axes[0,0].set_ylabel('ratio')
    axes[0,0].set_title('Probability density of {}'.format(gamedict[5901]), fontproperties=font)

    payoff2.plot(x='payoff', y='ratio', kind='line', ax = axes[0, 1])
    axes[0, 1].set_xlabel('payoff')
    axes[0, 1].set_ylabel('ratio')
    axes[0, 1].set_title('Probability density of {}'.format(gamedict[5902]), fontproperties=font)

    payoff3.plot(x='payoff', y='ratio', kind='line', ax = axes[0, 2])
    axes[0, 2].set_xlabel('payoff')
    axes[0, 2].set_ylabel('ratio')
    axes[0, 2].set_title('Probability density of {}'.format(gamedict[5908]), fontproperties=font)

    payoff4.plot(x='payoff', y='ratio', kind='line', ax = axes[1, 0])
    axes[1, 0].set_xlabel('payoff')
    axes[1, 0].set_ylabel('ratio')
    axes[1, 0].set_title('Probability density of {}'.format(gamedict[21]), fontproperties=font)

    payoff5.plot(x='payoff', y='ratio', kind='line', ax = axes[1, 1])
    axes[1, 1].set_xlabel('payoff')
    axes[1, 1].set_ylabel('ratio')
    axes[1, 1].set_title('Probability density of {}'.format(gamedict[35]), fontproperties=font)

    #show the plot
    plt.show()
except IndexError:
    print('請輸入正確的gameid')